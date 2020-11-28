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
        "id": 8,
        "full_name": "Ивин П.А.",
        "profession": "программист Python",
        "image": "https://img2.freepng.ru/20180622/pol/kisspng-man-male-facial-hair-dentistry-freud-5b2d6781f36fd2.3821397415297022739971.jpg",
        "video": "http://s35.savefrom.net/media/3382868757/9ed67c4dfcd7d327175f2df6cf1005ae/Sergueї+Panarine.mp4",
        "stage": 3,
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
        "date": "2020-11-28T09:59:22.420915Z",
        "cellNumber": "+7 903 228 65 68",
        "rating":4
    }

        # if get_interview() is not None:
        #     print(get_interview())


        data = CV.objects.all()
        get_serializers = CVSerializer(data, many=True)

        # if get_serializers.data[-1]['date'] < json_data['date']:
        #     post_serializers = CVSerializer(data=json_data)
        #     if (post_serializers.is_valid()):
        #         post_serializers.save()
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
