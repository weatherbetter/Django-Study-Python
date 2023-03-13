from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/{application name}/
    path('', views.index, name = 'index'),
    path('createMemo/', views.createMemo),
    
    # Get, Post
    path('methodMemo/', views.methodMemo),

    # 수정 페이지 요청
    path('edit/<str:idx>', views.edit),
    # 수정
    path('edit/update/', views.update)
]