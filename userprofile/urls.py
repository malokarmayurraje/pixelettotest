from django.urls import path
from .views import *


urlpatterns = [
    path('user/', Users.as_view()),
    path('userlist/',UserList.as_view()),
]