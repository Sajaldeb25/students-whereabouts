from django.urls import path
from .views import RegisterView, LoginView, CategoryView, ProductView, CartItemView, BlacklistRefreshView, UserOrderedItemView, ProductList


urlpatterns = [
    path('students/', StudentsAPIview.as_view(), name='students'),
]