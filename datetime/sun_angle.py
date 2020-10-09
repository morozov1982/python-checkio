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
