from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.main_view, name='items.main'),
    path('delete/<pk>/', views.ItemDeleteView.as_view(), name='items.delete'),
    path('update/', views.update_prices, name='items.update'),
    path('register/', views.register, name='items.register'),
    path('login/', views.login, name='items.login'),
    path('logout/', views.logoutUser, name='items.logout'),
]