from django.urls import path
from testApp import views

urlpatterns = [
	path('', views.display, name= 'index'),
	path('', views.login, name = 'login'),
	path('', views.signup, name = 'signup'),
	path('moduleEdit', views.moduleEdit, name='moduleEdit'),
	path('modelEdit', views.modelEdit, name='modelEdit'),
	path('modelChoice', views.modelChoice, name='modelChoice'),
	path('register', views.register, name='register'),
]
