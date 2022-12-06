import unittest
import advent
import numpy as np
from functools import reduce

def first_puzzle(array, file):
    for move in file:
        number_of_crates = int(move.split(' ')[1])
        from_column = int(move.split(' ')[3])-1
        to_column = int(move.split(' ')[5])-1
        for i in range(number_of_crates):
                remove_item = array[from_column].pop(0)
                array[to_column].insert(0, remove_item)
    return reduce(lambda string,crate: string+crate[0], array, '')



def second_puzzle(array, file):
    for move in file:
        number_of_crates = int(move.split(' ')[1])
        from_column = int(move.split(' ')[3])-1
        to_column = int(move.split(' ')[5])-1
        move_element = []
        for i in range(number_of_crates):
            if len(array[from_column])>0:
                move_element.append(array[from_column].pop(0))
        array[to_column] = move_element + array[to_column]

    return reduce(lambda string,crate: string+crate[0], array, '')


class Tests(unittest.TestCase):
    def test_first_puzzle(self):
        # given
        file = advent.read_file('files/test05.txt')
        array = [['N','Z'], ['D','C', 'M'], ['P']]
        # when
        result = first_puzzle(array, file)
        # then
        self.assertEqual(result, 'CMZ')
        
    def test_second_puzzle(self):
        # given
        file = advent.read_file('files/test05.txt')
        array = [['N','Z'], ['D','C', 'M'], ['P']]
        # when
        result = second_puzzle(array, file)
        # then
        self.assertEqual(result, 'MCD')


if __name__ == '__main__':
    file = advent.read_file('files/input05.txt')
    array = [
        ['J','F', 'C', 'N', 'D', 'B', 'W'], 
        ['T','S', 'L', 'Q', 'V', 'Z', 'P'],
        ['T','J', 'G', 'B', 'Z', 'P'],
        ['C','H', 'B', 'Z', 'J', 'L', 'T', 'D'],
        ['S','J', 'B', 'V', 'G'],
        ['Q','S', 'P'],
        ['N','P', 'M', 'L', 'F', 'D', 'V', 'B'],
        ['R','L', 'D', 'B', 'F', 'M', 'S', 'P'],
        ['R','T', 'D', 'V']]

    first_result = first_puzzle(array, file)
    print('First result :', first_result)

    array = [
        ['J','F', 'C', 'N', 'D', 'B', 'W'], 
        ['T','S', 'L', 'Q', 'V', 'Z', 'P'],
        ['T','J', 'G', 'B', 'Z', 'P'],
        ['C','H', 'B', 'Z', 'J', 'L', 'T', 'D'],
        ['S','J', 'B', 'V', 'G'],
        ['Q','S', 'P'],
        ['N','P', 'M', 'L', 'F', 'D', 'V', 'B'],
        ['R','L', 'D', 'B', 'F', 'M', 'S', 'P'],
        ['R','T', 'D', 'V']]
    second_result = second_puzzle(array2, file)
    print('Second result :', second_result)
