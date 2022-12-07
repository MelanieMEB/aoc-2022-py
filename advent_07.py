import unittest
import advent
import numpy as np
import functools

parent_dir = '//'

def return_size_by_dir(file):
    size_by_dir = {}
    parent_of_dir = {}
    parent_of_dir[parent_dir] = ''
    current_folder = ''
    depth = -1
    for line in file:
        if '$ cd' in line:
            if '..' in line:
                depth = depth - 1
                current_folder = '/'.join(current_folder.split('/')[:-1])
            else:
                depth = depth + 1
                current_folder = current_folder + '/' + line.split(' ')[2]
                size_by_dir[current_folder] = size_by_dir[current_folder] if current_folder in size_by_dir else 0
        elif '$ ls' not in line:
            if 'dir' in line:
                dir = current_folder + '/' + line.split(' ')[1]
                parent_of_dir[dir] = current_folder
            else:
                size = int(line.split(' ')[0])
                size_by_dir[current_folder] = size_by_dir[current_folder] + size
                parent_folder = parent_of_dir[current_folder]
                while parent_folder != '':
                    size_by_dir[parent_folder] = size_by_dir[parent_folder] + size
                    parent_folder = parent_of_dir[parent_folder]
    return size_by_dir

def first_puzzle(file):
    size_by_dir = return_size_by_dir(file)
    acceptable_sizes = [size_by_dir[x] for x in size_by_dir if size_by_dir[x]<=100000]
    return functools.reduce(lambda a, b: a+b, acceptable_sizes)


def second_puzzle(file):
    size_by_dir = return_size_by_dir(file)
    needed_size = 30000000 - (70000000 - size_by_dir[parent_dir])
    acceptable_sizes = [size_by_dir[x] for x in size_by_dir if size_by_dir[x]>=needed_size]
    acceptable_sizes.sort()
    return acceptable_sizes[0]


class Tests(unittest.TestCase):
    def test_first_puzzle(self):
        # given
        file = advent.read_file('files/test07.txt')
        # when
        result = first_puzzle(file)
        # then
        self.assertEqual(result, 95437)
    def test_second_puzzle(self):
        # given
        file = advent.read_file('files/test07.txt')
        # when
        result = second_puzzle(file)
        # then
        self.assertEqual(result, 24933642)

if __name__ == '__main__':
    file = advent.read_file('files/input07.txt')
    first_result = first_puzzle(file)
    print('First result :', first_result)
    second_result = second_puzzle(file)
    print('Second result :', second_result)
