from django.urls import path
from . import views

urlpatterns=[
    path('logout/', views.logout_view.as_view(), name = 'logout'),
    path('login/', views.login_view.as_view(), name = 'login'),
    path('signup/', views.SignUp.as_view(), name='signup'),]
