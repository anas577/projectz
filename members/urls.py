from django.urls import path
from . import views
#we used loggin for name bcz using 'login' causes an error
urlpatterns = [
    path('login_user/', views.login_user, name='loggin'),


]