from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import CV
from .serializers import CVSerializer
from rest_framework.response import Response
from rest_framework import status
from .bot import get_interview

@api_view(["GET", "POST"])
def show_list(request):

    if (request.method == "GET"):
        json_data = {
        "id": 1,
        "profession": "программист Python",
        "full_name": "Ивин П.А.",
        "schedule": "40",
        "employment": "flex",
        "education": "bachelor",
        "salary": "30 000",
        "experience": 1,
        "skills": "Python, matplotlib, pandas",
        "achievements": "text",
        "expectations": "text",
        "add_info": "text",
        "feedback": "text",
        "date": "2020-11-28T09:23:48.076327Z"
    }

        # if get_interview() is not None:
        #     print(get_interview())


        data = CV.objects.all()
        get_serializers = CVSerializer(data, many=True)
        print()
        if get_serializers.data[-1]['date'] < json_data['date']:
            post_serializers = CVSerializer(data=json_data)
            if (post_serializers.is_valid()):
                post_serializers.save()
        return Response(get_serializers.data)

    elif (request.method == "POST"):
        serializers = CVSerializer(data=request.data)
        if (serializers.is_valid()):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        operation = CV.delete()
        if operation:
            data["success"] = "delete succesful"
        else:
            data["failure"] = "delete failure"
        data = {}
        return Response(data=data)
