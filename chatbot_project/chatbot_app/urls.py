# chatbot_app/urls.py

from django.urls import path
from .api import api
from . import views  # Import the views module

urlpatterns = [
    path("api/", api.urls),
    path('', views.index, name='index'),  # Map the root URL to the index view
    path('chatbot1/', views.chatbot1, name='chatbot1'),
    path('chatbot2/', views.chatbot2, name='chatbot2'),
]
