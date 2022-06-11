"""DjangoSNSProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from content import views
from .views import Profile, FeedFavorite, FeedFavoriteList

app_name = 'content'

urlpatterns = [
    #path('<int:pk>/likes/', views.likes, name='likes'),
    path('<int:pk>/new_comment/', views.new_comment),
    path('<int:pk>/',views.FeedDetail.as_view(), name='feed_detail'),
    path('', views.FeedList.as_view()),
    path('create_feed/', views.FeedCreate.as_view()),
    path('profile/', Profile.as_view()),
    path('favorite/<int:feed_id>/', FeedFavorite.as_view(), name='favorite'),
    path('favorite/', FeedFavoriteList.as_view(), name='favorite_list')
]
