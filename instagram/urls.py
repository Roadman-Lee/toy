from django.urls import path

from . import views

app_name = 'instagram' # URL Revers에서 namespace역활을 함

urlpatterns = [
    path('', views.post_list),
    path('<int:pk>/', views.post_detail),
]
