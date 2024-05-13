from django.urls import path
from . import views  # Импортируем views из текущего приложения
from .views import products_view
urlpatterns = [
    path('', views.index, name='index'),  # Главная страница с товарами
    path('register/', views.register, name='register'),  # Страница регистрации
    path('login/', views.login_view, name='login'),  # Страница входа
    path('logout/', views.logout_view, name='logout'),  # Выход из системы
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('', views.index, name='index'),
    path('products/', products_view, name='products'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),

]

