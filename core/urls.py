from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('catalog/', views.catalog, name='catalog'),
	path('product/<int:pk>/', views.detail, name='detail'),
	path('product/<int:pk>/ingredients/', views.ingredients, name='ingredients'),
	path('category/<int:pk>/', views.category_details, name='category-details'),
	path('pos/<int:pk>/', views.pos, name='pos'),
	path('contact/', views.contact, name='contact'),
]