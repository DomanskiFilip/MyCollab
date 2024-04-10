from django.urls import path
from Core import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm




app_name = 'Core'

urlpatterns = [
    path("", views.home, name="home"),
    # path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path("mycollabs/", views.account, name="mycollabs"),
    path('account/', views.account, name='account'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', views.logout_view, name='logout'),
]