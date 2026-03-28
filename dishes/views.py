from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models import Avg
from .models import Dish
from orders.models import Order

class HomeView(TemplateView):
    template_name = 'home.html'

class DishListView(ListView):
    model = Dish
    template_name = 'dishes/menu.html'
    context_object_name = 'dishes'

    def get_queryset(self):
        category = self.request.GET.get('category')
        if category:
            return Dish.objects.filter(category=category)
        return Dish.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = [choice[0] for choice in Dish.CATEGORY_CHOICES]
        context['active_category'] = self.request.GET.get('category', '')
        return context

class HomemakerDashboardView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Dish
    template_name = 'dishes/dashboard.html'
    context_object_name = 'dishes'

    def test_func(self):
        return self.request.user.is_homemaker

    def get_queryset(self):
        return Dish.objects.filter(homemaker=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['incoming_orders'] = Order.objects.filter(dish__homemaker=self.request.user).order_by('-created_at')
        return context

class DishCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Dish
    template_name = 'dishes/dish_form.html'
    fields = ['name', 'price', 'category', 'description', 'ingredients', 'image']
    success_url = reverse_lazy('homemaker_dashboard')

    def test_func(self):
        return self.request.user.is_homemaker

    def form_valid(self, form):
        form.instance.homemaker = self.request.user
        return super().form_valid(form)

class DishDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Dish
    template_name = 'dishes/dish_confirm_delete.html'
    success_url = reverse_lazy('homemaker_dashboard')

class DishDetailView(DetailView):
    model = Dish
    template_name = 'dishes/dish_detail.html'
    context_object_name = 'dish'

class DishUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Dish
    template_name = 'dishes/dish_form.html'
    fields = ['name', 'price', 'category', 'description', 'ingredients', 'image']
    success_url = reverse_lazy('homemaker_dashboard')

    def test_func(self):
        return self.request.user.is_homemaker and self.get_object().homemaker == self.request.user
