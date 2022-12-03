import unittest
import advent

def first_puzzle(file):
    current_calories = 0
    max = 0
    for calories in file:
        if calories == '':
            max = max if current_calories < max else current_calories
            current_calories = 0
        else:
            current_calories = current_calories + int(calories)
    return max


def second_puzzle(file):
    current_calories = 0
    current_elf = 0
    calories_carrying = []
    for calories in file:
        if calories == '':
            calories_carrying.append(current_calories)
            current_calories = 0
            current_elf += 1
        else:
            current_calories = current_calories + int(calories)
    calories_carrying.append(current_calories)
    calories_carrying.sort(reverse=True)
    return calories_carrying[0] + calories_carrying[1] + calories_carrying[2]


class Tests(unittest.TestCase):
    def test_first_puzzle(self):
        # given
        file = advent.read_file('files/test01.txt')
        # when
        result = first_puzzle(file)
        # then
        self.assertEqual(result, 24000)
        
    def test_second_puzzle(self):
        # given
        file = advent.read_file('files/test01.txt')
        # when
        result = second_puzzle(file)
        # then
        self.assertEqual(result, 45000)

if __name__ == '__main__':
    file = advent.read_file('files/input01.txt')
    first_result = first_puzzle(file)
    print('First result :', first_result)
    second_result = second_puzzle(file)
    print('Second result :', second_result)
