from django.urls import path

from likeapp.views import LikeFeedView

app_name = 'likeapp'

urlpatterns = [
    path('main/like/<int:pk>/', LikeFeedView.as_view(), name='feed_like'),

]
