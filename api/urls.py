from django.urls import path
from api.views import PersonListCreateView, PersonRetrieveUpdateDestroyView

urlpatterns = [
    path('api/', PersonListCreateView.as_view(), name='Person-list-create'),
    path('api/<int:pk>/', PersonRetrieveUpdateDestroyView.as_view(), name='Person-retrieve-update-destroy'),
]
