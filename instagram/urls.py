from django.urls import path
from instagram.views import UserApiView, post_list, post_detail

app_name = 'instagram' # URL Revers에서 namespace역활을 함

urlpatterns = [
    path('', UserApiView.as_view()),
    path('<int:pk>', post_detail)
]
