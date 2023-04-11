from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from django.http import JsonResponse  
import pdfkit
from django.http import HttpResponse
from django.template.loader import get_template


from .serializers import TestUserSerializer
from .models import TestUserModel

# Create your views here.
class HomeView(APIView):  

 def get(self, request, format=None):
    return JsonResponse({"message":
    'HOLA MUNDO DESDE DJANGO, MYSQL Y DOCKER', "content":
    'Por Mario Medina'}) 

class TestUserView(RetrieveAPIView):
   serializer_class = TestUserSerializer
   queryset = TestUserModel.objects.all()

   def get(self, request, id):
      test_user = self.get_queryset().get(pk=id)
      data = self.serializer_class(instance=test_user)                
        
      return Response(data={
         "message":"",
         "content": data.data
      })


class TestUserPdfView(RetrieveAPIView):
   serializer_class = TestUserSerializer
   queryset = TestUserModel.objects.all()

   def get(self, request, id):
      test_user = self.get_queryset().get(pk=id)
      data = self.serializer_class(instance=test_user)                
      template = get_template('test_user.html')
      html = template.render(data.data)
      pdf = pdfkit.from_string(html, False)
      response = HttpResponse(pdf, content_type='application/pdf')
      response['Content-Disposition'] = 'attachment; filename="test_user.pdf"'
      return response

class TestUserList(RetrieveAPIView):
   serializer_class = TestUserSerializer
   queryset = TestUserModel.objects.all()

   def get(self, request):
      test_user = self.get_queryset()
      data = self.serializer_class(instance=test_user, many=True)                
        
      return Response(data={
         "message":"",
         "content": data.data
      })


class TestUserSavePdfView(RetrieveAPIView):
   serializer_class = TestUserSerializer
   queryset = TestUserModel.objects.all()

   def get(self, request, id):
      test_user = self.get_queryset().get(pk=id)
      data = self.serializer_class(instance=test_user)                
      template = get_template('test_user.html')
      html = template.render(data.data)

      pdfkit.from_string(html, 'miapp/static/pdf/test_user.pdf')
      return JsonResponse({"message":
         'PDF Creado', "content":
         'Por Mario Medina'}) 
      
   