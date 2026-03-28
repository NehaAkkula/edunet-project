from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import Order
from dishes.models import Dish

class PlaceOrderView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        dish_id = request.POST.get('dish_id')
        dish = get_object_or_404(Dish, id=dish_id)
        
        # In a real app, we'd get the address from the user profile or a form
        # For simplicity, we use the customer's name as address for now or a dummy
        address = "Default Delivery Address"
        if hasattr(request.user, 'homemaker_profile'):
             address = request.user.homemaker_profile.address
        
        order = Order.objects.create(
            customer=request.user,
            dish=dish,
            quantity=1,
            total_price=dish.price,
            delivery_address=address
        )
        return redirect('order_success', pk=order.id)

class OrderSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'orders/order_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = get_object_or_404(Order, id=self.kwargs['pk'], customer=self.request.user)
        return context

class OrderHistoryView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/order_history.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user).order_by('-created_at')

class UpdateOrderStatusView(LoginRequiredMixin, UserPassesTestMixin, View):
    def post(self, request, pk, *args, **kwargs):
        order = get_object_or_404(Order, id=pk)
        new_status = request.POST.get('status')
        if new_status in dict(Order.STATUS_CHOICES):
            order.status = new_status
            order.save()
            messages.success(request, f"Order #{order.id} status updated to {new_status}.")
        return redirect('homemaker_dashboard')

    def test_func(self):
        order = get_object_or_404(Order, id=self.kwargs['pk'])
        return self.request.user == order.dish.homemaker
