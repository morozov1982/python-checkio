"""
***** Time Converter (24h to 12h) *** (Simple) *****

***(EN)***

You prefer a good old 12-hour time format.
But the modern world we live in would rather use the 24-hour format and you see it everywhere.
Your task is to convert the time from the 24-h format into 12-h format by following the next rules:
    - the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday)
    - if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'
Here you can find some useful information about the 12-hour format.

Input: Time in a 24-hour format (as a string).

Output: Time in a 12-hour format (as a string).

Example:
    1. time_converter('12:30') == '12:30 p.m.'
    2. time_converter('09:00') == '9:00 a.m.'
    3. time_converter('23:15') == '11:15 p.m.'

How it is used: For work with the different time formats.

Precondition:
    '00:00' <= time <= '23:59'


***(RU)***

Вы предпочитаете использовать 12-часовой формат времени,
но современный мир живет в 24-часовом формате и вы видите это повсюду.
Ваша задача - переконвертировать время из 24-часового формата в 12-часовой, использкя следующие правила:
    - выходной формат должен быть 'чч:мм a.m.' (для часов до полудня) или 'чч:мм p.m.' (для часов после полудня)
    - если часы меньше 10 - не пишите '0' перед ними. Например: '9:05 a.m.'
Вы можете узнать больше подробностей о 12-часовом формате.

Входные данные: Время в 24-часовом формате (как строка).

Выходные данные: Время в 12-часовом формате (как строка).

Примеры:
    1. time_converter('12:30') == '12:30 p.m.'
    2. time_converter('09:00') == '9:00 a.m.'
    3. time_converter('23:15') == '11:15 p.m.'

Как это используется: Для работы с разными форматами времени.

Предусловия:
    '00:00' <= время <= '23:59'

"""


def time_converter(time):
    hours, minutes = time.split(':')
    time = f'{(int(hours) - 1) % 12 + 1}:{minutes} {"p.m." if (int(hours) // 12) else "a.m."}'
    return time


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
