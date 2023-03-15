from django.urls import path
from api.views import *

urlpatterns = [
    path('api/register/', Register.as_view()),
    path('api/user/', UserDetail.as_view()),
]