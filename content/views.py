import os
from uuid import uuid4

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, CreateView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed
from DjangoSNSProject.settings import MEDIA_ROOT


class FeedList(ListView):
    model = Feed
    ordering = '-pk'


class FeedCreate(LoginRequiredMixin, CreateView):
    model = Feed
    fields = ['content', 'image']

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.user_id = current_user
            form.instance.like = 0
            form.instance.profile_image = self.request.user.profile_image
            return super(FeedCreate, self).form_valid(form)
        else:
            return redirect('/main/')


# class UploadFeed(APIView):
#     def post(self, request):
#
#         file = request.data.get('file')
#         image = request.data.get('image')
#
#         print(file)
#         print(image)
#         # file = request.FILES['file']
#         # uuid_name = uuid4().hex
#         # save_path = os.path.join(MEDIA_ROOT, uuid_name)
#         #
#         # with open(save_path, 'wb+') as destination:
#         #     for chunk in file.chunks():
#         #         destination.write(chunk)
#         #
#         # image = uuid_name
#         # content = request.data.get('content')
#         # user_id = request.data.get('user_id')
#         # profile_image = request.data.get('profile_image')
#         #
#         # Feed.objects.create(image=image, content=content, user_id=user_id, profile_image=profile_image, like_count=0)
#
#         return Response(status=200)
