from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView, DetailView

from rest_framework.views import APIView


from .forms import CommentForm
from .models import Feed, Comment



class FeedList(ListView):
    model = Feed
    ordering = '-pk'


class FeedDetail(DetailView):
    model = Feed

    def get_context_data(self, **kwargs):
        context = super(FeedDetail, self).get_context_data()
        context['comment_form'] = CommentForm
        return context





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



class FeedFavorite(View):


    def get(self, request, *args, **kwargs):
        if 'feed_id' in kwargs:
            feed_id = kwargs['feed_id']
            feed= Feed.objects.get(pk=feed_id)
            user = request.user
            if user in feed.favorite.all():
                feed.favorite.remove(user)
            else:
                feed.favorite.add(user)
        return HttpResponseRedirect('/main/favorite/')

class FeedFavoriteList(ListView):
    model = Feed
    template_name = 'content/favorite_list.html'

    def dispatch(self, request, *args, **kwargs):
        return super(FeedFavoriteList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        queryset = user.favorite_feed.all()
        return queryset
