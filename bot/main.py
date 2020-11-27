import requests
import time
from config import token

def get_messages():
    result = requests.get(f'https://api.telegram.org/bot{token}/getUpdates?offset=10').json()
    return result['result']

def set_message(chat_id, text):
    requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

def check_message(message):
    if message.lower() in ['привет', 'hello']:
        return 'Привет :)'
    else:
        return 'Я не понимаю('

def run():
    update_id = get_messages()[-1]['update_id']
    while True:
        time.sleep(1)
        messages = get_messages() 
        for message in messages:
            if update_id < message['update_id']:
                update_id = message['update_id']
                print(get_messages()[0]['message']['from']['first_name'])
                set_message(message['message']['chat']['id'], check_message(message['message']['text']))

if __name__ == '__main__':
    run()

