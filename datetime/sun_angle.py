'''
***** Sun Angle *** (Simple) *****

***(EN)***

Every true traveler must know how to do 3 things:
fix the fire, find the water and extract useful information from the nature around him.
Programming won't help you with the fire and water,
but when it comes to the information extraction - it might be just the thing you need.

Your task is to find the angle of the sun above the horizon knowing the time of the day.
Input data: the sun rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees.
At 12:00 PM the sun reaches its zenith, which means that the angle equals 90 degrees.
6:00 PM is the time of the sunset so the angle is 180 degrees.
If the input will be the time of the night (before 6:00 AM or after 6:00 PM),
your function should return - "I don't see the sun!".

Input: The time of the day.

Output: The angle of the sun, rounded to 2 decimal places.

Example:
    1. sun_angle("07:00") == 15
    2. sun_angle("12:15"] == 93.75
    3. sun_angle("01:23") == "I don't see the sun!"

How it is used: One day it can save your life, if you'll be lost far away from civilization.

Precondition:
00:00 <= time <= 23:59


***(RU)***

Любой настоящий путешественник должен уметь делать три вещи:
добывать огонь, находить воду и извлекать полезную информацию из природы, окружающей его.
Программирование не поможет вам с огнем и водой, но с добычей информации справится вполне.

Ваша задача - определить угол солнца над горизонтом, зная время суток.
Исходные данные: солнце встает на востоке в 6:00, что соответствует углу 0 градусов.
В 12:00 солнце в зените, а значит угол = 90 градусов.
В 18:00 солнце садится за горизонт и угол равен 180 градусов.
В случае, если указано ночное время (раньше 6:00 или позже 18:00),
функция должна вернуть фразу "I don't see the sun!".

Входные данные: Время.

Выходные данные: Угол солнца над горизонтом, округленный до 2 знаков после запятой.

Пример:
    1. sun_angle("07:00") == 15
    2. sun_angle("12:15"] == 93.75
    3. sun_angle("01:23") == "I don't see the sun!"

Как это используется: Жизненно необходимый навык для любого путешественника,
особенно в случае утери компаса и разрядившегося мобильного телефона с GPS.
Правда, в такой ситуации приходится решать обратную задачу -
определять время по углу солнца и производить несколько дополнительных расчетов.

Предусловия:
00:00 <= время <= 23:59

'''


from datetime import datetime


def sun_angle(time):
    sunrise = datetime.strptime('06:00', '%H:%M')
    sundown = datetime.strptime('18:00', '%H:%M')
    time = datetime.strptime(time, '%H:%M')
    if sunrise > time or time > sundown:
        return "I don't see the sun!"
    total_sunny = int((sundown - sunrise).total_seconds() / 60)
    difference = int((time - sunrise).total_seconds() / 60)
    degrees = (180 / total_sunny) * difference
    return degrees


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
