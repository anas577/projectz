from django.urls import path
from . import views


urlpatterns = [
    path('login_user/', views.login_user, name='loggin'),
    path('logout_user/', views.logout_user, name='loggout'),
    path('register_user/', views.sign_up, name='reggister'),

]