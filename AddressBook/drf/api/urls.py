from django.urls import path
from . import views

urlpatterns = [
	path('', views.ApiOverview, name='home'),
	path('create/', views.add_Address, name='add-address'),
	path('all/', views.view_address, name='view_address'),
	path('update/<int:pk>/', views.update_address, name='update-address'),
	path('delete/<int:pk>/', views.delete_address, name='delete-address'),
]
