from django.urls import path
from api.views import PersonListCreateView, PersonRetrieveUpdateDestroyView

urlpatterns = [
    path('api/', PersonListCreateView.as_view(), name='Get all users or create a user'),
    path('api/<int:pk>/', PersonRetrieveUpdateDestroyView.as_view(), name='Retrieve user,Update user, or delete user'),
]
