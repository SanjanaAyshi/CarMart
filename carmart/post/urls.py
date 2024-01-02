from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('edit/<int:id>', views.EditCartUpdateView.as_view(), name='edit_Cart'),
    path('details/<int:pk>', views.DetailPostView.as_view(), name='detail_post'),
    path('cart/', views.cart, name='view_cart'),
]
