from django.urls import path

from user.views import Join, Login

urlpatterns = [
    path('', Login.as_view()),
    path('join/', Join.as_view()),
]
