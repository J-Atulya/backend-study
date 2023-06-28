from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name = 'index'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('loginpage', views.loginpage, name = 'loginpage'),
    path('logout', views.logout, name='logout'),
    #str-> string type; pk -> variable; next code creates a dynamic url => diff for diff user
    path('post/<str:pk>', views.post, name='post')
]