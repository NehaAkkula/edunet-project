from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Review
from dishes.models import Dish

class AddReviewView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['rating', 'comment']
    template_name = 'reviews/review_form.html'

    def form_valid(self, form):
        dish = get_object_or_404(Dish, id=self.kwargs['dish_id'])
        form.instance.customer = self.request.user
        form.instance.dish = dish
        try:
            return super().form_valid(form)
        except:
            # Handle duplicate reviews
            return redirect('menu')

    def get_success_url(self):
        return reverse_lazy('menu')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dish'] = get_object_or_404(Dish, id=self.kwargs['dish_id'])
        return context
