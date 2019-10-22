from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('change_status/<list_id>', views.change_status, name='change_status'),
    path('edit/<list_id>', views.edit, name='edit'),

]
