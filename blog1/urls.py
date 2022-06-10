from django.urls import path

from blog1.views import post_list

app_name = 'blog1'

urlpatterns =[
    path('', post_list, name='post_list'),
]