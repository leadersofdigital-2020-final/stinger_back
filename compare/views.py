from django.shortcuts import render

from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Compare
from .serializers import CompareSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET", "POST"])
def show_list(request):

    if (request.method == "GET"):

        # if get_interview() is not None:
        #     print(get_interview())


        data = Compare.objects.all()
        get_serializers = CompareSerializer(data, many=True)


        import requests

        result = requests.get('http://127.0.0.1:8000/cv/?format=json')
        

        # if get_serializers.data[-1]['date'] < json_data['date']:
        #     post_serializers = CompareSerializer(data=json_data)
        #     if (post_serializers.is_valid()):
        #         post_serializers.save()
        return Response(get_serializers.data)

    elif (request.method == "POST"):
        serializers = CompareSerializer(data=request.data)
        if (serializers.is_valid()):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        operation = Compare.delete()
        if operation:
            data["success"] = "delete succesful"
        else:
            data["failure"] = "delete failure"
        data = {}
        return Response(data=data)
