from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework.mixins import RetrieveModelMixin,DestroyModelMixin,CreateModelMixin
from order.models import Cart, CartItem, Order, OrderItem
from order.serializer import EmptySerializer, CartSerializer, CartItemSerializer,AddCartItemSerializer,UpdateCartItemSerializer, OrderSerializer, CreateOrderSerializer, UpdateOrderSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from order.services import OrderService

# Create your views here.
class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        if user.is_anonymous:
            return Cart.objects.none()
        
        if Cart.objects.filter(user=user).exists():
            raise ValidationError({
                'message': 'Cart already exists',
            })

        serializer.save(user=user)
        

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return Cart.objects.none()
        return Cart.objects.prefetch_related('items__product').filter(user=user).all()


class CartItemViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names =['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        else:
            return CartItemSerializer
    
    def get_serializer_context(self):
       context ={
           'cart_id': self.kwargs.get('cart_pk')
       }
       return context

    def get_queryset(self):
       items = CartItem.objects.select_related('product').filter(cart_id=self.kwargs.get('cart_pk')).all()
       return items
    
    def perform_create(self, serializer):
        cart_id = self.kwargs.get("cart_pk")

        # 1) Cart exists?
        cart = get_object_or_404(Cart, id=cart_id)

        # 2) Cart owner check
        if cart.user != self.request.user:
            raise ValidationError("You cannot add items to another user's cart")

        # 3) Save FK properly
        serializer.save(cart=cart)


class OrderViewSet(ModelViewSet):
    http_method_names = ['get', 'post','patch', 'delete', 'head','options']


    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def cancel(self, request, pk=None):
        order = self.get_object()
        user = request.user
        OrderService.cancel_order(order=order, user=user)
        return Response({
            'details':f'Your current order status is {order.status}'
        })


    def get_serializer_class(self):
        if self.action == 'cancel':
            return EmptySerializer
        elif self.request.method == "POST":
            return CreateOrderSerializer
        elif self.request.method == "PATCH":
            return UpdateOrderSerializer
        return OrderSerializer
    
    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAdminUser()]
        return [IsAuthenticated()]
    
    def get_serializer_context(self):
        return {
            'user_id':self.request.user.id,
            'user':self.request.user
        }

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return Order.objects.none()
        
        if user.is_staff:
           return Order.objects.prefetch_related('items__product').all()
        return Order.objects.prefetch_related('items__product').filter(user=user)
        
    