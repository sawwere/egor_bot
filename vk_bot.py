
import random, vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType

import re

def load_info(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file]
        token = lines[0]
        group_id = lines[1]
        key = lines
    return token, group_id, key

token, group_id, key = load_info("config.txt")


vk_session = vk_api.VkApi(
    token=token)

longpoll = vk_api.bot_longpoll.VkBotLongPoll(vk_session, group_id)
vk = vk_session.get_api()


def send_message(text):
    vk.messages.send(
        key=key,
        server=('https://lp.vk.com/wh'+group_id),
        ts=('1'),
        random_id=get_random_id(),
        message=text,
        chat_id=event.chat_id)


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        text = event.object['text']
        mes = "Baka"
        try:
            egor_reg = re.compile(re.escape('hippo'), re.IGNORECASE)
            egor_mes = re.sub(
                r"[ЕE][ГгGg][Оо0Oo][РрRrPp]", "*егор", text)
            #print(egor_mes)
        except:
            print('Error unicode')
        if egor_mes != text:
            if event.from_chat:
                send_message(egor_mes)
        if 'Ку' == text or 'Привет' == text or 'Хай' == text or 'Hello' == text or 'Hi' == text:
            if event.from_chat:
                send_message("Привет!")
            


             
'''
for event in Lslongpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        vars1 = ['������', '��', '���', '������']
        if event.text in vars1:
            if event.from_user:
                Lsvk.messages.send(
                    user_id = event.user_id,
                    message = '������)',
                    random_id = get_random_id()
                    )
        vars2 = ['����������', '����������']
        if event.text in vars2:
            if event.from_user:
                Lsvk.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    keyboard = keyboard.get_keyboard(),
                    message = '�����'
                    )
'''


