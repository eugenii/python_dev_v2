# kittybot/kittybot.py

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

import random

# Укажите токен,
# который вы получили при создании сообщества:
TOKEN = 'vk1.a.D-qbLuWvKtzamBWd7rAffOqnA-1akydXDmb9BPq9ICz-O58Nsz-ksIHXXPkN3SGLXVwr1SCXGLevMN8DtVcYvp8KgRexKcY3nECETx04Q4fRqTGemD4uhPpd3KXNFnBtUZq1SNB3RftV2t8i6tI_UtDXnbwn2ge8PlzTcFOOPQcT7ZG_wVXU2g6P4lzOqNlcYp0DxpCw6b7bj7MTSJU3Xg'

# Авторизация: начинаем сессию
vk_session = vk_api.VkApi(token=TOKEN)
# Получаем доступ к методам API
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, '241710901')

# Укажите id своего профиля ВКонтакте:
user_id = "255160700"

message = 'Вам телеграмма! (с посылкой)'
# Вызываем метод vk.messages.send, с помощью которого отправляются сообщения:
vk.messages.send(
    user_id=user_id,
    message=message,
    random_id=random.randint(0, 100000)
    # random_id нужен для предотвращения дублирования сообщений
)


def get_user_name(vk, user_id):
    user_info = vk.users.get(user_ids=user_id)[0]
    return user_info['first_name']

def handle_start(vk, message):
    user_id = message['from_id']
    name = get_user_name(vk, user_id)
    vk.messages.send(
        user_id=user_id,
        message=f"Спасибо, что включили меня, {name}",
        random_id=random.randint(0, 100000)
    )

def handle_text(vk, message):
    user_id = message['from_id']
    vk.messages.send(
        user_id=user_id,
        message="Привет, я KittyBot!",
        random_id=random.randint(0, 100000)
    )

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        message = event.object.message
        text = message.get('text', '').strip().lower()
        if text:
            if text == 'начать':
                handle_start(vk, message)
            else:
                handle_text(vk, message) 