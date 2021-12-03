from . import views
from django.urls import path

urlpatterns = [
    path('', views.main_view, name='items.main'),
    path('delete/<pk>/', views.ItemDeleteView.as_view(), name='items.delete'),
    path('update/', views.update_prices, name='items.update'),
]