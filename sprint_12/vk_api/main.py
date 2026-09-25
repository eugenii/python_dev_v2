import requests

# Указываем актуальную версию VK API
API_VERSION = "5.199"
# Вставьте сервисный ключ приложения
SERVICE_TOKEN = "07e66a5b07e66a5b07e66a5bdc04a59703007e607e66a5b6d52b3fc39c6a67253cb9693" 

# Создаём функцию, которая будет отправлять
# запросы по адресу https://api.vk.com/method/{method} 
def vk_call(method, params):
    url = f"https://api.vk.com/method/{method}"
    params |= {
        "access_token": SERVICE_TOKEN,
        "v": API_VERSION,
    }
    response = requests.get(url, params=params, timeout=10)
    
    # Парсим JSON с ответом
    data = response.json()
    if "error" in data:
        raise RuntimeError(f"VK API error: {data['error']}")
    return data["response"]

# Вызываем функцию с дополнительными параметрами
response = vk_call(
    method="groups.getById",
    params={
        "group_id": "yandex.practicum",
        "fields": "description"
    }
)
print(response)