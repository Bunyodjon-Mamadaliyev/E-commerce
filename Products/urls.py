from django.urls import path
from .views import (
    ProductListCreateView, ProductDetailView,
    OrderItemDetailView, OrderItemListCreateView,
    CategoryDetailView, CategoryListCreateView,
    OrderListCreateView, OrderDetailView )

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('orderItem/', OrderItemListCreateView.as_view(), name='orderItem-list'),
    path('orderItem/<int:pk>/', OrderItemDetailView.as_view(), name='orderItem-detail'),
    path('category/', CategoryListCreateView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('order/', OrderListCreateView.as_view(), name='order-list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),

]
