import unittest
import advent
import numpy as np

def is_the_tallest(list_of_trees, position):
    visible_before = True
    visible_after = True
    tree = list_of_trees[position]
    for t in range(0, position):
        if list_of_trees[t] >= tree:
            visible_before = False
    for t in range(position+1, list_of_trees.size):
        if list_of_trees[t] >= tree:
            visible_after = False
    return (visible_before or visible_after)

def visible_trees(list_of_trees, position):
    visible_trees_before = 0
    visible_trees_after = 0
    tree = list_of_trees[position]
    for t in reversed(range(0,position)):
        if list_of_trees[t] < tree:
            visible_trees_before += 1
        elif list_of_trees[t] >= tree:
            visible_trees_before += 1
            break
    for t in range(position+1, list_of_trees.size):
        if list_of_trees[t] < tree:
            visible_trees_after += 1
        elif list_of_trees[t] >= tree:
            visible_trees_after += 1
            break

    return (visible_trees_before * visible_trees_after)

def first_puzzle(file):
    trees_map = np.array(list(map(lambda line: list(map(lambda t: int(t), line)), file)))
    number_of_lines = trees_map.shape[0]
    number_of_column = trees_map.shape[1]
    number_visible_tree = 0
    for line in range(0, number_of_lines):
        for column in range(0, number_of_column):
            if line == 0 or line == number_of_lines-1 or column == 0 or column == number_of_column -1 : 
                number_visible_tree += 1
            else:
                others_tree_in_line = trees_map[line]
                others_tree_in_column = trees_map[:, column]
                tallest_in_line = is_the_tallest(others_tree_in_line, column)
                tallest_in_column = is_the_tallest(others_tree_in_column, line)
                if tallest_in_line or tallest_in_column:
                    number_visible_tree += 1
    return number_visible_tree


def second_puzzle(file):
    trees_map = np.array(list(map(lambda line: list(map(lambda t: int(t), line)), file)))
    number_of_lines = trees_map.shape[0]
    number_of_column = trees_map.shape[1]
    max_visible_tree = 0
    for line in range(0, number_of_lines):
        for column in range(0, number_of_column):
            if line == 0 or line == number_of_lines-1 or column == 0 or column == number_of_column -1 : 
                max_visible_tree = max_visible_tree
            else :
                others_tree_in_line = trees_map[line]
                others_tree_in_column = trees_map[:, column]
                visible_in_line = visible_trees(others_tree_in_line, column)
                visible_in_column = visible_trees(others_tree_in_column, line)
                max_visible_tree = visible_in_line * visible_in_column if visible_in_line * visible_in_column > max_visible_tree else max_visible_tree
    return max_visible_tree


class Tests(unittest.TestCase):
    def test_first_puzzle(self):
        # given
        file = advent.read_file('files/test08.txt')
        # when
        result = first_puzzle(file)
        # then
        self.assertEqual(result, 21)
        
    def test_second_puzzle(self):
        # given
        file = advent.read_file('files/test08.txt')
        # when
        result = second_puzzle(file)
        # then
        self.assertEqual(result, 8)

if __name__ == '__main__':
    file = advent.read_file('files/input08.txt')
    first_result = first_puzzle(file)
    print('First result :', first_result)
    second_result = second_puzzle(file)
    print('Second result :', second_result)
