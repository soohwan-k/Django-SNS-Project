from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from rest_framework.views import APIView
from .models import Feed

# class Main(APIView):
#     def get(self, request):
#         feed_list = Feed.objects.all().order_by('-pk')
#         return render(request, "content/main.html", context=dict(feeds=feed_list))


class FeedList(ListView):
    model = Feed
    ordering = '-pk'
