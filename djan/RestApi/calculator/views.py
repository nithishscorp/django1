# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import calc
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.
class cal(APIView):
    permission_classes= [IsAuthenticated]
    authentication_classes=(TokenAuthentication,)
    def get(self,request,num1,num2):
        try:
            num1=int(num1)
            num2=int(num2)
        except ValueError:
            return Response(status.HTTP_400_BAD_REQUEST)    
        try:
            p=calc.objects.get(operator="+",n1=num1,n2=num2)
            return Response("from database %s" % p.total)
        except calc.DoesNotExist:    
            p=calc(operator='+',n1=num1,n2=num2,total=num1+num2)
            p.save()
        sum=num1+num2
        return Response(sum)

    def put(self,request,num1,num2):
        num1=int(num1)
        num2=int(num2)
        try:
            p=calc.objects.get(operator="-",n1=num1,n2=num2)
            return Response("from database %s" % p.total)
        except calc.DoesNotExist:    
            p=calc(operator='-',n1=num1,n2=num2,total=num1-num2)
            p.save()
        sub=num1-num2
        return Response(sub)

    def post(self,request,num1,num2):
        num1=int(num1)
        num2=int(num2)
        try:
            p=calc.objects.get(operator="*",n1=num1,n2=num2)
            return Response("from database %s" % p.total)
        except calc.DoesNotExist:    
            p=calc(operator='*',n1=num1,n2=num2,total=num1*num2)
            p.save()
        mul=num1*num2
        return Response(mul)

    def delete(self,request,num1,num2):
        num1=int(num1)
        num2=int(num2)
        try:
            p=calc.objects.get(operator="/",n1=num1,n2=num2)
            return Response("from database %s" % p.total)
        except calc.DoesNotExist:    
            p=calc(operator='/',n1=num1,n2=num2,total=num1/num2)
            p.save()
        div=num1/num2
        return Response(div)    