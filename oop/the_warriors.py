"""
***** The Warriors *** (Simple) *****

***(EN)***

I'm sure that many of you have some experience with computer games.
But have you ever wanted to change the game so that the characters or a game world
would be more consistent with your idea of the perfect game? Probably, yes.
In this mission (and in several subsequent ones, related to it) you’ll have a chance "to sit in the developer's chair"
and create the logic of a simple game about battles.
Let's start with the simple task - one-on-one duel.
You need to create the class Warrior, the instances of which will have 2 parameters - health (equal to 50 points)
and attack (equal to 5 points), and 1 property - is_alive,
which can be True (if warrior's health is > 0) or False (in the other case).
In addition you have to create the second unit type - Knight,
which should be the subclass of the Warrior but have the increased attack - 7.
Also you have to create a function fight(),
which will initiate the duel between 2 warriors and define the strongest of them.

The duel occurs according to the following principle:
    * Every turn, the first warrior will hit the second and this second will lose his health
    in the same value as the attack of the first warrior.
    After that, if he is still alive, the second warrior will do the same to the first one.
    * The fight ends with the death of one of them.
If the first warrior is still alive (and thus the other one is not anymore),
the function should return True, False otherwise.

Round     1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17
Warrior  50 50 43 43 36 36 29 29 22 22 15 15  8  8  1  1 -6
Knight   50 45 45 40 40 35 35 30 30 25 25 20 20 15 15 10 10

Example:
     1. chuck = Warrior()
     2. bruce = Warrior()
     3. carl = Knight()
     4. dave = Warrior()
     5.
     6. fight(chuck, bruce) == True
     7. fight(dave, carl) == False
     8. chuck.is_alive == True
     9. bruce.is_alive == False
    10. carl.is_alive == True
    11. dave.is_alive == False

Input: The warriors.

Output: The result of the duel (True or False).

How it is used: For computer games development.

Precondition:
    * 2 types of units
    * All given fights have an end (for all missions).


***(RU)***

Наверняка многие из вас имеют опыт прохождения компьютерных игр.
Возникало ли у вас в процессе игры желание изменить что-нибудь и сделать так,
чтобы персонажи или игровой мир больше соответствовали вашему представлению о хорошей игре? Скорее всего да.
В этой миссии (и в нескольких последующих, связанных с ней)
вам предоставится возможность «посидеть в кресле разработчика» и создать логику простой игры о сражениях.
Давайте начнем с малого — сражения 1×1.
В этой миссии вам необходимо будет создать класс Warrior,
у экземпляров которого будет 2 параметра — здоровье (равное 50) и атака (равная 5),
а также свойство is_alive, которое может быть True (если здоровье воина > 0) или False (в ином случае).
Кроме этого вам необходимо создать класс для второго типа солдат — Knight, который будет наследником Warrior,
но с увеличенной атакой — 7. Также вам необходимо будет создать функцию fight(),
которая будет проводить дуэли между 2 воинами и определять сильнейшего из них.

Бои происходят по следующему принципу:
    • каждый ход первый воин наносит второму урон в размере своей атаки,
    вследствие чего здоровье второго воина уменьшается
    • аналогично и второй воин, если он еще жив, поступает по отношению к первому.
Битва заканчивается смертью одного из них. Если первый воин все еще жив (а второй, соответственно, уже нет),
функция возвращает True, или в ином случае False.

Round     1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17
Warrior  50 50 43 43 36 36 29 29 22 22 15 15  8  8  1  1 -6
Knight   50 45 45 40 40 35 35 30 30 25 25 20 20 15 15 10 10

Пример:
     1. chuck = Warrior()
     2. bruce = Warrior()
     3. carl = Knight()
     4. dave = Warrior()
     5.
     6. fight(chuck, bruce) == True
     7. fight(dave, carl) == False
     8. chuck.is_alive == True
     9. bruce.is_alive == False
    10. carl.is_alive == True
    11. dave.is_alive == False

Входные данные: воины.

Выходные данные: результат поединка (True или False).

Как это используется: Для разработки компьютерных игр.

Предусловие: 2 типа солдат

"""


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


def fight(unit_1, unit_2):
    attacker, attacked = unit_1, unit_2
    while True:
        attacked.health -= attacker.attack
        if attacked.is_alive:
            attacker, attacked = attacked, attacker
            continue
        break
    return unit_1.is_alive


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    print(chuck.health)
    print(chuck.attack)
    print(chuck.is_alive)
    
    print(carl.health)
    print(carl.attack)
    print(carl.is_alive)

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
