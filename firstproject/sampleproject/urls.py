from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/{application name}/
    path('', views.index, name = 'index'),
    path('createMemo/', views.createMeomo)
]