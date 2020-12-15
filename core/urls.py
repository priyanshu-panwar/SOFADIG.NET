from django.urls import path
from . import views

urlpatterns = [
	path('catalog/', views.catalog, name='catalog'),
	path('', views.home, name='home'),
	path('product/<str:pk>/', views.detail, name='detail'),
	path('product/<str:pk>/ingredients/', views.ingredients, name='ingredients'),
	path('category/1/<str:pk>/', views.category_1_details, name='category-1-details'),
	path('category/2/<str:pk>/', views.category_2_details, name='category-2-details'),
	# path('category/3/<str:pk>/', views.category_3_details, name='category-3-details'),
	path('pos/<int:pk>/', views.pos, name='pos'),
	path('contact/', views.contact, name='contact'),
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout'),
	path('request_info/<int:pk>', views.request_info, name='request-info'),
	path('loadxyz/', views.load_data_from_excel, name='load-data'),
	path('loadxyzabc/', views.load_data_stores, name='load-data-stores'),
]