# Напишите декоратор obfuscator


def obfuscator(func):
    def wrapper():
        res = func()
        value = res['name']
        res['name'] = value[0] + '*' * (len(value) - 2) + value[-1]
        value = res['password']
        res['password'] = value = '*' * len(value)
        return res
    return wrapper

@obfuscator
def get_credentials():
    return {
        'name': 'StasBasov',
        'password': 'iamthebest'
    }


print(get_credentials())