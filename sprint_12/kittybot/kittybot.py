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


def handle_start(user_id):
    vk.messages.send(
        user_id=user_id,
        message="Спасибо, что включили меня",
        random_id=random.randint(0, 100000)
    )

def handle_text(user_id):
    vk.messages.send(
        user_id=user_id,
        message="Привет, я KittyBot!",
        random_id=random.randint(0, 100000)
    )

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        message = event.object.message
        user_id = message['from_id']

        # Проверим, есть ли текст в сообщении
        text = message.get('text', '').strip().lower()
        if text:  # Если текст не пустой
            if text == 'начать':
                handle_start(user_id)
            else:
                handle_text(user_id)
        # На вложения бот по-прежнему не реагирует 