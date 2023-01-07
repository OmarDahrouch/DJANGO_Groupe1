from django.urls import path
from . import views
from django.contrib.auth import views as login_views

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', login_views.LogoutView.as_view(), name='logout')
]
