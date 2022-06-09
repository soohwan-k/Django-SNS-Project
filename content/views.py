from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView
from rest_framework.response import Response

from rest_framework.views import APIView

from user.models import User
from .forms import CommentForm
from .models import Feed, Comment
from DjangoSNSProject.settings import MEDIA_ROOT


class FeedList(ListView):
    model = Feed
    ordering = '-pk'


class FeedDetail(DetailView):
    model = Feed

    def get_context_data(self, **kwargs):
        context = super(FeedDetail, self).get_context_data()
        context['comment_form'] = CommentForm
        return context


# class ProfileList(ListView):
#     model = Feed
#     ordering = '-pk'


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


class Profile(APIView):
    def get(self, request):
        user = request.user
        feeds = Feed.objects.filter(user_id=user)

        context = {
            'user': user,
            'feeds': feeds,
        }
        return render(request, 'content/profile.html', context)


def new_comment(request, pk):
        feed = get_object_or_404(Feed, pk=pk)

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.feed = feed
                comment.user_id = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else:
            return redirect(feed.get_absolute_url())

