# from django.contrib.auth.hashers import make_password
# from django.shortcuts import render
#
# # Create your views here.
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import User
#
# class Join(APIView):
#     def get(self,request):
#         return render(request, 'user/join.html')
#
#     def post(self, request):
#         email = request.data.get('email', None)
#         nickname = request.data.get('nickname', None)
#         name = request.data.get('name', None)
#         password = request.data.get('password', None)
#
#         User.objects.create(email=email,
#                             nickname=nickname,
#                             name=name,
#                             password=make_password(password),
#                             porfile_image="default_profile.jpg")
#
#         return Response(status=200)
#
# class Login(APIView):
#     def get(self,request):
#         return render(request, 'user/login.html')