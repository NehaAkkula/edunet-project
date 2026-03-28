from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.DishListView.as_view(), name='menu'),
    path('dashboard/', views.HomemakerDashboardView.as_view(), name='homemaker_dashboard'),
    path('add/', views.DishCreateView.as_view(), name='dish_add'),
    path('<int:pk>/', views.DishDetailView.as_view(), name='dish_detail'),
    path('<int:pk>/edit/', views.DishUpdateView.as_view(), name='dish_edit'),
    path('<int:pk>/delete/', views.DishDeleteView.as_view(), name='dish_delete'),
]
