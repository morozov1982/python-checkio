'''
***** Morse Decoder *** (Elementary+) *****

***(EN)***

Your task is to decrypt the secret message using the Morse code.
(https://en.wikipedia.org/wiki/Morse_code)
The message will consist of words with 3 spaces between them and 1 space between each letter of each word.
If the decrypted text starts with a letter then you'll have to print this letter in uppercase.

Input: The secret message.

Output: The decrypted text.

Example:
    1. morse_decoder("... --- -- .   - . -..- -") == "Some text"
    2. morse_decoder("..--- ----- .---- ---..") == "2018"
    3. morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"

How it is used: For cryptography and spy work.

Precondition:
0 < len(message) < 100
The message will consists of numbers and English letters only.


***(RU)***

Ваша задача - расшифровать сообщение используя азбуку Морзе.
(https://ru.wikipedia.org/wiki/%D0%90%D0%B7%D0%B1%D1%83%D0%BA%D0%B0_%D0%9C%D0%BE%D1%80%D0%B7%D0%B5)
В шифровке будет использован 1 пробел между буквами одого слова и 3 пробела между отдельными словами.
Если расшифрованный текст начинается со слова, первая буква этого слова должна быть заглавной.

Входные данные: Секретное сообщение

Выходные данные: Расшифрованный текст

Примеры:
    1. morse_decoder("... --- -- .   - . -..- -") == "Some text"
    2. morse_decoder("..--- ----- .---- ---..") == "2018"
    3. morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"

Как это используется: Для криптографии, передачи и защиты важной информации.

Предусловия:
0 < len(message) < 100
Текст будет состоять только из цифр и букв английского алфавита.

'''

from re import sub

MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
         }


# Не удержался, регулярочки ;-) работает медленнее, чем morse_decoder()
def morse_decoder_1(code):
    return sub(r'[-|.]+', lambda l: MORSE.get(l.group(0)), code + '\n')[::2].capitalize()


# Решение в одну строку, как я люблю ;-)
def morse_decoder(code):
    return ''.join([MORSE.get(let) if let in MORSE else ' ' for let in code.split(' ')]).replace('  ', ' ').capitalize()


# Первое решение
def morse_decoder_old(code):
    decoded = ''
    words_list = code.split('   ')
    for w_idx, word in enumerate(words_list):
        words_list[w_idx] = word.split(' ')
        for letter in words_list[w_idx]:
            decoded += MORSE.get(letter)
        decoded += ' '

    return decoded.strip().capitalize()


if __name__ == '__main__':
    print("Example:")
    print(morse_decoder('... --- ...'))
    print(morse_decoder("... --- -- .   - . -..- -"))
    print(morse_decoder("..--- ----- .---- ---.."))
    print(morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert morse_decoder("..--- ----- .---- ---..") == "2018"
    assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"
    print("Coding complete? Click 'Check' to earn cool rewards!")
