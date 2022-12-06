import unittest
import advent

def first_puzzle(file):
    signal = file[0]
    for i in range(4, len(signal)-1):
        sequence = [signal[x] for x in range(i-4,i)]
        double = [char2 for char1, char2 in enumerate(sequence) if char1 != sequence.index(char2)]
        if len(double) == 0:
            return i
    return -1


def second_puzzle(file):
    signal = file[0]
    for i in range(14, len(signal)-1):
        sequence = [signal[x] for x in range(i-14,i)]
        double = [char2 for char1, char2 in enumerate(sequence) if char1 != sequence.index(char2)]
        if len(double) == 0:
            return i
    return -1

class Tests(unittest.TestCase):
    def test_first_puzzle_example1(self):
        # given
        file = ['mjqjpqmgbljsphdztnvjfqwrcgsmlb']
        # when
        result = first_puzzle(file)
        # then
        self.assertEqual(result, 7)
    def test_first_puzzle_example2(self):
        # given
        file = ['bvwbjplbgvbhsrlpgdmjqwftvncz']
        # when
        result = first_puzzle(file)
        # then
        self.assertEqual(result, 5)
    def test_first_puzzle_example3(self):
        # given
        file = ['nppdvjthqldpwncqszvftbrmjlhg']
        # when
        result = first_puzzle(file)
        # then
        self.assertEqual(result, 6)
    def test_first_puzzle_example4(self):
        # given
        file = ['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg']
        # when
        result = first_puzzle(file)
        # then
        self.assertEqual(result, 10)             
    def test_first_puzzle_example5(self):
        # given
        file = ['zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']
        # when
        result = first_puzzle(file)
        # then
        self.assertEqual(result, 11)     
    def test_second_puzzle(self):
        # given
        file = ['mjqjpqmgbljsphdztnvjfqwrcgsmlb']
        # when
        result = second_puzzle(file)
        # then
        self.assertEqual(result, 19)

if __name__ == '__main__':
    file = advent.read_file('files/input06.txt')
    first_result = first_puzzle(file)
    print('First result :', first_result)
    second_result = second_puzzle(file)
    print('Second result :', second_result)
