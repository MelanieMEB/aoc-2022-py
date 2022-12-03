import unittest
import advent

def first_puzzle(file):
    return 1


def second_puzzle(file):
    return 2


class Tests(unittest.TestCase):
    def test_first_puzzle(self):
        # given
        file = advent.read_file('files/test01.txt')
        # when
        result = first_puzzle(file)
        # then
        self.assertEqual(result, 1)
        
    def test_second_puzzle(self):
        # given
        file = advent.read_file('files/test01.txt')
        # when
        result = second_puzzle(file)
        # then
        self.assertEqual(result, 2)

if __name__ == '__main__':
    file = advent.read_file('files/input01.txt')
    first_result = first_puzzle(file)
    print('First result :', first_result)
    second_result = second_puzzle(file)
    print('Second result :', second_result)
