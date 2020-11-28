import requests
import time
token = '1209437264:AAHJmddIHrGFVtn4fj44lXJ5h_rxMFBANjM'

def get_messages():
    time.sleep(1)
    result = requests.get(f'https://api.telegram.org/bot{token}/getUpdates?offset=10').json()
    return result['result'][0]['message']

def get_json_data():


    name = get_messages()['from']['first_name']
    # json_data = 
    # {
    #     "profession": "", 
    #     "full_name": name, 
    #     "schedule", 
    #     "employment", 
    #     "education', 
    #     "salary', 
    #     "experience', 
    #     "skills', 
    #     'achievements', 
    #     "expectations",
    #     "add_info", 
    #     "feedback"
    #         }
    # return json_data
    #     else:
    #         return None

# import requests
# import time
# from config import token

# def get_messages():
#     result = requests.get(f'https://api.telegram.org/bot{token}/getUpdates?offset=10').json()
#     return result['result']

# def set_message(chat_id, text):
#     requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

# def check_message(message):
#     if message.lower() in ['привет', 'hello']:
#         return 'Привет :)'
#     else:
#         return 'Я не понимаю('

# def run():
#     update_id = get_messages()[-1]['update_id']
#     while True:
#         time.sleep(1)
#         messages = get_messages() 
#         for message in messages:
#             if update_id < message['update_id']:
#                 update_id = message['update_id']
#                 print(get_messages()[0]['message']['from']['first_name'])
#                 set_message(message['message']['chat']['id'], check_message(message['message']['text']))

# if __name__ == '__main__':
#     run()
