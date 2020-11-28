from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import CV
from .serializers import CVSerializer
from rest_framework.response import Response
from rest_framework import status
from .get import get_json_data


@api_view(["GET", "POST"])
def show_list(request):

    if (request.method == "GET"):
        json_data = None

        # if json_data is not None:
        #     serializers = CVSerializer(data=json_data)
        #     if (serializers.is_valid()):
        #         serializers.save()


        data = CV.objects.all()
        serializers = CVSerializer(data, many=True)
        print(serializers.data)
        return Response(serializers.data)

    elif (request.method == "POST"):
        serializers = CVSerializer(data=request.data)
        if (serializers.is_valid()):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

