import random

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from vk_bot import TOKEN

vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, "199503937")

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        print('Новое сообщение:')
        print('Для меня от: ', end='')
        print(event.obj.from_id)
        print('Текст:', event.obj.text)
        print()
        vk.messages.send(user_id=event.obj.from_id, message=event.obj.text, random_id=random.random())
    elif event.type == VkBotEventType.MESSAGE_REPLY:
        print('Новое сообщение:')
        print('От меня для: ', end='')
        print(event.obj.peer_id)
        print('Текст:', event.obj.text)
        print()
