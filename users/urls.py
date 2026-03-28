from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup/customer/', views.CustomerSignUpView.as_view(), name='customer_signup'),
    path('signup/homemaker/', views.HomemakerSignUpView.as_view(), name='homemaker_signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(next_page='home'), name='logout'),
]
