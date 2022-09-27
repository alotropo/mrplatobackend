from urllib import response
from django.shortcuts import render
from api.serializers import ContentSerializer,NotificationSerializer
from content.models import Content
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status
from notification.models import Notification
import json
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response
from rest_framework import status

class ApiTest(APIView):
	def get(self,request):
		return Response({"okokokokok"})

	def post(self,request):
		print("DASDsadsasadad",request.data)
		return Response(request.data,status=status.HTTP_201_CREATED)

@api_view(http_method_names=['GET','POST'])
def api_test(request):
    return Response({"message":"okokok"})



class ApiContent(ModelViewSet):
	queryset = Content.objects.using("mrplatofixed").all()
	serializer_class = ContentSerializer

	def create(self, request, *args, **kwargs):
		return Response("Unauthorized",status=status.HTTP_401_UNAUTHORIZED)

	def destroy(self, request, *args, **kwargs):
		return Response("Unauthorized",status=status.HTTP_401_UNAUTHORIZED)

	def update(self, request, *args, **kwargs):
		return Response("Unauthorized",status=status.HTTP_401_UNAUTHORIZED)


class ApiNotification(ListAPIView):
	queryset = Notification.objects.using("mrplatofixed").all()
	serializer_class = NotificationSerializer


