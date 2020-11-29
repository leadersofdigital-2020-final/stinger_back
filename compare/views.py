from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Compare
from .serializers import CompareSerializer
from rest_framework.response import Response
from rest_framework import status
import requests

@api_view(["GET", "POST"])
def show_list(request):

    if (request.method == "GET"):

        # if get_interview() is not None:
        #     print(get_interview())


        data = Compare.objects.all()
        get_serializers = CompareSerializer(data, many=True)

        cv = requests.get('http://127.0.0.1:8000/cv/?format=json').json()
        vacancy = requests.get('http://127.0.0.1:8000/vacancy/?format=json').json()

        cv = cv[-1]
        vacancy = vacancy[-1]

        data = {
            "id": 1,
            "full_name": "Ивин П.А.",
            "profession": "Senior Python Developer",
            "image": "https://img2.freepng.ru/20180622/pol/kisspng-man-male-facial-hair-dentistry-freud-5b2d6781f36fd2.3821397415297022739971.jpg",
            "video": "http://s35.savefrom.net/media/3382868757/9ed67c4dfcd7d327175f2df6cf1005ae/Sergueї+Panarine.mp4",
            "stage": cv["stage"]/vacancy["stage"],
            "schedule": cv["schedule"]/vacancy["schedule"],
            "employment": "flex",
            "education": "master",
            "salary": cv["salary"]/vacancy["salary"],
            "experience": cv["experience"]/vacancy["experience"],
            "skills": "Python, matplotlib, pandas",
            "achievements": "text",
            "expectations": "text",
            "add_info": "text",
            "feedback": "text",
            "date": "2020-11-28T23:58:35.760268Z",
            "phone": "+7 903 228 65 68",
            "rating": data["stage"] + data["schedule"] + data["salary"] + data["experience"]
        }


        

        if get_serializers.data[-1]['date'] < data['date']:
            post_serializers = CompareSerializer(data=data)
            if (post_serializers.is_valid()):
                post_serializers.save()
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
