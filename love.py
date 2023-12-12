import random
import time
import schedule
from twilio.rest import Client
import os

sweet_names = ['Adorable', 'Angel', 'Angelica', 'Autumn', 'Baby', 'Beauty', 'Berry', 'Bubbles', 'Butterfly', 'Cherry', 'Cookie', 'Cuddlebug', 'Cupid', 'Cupcake', 'Daisy', 'Darling', 'Dove', 'Elf', 'Fairy', 'Heart', 'Jasmine', 'Janea-bug', 'Joy', 'Lily', 'Lollipop', 'Love', 'Lovely', 'Marshmallow', 'Melody', 'Mermaid', 'Moonbeam', 'Peaches', 'Peachy', 'Precious', 'Princess', 'Puddin', 'Rhapsody', 'Rose', 'Serenade', 'Snickerdoodle', 'Snowflake', 'Spring', 'Star', 'Summer', 'Sunshine', 'Symphony', 'Sweetie', 'Symphony', 'Treasure', 'Unicorn', 'Violet', 'Winter', 'Waifu']
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)
twilio_phone_number = ''
recipient_phone_number = ''



def send_message_twilio(account_sid, auth_token, twilio_phone_number, recipient_phone_number, message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=recipient_phone_number,
        from_=twilio_phone_number,
        body=message)

def Loveyou():
    select_love = random.randint(0, 50)
    message = "I love you my " + sweet_names[select_love]
    send_message_twilio(account_sid,auth_token,twilio_phone_number,recipient_phone_number,message)
    print(message)



def goodmorning():
    select_love = random.randint(0, 50)
    message = 'Good Morning my' + sweet_names[select_love]
    send_message_twilio(account_sid,auth_token,twilio_phone_number,recipient_phone_number,message)
    print(message)


def goodnight():
    select_love = random.randint(0, 50)
    message = 'Good Night my' + sweet_names[select_love]
    send_message_twilio(account_sid,auth_token,twilio_phone_number,recipient_phone_number,message)
    print(message)



schedule.every().day.at('08:00').do(goodmorning)
schedule.every().day.at('08:00').do(Loveyou)
schedule.every().day.at('17:33').do(Loveyou)
schedule.every().day.at('21:45').do(goodnight)


while True:
    schedule.run_pending()
    time.sleep(1)
    print('waiting..')





