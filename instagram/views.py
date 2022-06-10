from django.views.generic import ListView, DetailView
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Post


from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import permissions


class VerifyPermissionLevel(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        result = bool(user and user.is_authenticated and user.permission_level >= 0)
        return result


class UserApiView(APIView):
    permission_classes = [VerifyPermissionLevel]
    def get(self, request):
        return Response({"message": "get success!"})




post_list = ListView.as_view(model=Post)


# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)
#     # __incontains : 대소문자 관계없이 쿼리문에 대한 내용을 가지고 옴
#     # instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q': q,
#     })

post_detail = DetailView.as_view(model=Post)

# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     #     raise Http404
#     return render(request, 'instagram/post_detail.html', {
#         'post': post,
#     })

