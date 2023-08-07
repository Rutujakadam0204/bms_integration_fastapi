import requests
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.serializers import serialize
import json
from . models import Invoice

# Create your views here.
class Okk(APIView):
    def get(self, request):
        print("ok")
        user = User.objects.all()
        user = serialize('json', user)
        user = json.loads(user)
        data = user
        return Response(data)

    def post(self, request):
        print(request.data)
        Invoice.objects.create(name=request.data['name'], date=request.data['date'])
        message = {'message':"done"}
        return Response(message)