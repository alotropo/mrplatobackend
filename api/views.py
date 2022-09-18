from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response

from rest_framework import status

import json

class ApiTest(APIView):
	def get(self,request):
		return Response({"okokokokok"})

	def post(self,request):
		print("DASDsadsasadad",request.data)
		return Response(request.data,status=status.HTTP_201_CREATED)

@api_view(http_method_names=['GET','POST'])
def api_test(request):
    return Response({"message":"okokok"})