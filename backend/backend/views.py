from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status


import requests
import time
token = '1209437264:AAHJmddIHrGFVtn4fj44lXJ5h_rxMFBANjM'

def get_messages():
    result = requests.get(f'https://api.telegram.org/bot{token}/getUpdates?offset=10').json()
    return result['result'][-1]['message']

def get_json_data():


    name = get_messages()['from']['first_name']
    json_data = {
            "title": name,
            "description": "aa",
            "done": True
            }
    return json_data
        # else:
        #     return None

@api_view(["GET", "POST"])
def show_list(request):

    if (request.method == "GET"):
        time.sleep(1)
        json_data = get_json_data()

        if json_data is not None:
            serializers = TodoSerializer(data=json_data)
            if (serializers.is_valid()):
                serializers.save()

        data = Todo.objects.all()
        serializers = TodoSerializer(data, many=True)
        return Response(serializers.data)

    elif (request.method == "POST"):
        serializers = TodoSerializer(data=request.data)
        if (serializers.is_valid()):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    # update_id = get_messages()[-1]['update_id']
    # print(update_id)
    # time.sleep(1)
    # messages = get_messages() 
    # for message in messages:
    #     print(message['update_id'])
    #     # if update_id < message['update_id']:
    #     update_id = message['update_id']