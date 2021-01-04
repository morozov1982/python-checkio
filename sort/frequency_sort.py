"""
***** Frequency Sorting *** (Elementary+) *****

***(EN)***

Your mission is to sort the list by the frequency of numbers included in it.
If a few numbers have an equal frequency - they should be sorted according to their natural order.
For example: [5, 2, 4, 1, 1, 1, 3] ==> [1, 1, 1, 2, 3, 4, 5]

Input: Chaotic list of numbers.
Output: The list of numbers in which they are sorted by their frequency.

Example:
    1 frequency_sorting([5, 3, 8, 11, 5, 6, 6, 5]) == [5, 5, 5, 6, 6, 3, 8, 11]

How it is used: For analyzing data using mathematical statistics and mathematical analysis,
and for finding trends and predicting future changes (systems, phenomena, etc.)


***(RU)***

Ваше задание - пересортировать список, расположив числа в порядке уменьшения их количества в списке.
Если несколько чисел встречаются одинаково часто - их необходимо расположить в порядке от меньшего к большему,
вне зависимости от того, в каком порядке они встречаются в исходном списке.
Например: [5, 2, 4, 1, 1, 1, 3] ==> [1, 1, 1, 2, 3, 4, 5]

Входные данные: Хаотичный набор чисел.
Выходные данные: Список, отсортированный в зависимости от количества каждого числа в списке.

Пример:
    1 frequency_sorting([5, 3, 8, 11, 5, 6, 6, 5]) == [5, 5, 5, 6, 6, 3, 8, 11]

Как это используется:
Для анализа данных с помощью математической статистики и мат.анализа,
а также для нахождения тенденций и предсказания будущих изменений (систем, явлений и т.д.)

"""


def frequency_sorting(numbers):
    return sorted(sorted(numbers), key=lambda x: numbers.count(x), reverse=True)


if __name__ == '__main__':
    print("Example:")
    print(frequency_sorting([1, 2, 3, 4, 5]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert frequency_sorting([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Already sorted"
    assert frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]) == [4, 4, 4, 3, 3, 11, 11, 7, 13], "Not sorted"
    assert frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10]) == [10, 10, 21, 21, 55, 55, 99, 99], "Reversed"
    print("Coding complete? Click 'Check' to earn cool rewards!")
