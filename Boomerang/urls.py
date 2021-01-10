from django.urls import path

from Boomerang import views

urlpatterns = [
    path('', views.Boomerang_entertext, name = 'Enter text'),
	path('analysis/', views.Boomerang_analysis, name = 'Analysis'),
]