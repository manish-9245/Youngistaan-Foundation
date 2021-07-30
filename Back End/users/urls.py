from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logoutUser')

]