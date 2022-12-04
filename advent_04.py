import unittest
import textwrap
import numpy as np
import advent

def get_all_sections(sections):
    first_section = int(sections.split('-')[0])
    second_section = int(sections.split('-')[1])
    all_sections = ','
    while first_section <= second_section:
        all_sections = all_sections + str(first_section) + ','
        first_section += 1
    return all_sections

def is_contains_fully_overlap(sections_first_elf, sections_second_elf):
    return True if (sections_first_elf.find(sections_second_elf) > -1 or
        sections_second_elf.find(sections_first_elf) > -1) else False

def transform_to_set(sections):
    array = np.array(sections.split(','))
    filtered_array = array != ''
    return set(array[filtered_array])

def is_contains_overlap(sections_first_elf, sections_second_elf):
    set_sections_first_elf = transform_to_set(sections_first_elf)
    set_sections_second_elf = transform_to_set(sections_second_elf)
    return True if len(set_sections_second_elf.intersection(set_sections_first_elf)) > 0 else False

def first_puzzle(file):
    number_of_overlap = 0
    for couple_of_sections in file:
        sections_first_elf = get_all_sections(couple_of_sections.split(',')[0])
        sections_second_elf = get_all_sections(couple_of_sections.split(',')[1])

        number_of_overlap += 1 if is_contains_fully_overlap(sections_first_elf, sections_second_elf) else 0
    return number_of_overlap

def second_puzzle(file):
    number_of_overlap = 0
    for couple_of_sections in file:
        sections_first_elf = get_all_sections(couple_of_sections.split(',')[0])
        sections_second_elf = get_all_sections(couple_of_sections.split(',')[1])

        number_of_overlap += 1 if is_contains_overlap(sections_first_elf, sections_second_elf) else 0
    return number_of_overlap

    return 4


class Tests(unittest.TestCase):
    def test_get_all_sections(self):
        # given
        string = '2-6'
        # when
        result = get_all_sections(string)
        # then
        self.assertEqual(result,',2,3,4,5,6,')
    def test_get_all_sections_only_one_section(self):
        # given
        string = '6-6'
        # when
        result = get_all_sections(string)
        # then
        self.assertEqual(result,',6,')

    def test_is_contains_fully_overlap_true(self):
        # given
        first_elf = ',1,2,3,4,'
        second_elf = ',2,3,4,'
        # when
        result = is_contains_fully_overlap(first_elf, second_elf)
        # then
        self.assertEqual(result,True)
    def test_is_contains_fully_overlap_true_exchange_elf(self):
        # given
        first_elf = ',2,3,4,'
        second_elf = ',1,2,3,4,5,'
        # when
        result = is_contains_fully_overlap(first_elf, second_elf)
        # then
        self.assertEqual(result,True)

    def test_is_contains_fully_overlap_false(self):
        # given
        first_elf = ',1,2,3,4,'
        second_elf = ',3,4,5,'
        # when
        result = is_contains_fully_overlap(first_elf, second_elf)
        # then
        self.assertEqual(result,False)

    def test_is_contains_overlap_true(self):
        # given
        first_elf = ',1,2,3,4,'
        second_elf = ',3,4,5,'
        # when
        result = is_contains_fully_overlap(first_elf, second_elf)
        # then
        self.assertEqual(result,True)
    def test_is_contains_overlap_true(self):
        # given
        first_elf = ',1,2,3,4,'
        second_elf = ',5,6'
        # when
        result = is_contains_fully_overlap(first_elf, second_elf)
        # then
        self.assertEqual(result,False)

    def test_first_puzzle(self):
        # given
        file = advent.read_file('files/test04.txt')
        # when
        result = first_puzzle(file)
        # then
        self.assertEqual(result, 2)

    def test_second_puzzle(self):
        # given
        file = advent.read_file('files/test04.txt')
        # when
        result = second_puzzle(file)
        # then
        self.assertEqual(result, 4)


if __name__ == '__main__':
    file = advent.read_file('files/input04.txt')
    first_result = first_puzzle(file)
    print('First result :', first_result)
    second_result = second_puzzle(file)
    print('Second result :', second_result)