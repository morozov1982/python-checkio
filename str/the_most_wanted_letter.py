'''
***** Pawn Brotherhood *** (Simple) *****

***(EN)***

You are given a text, which contains different English letters and punctuation symbols.
You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a".
Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

If you have two or more letters with the same frequency,
then return the letter which comes first in the Latin alphabet.
For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string.

Output: The most frequent letter in lower case as a string.

Example:
    1 checkio("Hello World!") == "l"
    2 checkio("How do you do?") == "o"
    3 checkio("One") == "e"
    4 checkio("Oops!") == "o"
    5 checkio("AAaooo!!!!") == "a"
    6 checkio("abe") == "a"

How it is used:
For most decryption tasks you need to know the frequency of occurrence for various letters in a section of text.
For example:
we can easily crack a simple addition or substitution cipher if we know the frequency in which letters appear.
This is interesting stuff for language experts!

Precondition:
    A text contains only ASCII symbols.
    0 < len(text) ≤ 105


***(RU)***

Дан текст, который содержит различные английские буквы и знаки препинания.
Вам необходимо найти самую частую букву в тексте. Результатом должна быть буква в нижнем регистре.
При поиске самой частой буквы, регистр не имеет значения, так что при подсчете считайте, что "A" == "a".
Убедитесь, что вы не считайте знаки препинания, цифры и пробелы, а только буквы.

Если в тексте две и больше буквы с одинаковой частотой, тогда результатом будет буква, которая идет первой в алфавите.
Для примера, "one" содержит "o", "n", "e" по одному разу, так что мы выбираем "e".

Вх. данные: Текст для анализа, как строка.

Вых. данные: Наиболее частая буква, как строка.

Примеры:
    1 checkio("Hello World!") == "l"
    2 checkio("How do you do?") == "o"
    3 checkio("One") == "e"
    4 checkio("Oops!") == "o"
    5 checkio("AAaooo!!!!") == "a"
    6 checkio("abe") == "a"

Как это используется:
Для большинства задач по дешифрованию необходимо знать частоту появления различных букв в подобном тексте.
Для примера, мы легко можем взломать одноалфавитный шифр подстановки, если мы знаем вероятность появления букв.
Это также может быть полезной информацией для лингвистов.

Предусловия:
    text содержит только ASCII символы.
    0 < len(text) ≤ 105

'''


# моё решение
def checkio(text: str) -> str:
    count_dict = {}
    for letter in text.lower():
        if letter.isalpha() and letter not in count_dict:
            count_dict[letter] = text.lower().count(letter)
    sorted_list = sorted(sorted(count_dict.items()), key = lambda x: x[1], reverse=True)
    return sorted_list[0][0]


# понравилось решение
def checkio1(text):
    l = [a for a in text.lower() if a.isalpha()]
    return max(sorted(l), key=l.count)


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
