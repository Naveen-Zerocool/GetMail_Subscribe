from django.urls import path
from . import views


urlpatterns = [
	path('', views.get_mail, name='mail'),
	path('thanks', views.thanks, name='thanks'),
]