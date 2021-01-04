'''
***** Replace Last *** (Elementary) *****

***(EN)***

In a given list the last element should become the first one.
An empty list or list with only one element should stay the same example

Input: List.

Output: Iterable.

Example:

	replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
	replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
	replace_last([1]) == [1]
	replace_last([]) == []


***(RU)***

В предлагаемом список последний элемент должен стать первым.
Пустой список или список с одним элементом должен остаться тем же

Принимает: Список.

Возвращает: Итерируемый объект.

Пример:

	replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
	replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
	replace_last([1]) == [1]
	replace_last([]) == []

'''


from typing import Iterable


def replace_last(items: list) -> Iterable:
	return [line.pop()] + line if len(line) > 1 else line  # моё решение
    # return items[-1:] + items[:-1]  # more better (так лучше)


if __name__ == '__main__':
    print("Example:")
    print(list(replace_last([2, 3, 4, 1])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_last([2, 3, 4, 1])) == [1, 2, 3, 4]
    assert list(replace_last([1])) == [1]
    assert list(replace_last([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
