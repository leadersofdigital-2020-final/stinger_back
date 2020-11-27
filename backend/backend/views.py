from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET", "POST"])
def show_list(request):
    if (request.method=="GET"):
        data=Todo.objects.all()
        serializers = TodoSerializer(data, many=True)
        return Response(serializers.data)
    elif (request.method=="POST"):
        serializers = TodoSerializer(data=request.data)
        if (serializers.is_valid()):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)