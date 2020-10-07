'''
***** Sort Array by Element Frequency *** (Elementary+) *****

***(EN)***

Sort the given iterable so that its elements end up in the decreasing frequency order,
that is, the number of times they appear in elements.
If two elements have the same frequency,
they should end up in the same order as the first appearance in the iterable.

Input: Iterable

Output: Iterable

Example:

	1. frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
	2. frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']

Precondition: elements can be ints or strings

The mission was taken from Python CCPS 109 Fall 2018.
It's being taught for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen
(http://www.scs.ryerson.ca/~ikokkari/)


***(RU)***

Отсортируйте данный итератор таким образом,
чтобы его элементы оказались в порядке убывания частоты их появления,
то есть по количеству раз, которое они появляются в элементах.
Если два элемента имеют одинаковую частоту, они должны оказаться в том же порядке,
в котором стояли изначально в итераторе.

Входные данные: Итератор

Выходные данные: Итератор

Пример:

	1. frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
	2. frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']

Предварительное условие: Элементы могут быть целыми числами или строками.

Миссия была взята из Python CCPS 109 Осень 2018.
Она преподается Илккой Коккариненым в Школа непрерывного образования Раймонда Чанга.

'''


def frequency_sort(items):
	idx_sort = sorted(items, key=lambda x: items.index(x))
    res = sorted(idx_sort, key=lambda x: items.count(x), reverse = True)
    return res

    # return sorted(items, key=lambda x: (items.count(x), -items.index(x)), reverse=True)  # I like it (не мой но прекрасный вариант)

if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
