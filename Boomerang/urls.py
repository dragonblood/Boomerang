from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.http import QueryDict

from Boomerang import views

urlpatterns = [
    path('', views.Boomerang_entertext, name = 'Enter text'),
	path('analysis/', views.Boomerang_analysis, name = 'Analysis'),
]