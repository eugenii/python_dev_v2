# Шифрованные ссылки.
import random


class MarsURLEncoder:

    SET_OF_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    SET_OF_CHARS_LEN = 7

    def __init__(self):
        self.__hash_dict = {}

    def encode(self, long_url: str) -> str:
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        hash = ''.join(random.choice(self.SET_OF_CHARS) for _ in range(self.SET_OF_CHARS_LEN))
        while hash in self.__hash_dict:
            hash = ''.join(random.choice(self.SET_OF_CHARS) for _ in range(self.SET_OF_CHARS_LEN))
        self.__hash_dict[hash] = long_url
        return 'https://ma.rs/' + hash

    def decode(self, short_url: str) -> str:
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        return self.__hash_dict[short_url[14:]]
    

coder = MarsURLEncoder()

long_url = "http://ph-k210.ucoz.ru"
shirt_url = coder.encode(long_url)
print(shirt_url)
print(coder.decode(shirt_url))