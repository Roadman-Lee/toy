from django.urls import path

from blog1.views import views

urlpatterns =[
    path('', views.post_list, name='post_list'),
]