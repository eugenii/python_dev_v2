class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


    def process_text(self, text, shift, is_encrypt):
        if shift > len(self.alphabet):
            shift = shift % len(self.alphabet)
        if not is_encrypt:
            shift = -shift
        result = []
        for letter in text:
            if letter.lower() in self.alphabet:
                idx = (str.index(self.alphabet, letter.lower()) + shift) % len(self.alphabet)
                letter = self.alphabet[idx]
            result.append(letter)
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
)) 