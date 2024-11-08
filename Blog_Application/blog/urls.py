from django.urls import path
from .views import *


urlpatterns = [
    path('post/',post_view,name='post_url'),
    path('home/',home_view,name='home_url')
]