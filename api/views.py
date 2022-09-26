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

class ApiTest(APIView):
	def get(self,request):
		return Response({"okokokokok"})

	def post(self,request):
		print("DASDsadsasadad",request.data)
		return Response(request.data,status=status.HTTP_201_CREATED)

@api_view(http_method_names=['GET','POST'])
def api_test(request):
    return Response({"message":"okokok"})



class ApiContent(ListAPIView):
	queryset = Content.objects.using("mrplatofixed").all()
	serializer_class = ContentSerializer



class ApiNotification(ListAPIView):
	queryset = Notification.objects.using("mrplatofixed").all()
	serializer_class = NotificationSerializer
