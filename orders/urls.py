from django.urls import path
from . import views

urlpatterns = [
    path('place/', views.PlaceOrderView.as_view(), name='place_order'),
    path('success/<int:pk>/', views.OrderSuccessView.as_view(), name='order_success'),
    path('history/', views.OrderHistoryView.as_view(), name='order_history'),
    path('<int:pk>/update-status/', views.UpdateOrderStatusView.as_view(), name='update_order_status'),
]
