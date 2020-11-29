from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Vacancy
from .serializers import VacancySerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET", "POST"])
def show_list(request):

    if (request.method == "GET"):
        data = Vacancy.objects.all()
        get_serializers = VacancySerializer(data, many=True)
        json_data = {
            
        "profession": "Senior Python Developer",
        "schedule": 40,
        "employment": "flex",
        "education": "master",
        "salary": 200000,
        "experience": 5,
        "skills": "Python, matplotlib, pandas",
        "achievements": "text",
        "expectations": "text",
        "add_info": "text",
        "feedback": "text"
}

        # if get_serializers.data[-1]['date'] < json_data['date']:
        post_serializers = VacancySerializer(data=json_data)
        if (post_serializers.is_valid()):
            post_serializers.save()
        get_serializers = VacancySerializer(data, many=True)
        return Response(get_serializers.data)

    elif (request.method == "POST"):
        serializers = VacancySerializer(data=request.data)
        if (serializers.is_valid()):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        operation = Vacancy.delete()
        if operation:
            data["success"] = "delete succesful"
        else:
            data["failure"] = "delete failure"
        data = {}
        return Response(data=data)