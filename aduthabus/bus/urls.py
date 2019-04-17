from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'bus'
urlpatterns = [
	path('login/', views.redirect_to_login, name='redirect_to_login'),
	path('admin-login/', views.admin_login, name='admin_login'),
	
]