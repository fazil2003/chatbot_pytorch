from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('chatbot_response/',views.chatbot_response,name='Chatbot Response'),
]
