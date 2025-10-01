"""
URL configuration for ecommerce_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, register, LoginView
from categories.views import CategoryViewSet
from products.views import ProductViewSet
from cart.views import view_cart, add_to_cart, update_cart, remove_from_cart
from orders.views import OrderViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/register/', register, name='register'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/cart/', view_cart, name='view_cart'),
    path('api/cart/add/', add_to_cart, name='add_to_cart'),
    path('api/cart/update/', update_cart, name='update_cart'),
    path('api/cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('api/', include(router.urls)),
]
