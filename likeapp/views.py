from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import RedirectView, ListView
from rest_framework.views import APIView

from content.models import Feed
from likeapp.models import LikeRecord


class LikeFeedView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('content:feed_detail', kwargs={'pk': kwargs['pk']})

    def get(self, *args, **kwargs):
        users = self.request.user
        feed = get_object_or_404(Feed, pk=kwargs['pk'])

        if LikeRecord.objects.filter(user=users, feed=feed).exists():
            return HttpResponseRedirect(reverse('content:feed_detail', kwargs={'pk': kwargs['pk']}))
        else:
            LikeRecord(user=users, feed=feed).save()

        feed.like += 1
        feed.save()

        return super(LikeFeedView, self).get(self.request, *args, **kwargs)



