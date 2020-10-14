'''
***** Pawn Brotherhood *** (Simple) *****

***(EN)***

Almost everyone in the world knows about the ancient game Chess
and has at least a basic understanding of its rules.
It has various units with a wide range of movement patterns allowing
for a huge number of possible different game positions
(for example Number of possible chess games at the end of the n-th plies).
For this mission, we will examine the movements and behavior of chess pawns.

Chess is a two-player strategy game played on a checkered game board laid out in eight rows
(called ranks and denoted with numbers 1 to 8) and eight columns
(called files and denoted with letters a to h) of squares.
Each square of the chessboard is identified by a unique coordinate pair — a letter and a number
(ex, "a1", "h8", "d6").
For this mission we only need to concern ourselves with pawns.
A pawn may capture an opponent's piece on a square diagonally in front of it on an adjacent file,
by moving to that square.
For white pawns the front squares are squares with greater row number than the square they currently occupy.

A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall.
With this strategy, one pawn defends the others.
A pawn is safe if another pawn can capture a unit on that square.
We have several white pawns on the chess board and only white pawns.
You should design your code to find how many pawns are safe.

You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.

Output: The number of safe pawns as a integer.

Example:
    1. safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    2. safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

How it is used: For a game AI one of the important tasks is the ability to estimate game state.
This concept will show how you can do this on the simple chess figures positions.

Precondition:
    0 < pawns ≤ 8


***(RU)***

Шахматы известны по всему миру, и практически всем людям знакомы их основные правила игры.
В игре используется набор фигур, которые могут ходить по игровому полю различными способами,
что обеспечивает огромное количество различных игровых комбинаций
(к примеру, количество возможных шахматных партий оценивается Шенноном в 10^118).
В этой задаче мы будем исследовать правила игры пешками.

Шахматы - это стратегическая игра двух игроков, которая разыгрывается на игровой доске с клетками,
расположенными в восьми рядах (называемых горизонталями и обозначаемых цифрами от 1 до 8)
и в восьми колонках (называемых вертикалями и обозначаемых буквами от a до h).
Каждая клетка доски идентифицируется уникальной парой координат,
состоящей из буквы и цифры (например, "a1", "h8", "d6").
В этой задаче мы будем иметь дело только с пешками.
Пешка может бить пешку противника, которая находится перед ней в соседней клетке по диагонали справа или слева,
переходя в эту клетку. У белых пешек клетки перед ними имеют номер горизонтали на единицу больше.

Сама по себе пешка является слабой фигурой,
но мы можем использовать до восьми пешек для построения оборонительной стены.
Стратегия оборонительной стены основывается на защите друг друга.
Пешка защищена, если её клетка находится по ударом другой своей пешки.
На игровом поле находятся только белые пешки.
Вы должны разработать код, позволяющий определить сколько пешек защищены в этой позиции.

Вам предоставляется набор координат, в которых расставлены белые пешки.
Вы должны подсчитать количество защищенных пешек.

Входные данные: Координаты расставленных пешек в виде набора строк.

Выходные данные: Количество защищенных пешек в виде целого числа.

Пример:
    1. safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    2. safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

Как это используется:
Для игрового искусственного интеллекта оценка текущего состояния в игре является одной из важных задач.
Эта методика покажет вам как можно реализовать это для расстановок шахматных фигур.

Предусловия:
    0 < pawns ≤ 8

'''

# моё решние
COLS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ROWS = ['1', '2', '3', '4', '5', '6', '7', '8']


def safe_pawns(pawns: set) -> int:
    if len(pawns) < 2:
        return 0
    count = 0
    for pawn in pawns:
        left_def = ''
        right_def = ''
        col_idx = int(COLS.index(pawn[0]))
        row_idx = int(ROWS.index(pawn[1]))
        if row_idx > 0:
            if col_idx > 0:
                left_def = COLS[col_idx - 1] + ROWS[row_idx - 1]
            if col_idx < 7:
                right_def = COLS[col_idx + 1] + ROWS[row_idx - 1]
        count += 1 if (left_def in pawns) or (right_def in pawns) else 0
    return count


# не моё, но более лаконичное решение
def safe_pawns_1(pawns: set) -> int:
    def guard12(pa):
        guard1 = chr(ord(pa[0]) - 1) + str(int(pa[1]) - 1)
        guard2 = chr(ord(pa[0]) + 1) + str(int(pa[1]) - 1)
        return guard1 in pawns or guard2 in pawns

    return sum(guard12(i) for i in list(pawns))


if __name__ == '__main__':
    print(safe_pawns(["a2", "b4", "c6", "d8", "e1", "f3", "g5", "h8"]))
    print(safe_pawns(["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
