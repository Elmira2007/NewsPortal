from django.urls import path
from apps.base.views import *

urlpatterns = [
    path('', index , name='index'),
    path('blog/<int:id>//', blog , name='blog'),
    path('login/', signin, name='login'),
    path('signup/', signup, name='signup')
]
