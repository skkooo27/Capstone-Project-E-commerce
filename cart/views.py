from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from products.models import Product

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    serializer = CartSerializer(cart)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity', 1)
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={'quantity': quantity})
    if not created:
        cart_item.quantity += quantity
        cart_item.save()
    serializer = CartItemSerializer(cart_item)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_cart(request):
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity')
    try:
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
    except (Cart.DoesNotExist, CartItem.DoesNotExist):
        return Response({'error': 'Item not in cart'}, status=status.HTTP_404_NOT_FOUND)
    if quantity <= 0:
        cart_item.delete()
        return Response({'message': 'Item removed'}, status=status.HTTP_204_NO_CONTENT)
    cart_item.quantity = quantity
    cart_item.save()
    serializer = CartItemSerializer(cart_item)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_cart(request, product_id):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
        cart_item.delete()
        return Response({'message': 'Item removed'}, status=status.HTTP_204_NO_CONTENT)
    except (Cart.DoesNotExist, CartItem.DoesNotExist):
        return Response({'error': 'Item not in cart'}, status=status.HTTP_404_NOT_FOUND)
