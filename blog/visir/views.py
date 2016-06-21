from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Data
from .serializers import DataSerializer

# Create your views here.
class DataList(APIView):

	def get(self, request):
		datas = Data.objects.all()
		serializer = DataSerializer(datas, many = True)
		return Response(serializer.data)

	def post(self):
		pass
