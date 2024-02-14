from django.urls import path, include
from . import views
urlpatterns = [
    path ('', views.home_page, name="home"),
    path ('sting/', views.chatbot_page, name="chatbot"),
    path ('getResponse', views.getResponse, name="getResponse"),
   


]