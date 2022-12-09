import unittest
import advent
import math

def move_T_and_H(current_T, current_H, direction):
    position_T = list(current_T)
    position_H = list(current_H)
    if direction == 'R':
        position_H[0] += 1
        if math.dist(position_T, position_H)>=2:
            position_T[1] = position_H[1]
            position_T[0] = position_H[0]-1
    elif direction == 'L':
        position_H[0] += -1
        if math.dist(position_T, position_H)>=2:
            position_T[1] = position_H[1]
            position_T[0] = position_H[0]+1
    elif direction == 'U':
        position_H[1] += 1
        if math.dist(position_T, position_H)>=2:
            position_T[0] = position_H[0]
            position_T[1] = position_H[1]-1
    elif direction == 'D':
        position_H[1] += -1
        if math.dist(position_T, position_H)>=2:
            position_T[0] = position_H[0]
            position_T[1] = position_H[1]+1
    return [tuple(position_T), tuple(position_H)]

def move_T_to_H(current_T, current_H, current_1_to_8, direction):
    all_snake = [current_T] + current_1_to_8 + [current_H]
    new_position = []
    for position in range(1, len(all_snake)):
        head = all_snake(position-1)
        tail = all_snake(position)
        [new_head, new_tail] = move_T_and_H(head,tail, direction)
        new_position
    return [tuple(position_T), tuple(position_H)]

def first_puzzle(file):
    all_positions_for_T = set()
    current_T = (0,0)
    current_H = (0,0)
    for move in file:
        direction = move.split(' ')[0]
        step = int(move.split(' ')[1])
        for s in range(0, step):
            [current_T, current_H] = move_T_and_H(current_T, current_H, direction)
            print([current_H, current_T])
            all_positions_for_T.add(current_T)
    return len(all_positions_for_T)


def second_puzzle(file):
    all_positions_for_T = set()
    current_T = (0,0)
    current_1_to_8 = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
    current_H = (0,0)
    for move in file:
        direction = move.split(' ')[0]
        step = int(move.split(' ')[1])
        for s in range(0, step):
            [current_T, current_1_to_8, current_H] = move_T_to_H(current_T, current_H, current_1_to_8, direction)
            all_positions_for_T.add(current_T)
    return len(all_positions_for_T)

class Tests(unittest.TestCase):
    def test_first_puzzle(self):
        # given
        file = advent.read_file('files/test09.txt')
        # when
        result = first_puzzle(file)
        # then
        self.assertEqual(result, 13)

    def test_second_puzzle(self):
        # given
        file = advent.read_file('files/test09.txt')
        # when
        result = second_puzzle(file)
        # then
        self.assertEqual(result, 2)

if __name__ == '__main__':
    file = advent.read_file('files/input09.txt')
    first_result = first_puzzle(file)
    print('First result :', first_result)
    second_result = second_puzzle(file)
    print('Second result :', second_result)
