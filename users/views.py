from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomerSignUpForm, HomemakerSignUpForm
from .models import CustomUser

class SignUpView(TemplateView):
    template_name = 'users/signup_choice.html'

class CustomerSignUpView(CreateView):
    model = CustomUser
    form_class = CustomerSignUpForm
    template_name = 'users/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class HomemakerSignUpView(CreateView):
    model = CustomUser
    form_class = HomemakerSignUpForm
    template_name = 'users/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Homemaker'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('homemaker_dashboard')

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    
    def get_success_url(self):
        if self.request.user.is_homemaker:
            return reverse_lazy('homemaker_dashboard')
        return reverse_lazy('home')
