import unittest
import textwrap
import numpy as np
import advent

def find_double_letter(string):
    rucksacks = np.array_split(list(string),2)
    object_in_double='a'
    for object in rucksacks[0]:
        if object in rucksacks[1]:
            object_in_double = object
    return object_in_double

def value_for_object(letter):
    ascii_value = ord(letter)
    return (ascii_value - 65)+27 if ascii_value < 97 else ascii_value - 96

def find_shared_item(groups):
    for object in groups[0]:
        if object in groups[1] and object in groups[2]:
            return object

def first_puzzle(file):
    priorities = 0

    for backpack in file:
        object_in_double = find_double_letter(backpack)
        priorities += value_for_object(object_in_double)

    return priorities

def second_puzzle(file):
    priorities = 0
    index = 0
    while index < len(file):
        backpacks = [file[index], file[index+1], file[index+2]]
        object_in_all_groups = find_shared_item(backpacks)
        priorities += value_for_object(object_in_all_groups)
        index +=3

    return priorities


class Tests(unittest.TestCase):
    def test_find_double(self):
        # given
        string = 'vJrwpWtwJgWrhcsFMMfFFhFp'
        # when
        result = find_double_letter(string)
        # then
        self.assertEqual(result, 'p')
    def test_find_value_for_object(self):
        # given
        object = 'P'
        # when
        result = value_for_object(object)
        # then
        self.assertEqual(result, 42)
    def test_find_value_for_small_object(self):
        # given
        object = 'p'
        # when
        result = value_for_object(object)
        # then
        self.assertEqual(result, 16)
    def test_find_shared_item(self):
        # given
        groupe1=['vJrwpWtwJgWrhcsFMMfFFhFp','jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL','PmmdzqPrVvPwwTWBwg']
        # when
        result = find_shared_item(groupe1)
        # then
        self.assertEqual(result, 'r')

    def test_first_puzzle(self):
        # given
        file = advent.read_file('files/test03.txt')
        # when
        result = first_puzzle(file)
        # then
        self.assertEqual(result, 157)
        
    def test_second_puzzle(self):
        # given
        file = advent.read_file('files/test03.txt')
        # when
        result = second_puzzle(file)
        # then
        self.assertEqual(result, 70)


if __name__ == '__main__':
    file = advent.read_file('files/input03.txt')
    first_result = first_puzzle(file)
    print('First result :', first_result)
    second_result = second_puzzle(file)
    print('Second result :', second_result)