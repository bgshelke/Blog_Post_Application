from django.urls import path
from .views import *


urlpatterns = [
    path('post/',add_post,name='add_post_url'),
    path('home/',home_view,name='home_url'),
    path('blog_details/<int:pk>/',blog_details,name='blog_details_url')
]