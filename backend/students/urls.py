from django.urls import path
from .views import StudentsView


urlpatterns = [
    path('students/', StudentsView.as_view(), name='students'),
]