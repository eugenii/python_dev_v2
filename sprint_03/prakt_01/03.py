class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    LEN = len(alphabet)

    def cipher(self, original_text, shift):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        
        if shift > self.LEN:
            shift = shift % self.LEN
        result = []
        for letter in original_text:
            if letter.lower() in self.alphabet:
                idx = (str.index(self.alphabet, letter.lower()) + shift) % self.LEN
                letter = self.alphabet[idx]
            result.append(letter)
        return ''.join(result)

    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        if shift > self.LEN:
            shift = shift % self.LEN
        result = []
        for letter in cipher_text:
            if letter.lower() in self.alphabet:
                idx = (str.index(self.alphabet, letter.lower()) + shift) % self.LEN
                letter = self.alphabet[idx]
            result.append(letter)
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))