import random
import requests

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from googletrans import Translator

from vk_bot import TOKEN, GROUP_ID, WEATHER

vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, group_id=GROUP_ID)

translator = Translator()


def translate(api, update):
    message = update.message.text.removeprefix("/translate ")
    result = translator.translate(message, dest="ru")
    api.messages.send(user_id=update.message.from_id,
                      message=result.text,
                      random_id=random.random())


def weather(api, update):
    city = update.message.text.removeprefix("/weather ")
    data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}"
                        f"&appid={WEATHER}"
                        f"&units=metric"
                        f"&lang=ru").json()
    result = f"Сейчас {data['weather'][0]['description']}, " \
             f"температура {data['main']['temp']}°С, " \
             f"ощущается как {data['main']['feels_like']}°С."
    api.messages.send(user_id=update.message.from_id,
                      message=result,
                      random_id=random.random())


def echo(api, update):
    api.messages.send(user_id=update.message.from_id,
                      message=update.message.text,
                      random_id=random.random())


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.message.text.startswith("/translate"):
            translate(vk, event)
        elif event.message.text.startswith("/weather"):
            weather(vk, event)
        else:
            echo(vk, event)
