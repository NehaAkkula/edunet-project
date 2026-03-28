from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import CustomUser, HomemakerProfile

class CustomerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        return user

class HomemakerSignUpForm(UserCreationForm):
    delivery_radius = forms.IntegerField(label="Delivery Radius (km)", required=True)
    phone = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_homemaker = True
        user.save()
        HomemakerProfile.objects.create(
            user=user,
            delivery_radius=self.cleaned_data.get('delivery_radius'),
            phone=self.cleaned_data.get('phone'),
            address=self.cleaned_data.get('address')
        )
        return user
