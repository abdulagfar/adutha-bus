from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'bus'
urlpatterns = [
	path('', views.home_page, name='home_page'),
	path('login/', views.redirect_to_login, name='redirect_to_login'),
	path('add-data/', views.admin_login, name='admin_login'),
	path('added/', views.add_data, name='add_data'),
	path('admin-logout/', views.admin_logout, name='admin_logout'),
	path('logout/', views.admin_logout, name='admin_logout'),
	path('table/', views.show_table),
	path('home/', views.home_page),
	path("bus_details/<int:id>/", views.bus_details),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)