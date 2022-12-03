import unittest
import advent
import numpy as np

def first_puzzle(file):
    match = []
    for round in file :
        if round.find('X') != -1:
            match.append(1)
            if round.find('A') != -1:
                match.append(3)
            if round.find('B') != -1:
                match.append(0)
            if round.find('C') != -1:
                match.append(6)
        if round.find('Y') != -1:
            match.append(2)
            if round.find('A') != -1:
                match.append(6)
            if round.find('B') != -1:
                match.append(3)
            if round.find('C') != -1:
                match.append(0)
        if round.find('Z') != -1:
            match.append(3)
            if round.find('A') != -1:
                match.append(0)
            if round.find('B') != -1:
                match.append(6)
            if round.find('C') != -1:
                match.append(3)
    return np.sum(match)


def second_puzzle(file):
    match = []
    for round in file :
        if round.find('X') != -1:
            match.append(0)
            if round.find('A') != -1:
                match.append(3)
            if round.find('B') != -1:
                match.append(1)
            if round.find('C') != -1:
                match.append(2)
        if round.find('Y') != -1:
            match.append(3)
            if round.find('A') != -1:
                match.append(1)
            if round.find('B') != -1:
                match.append(2)
            if round.find('C') != -1:
                match.append(3)
        if round.find('Z') != -1:
            match.append(6)
            if round.find('A') != -1:
                match.append(2)
            if round.find('B') != -1:
                match.append(3)
            if round.find('C') != -1:
                match.append(1)
    return np.sum(match)


class Tests(unittest.TestCase):
    def test_first_puzzle(self):
        # given
        file = advent.read_file('files/test02.txt')
        # when
        result = first_puzzle(file)
        # then
        self.assertEqual(result, 15)
        
    def test_second_puzzle(self):
        # given
        file = advent.read_file('files/test02.txt')
        # when
        result = second_puzzle(file)
        # then
        self.assertEqual(result, 12)

if __name__ == '__main__':
    file = advent.read_file('files/input02.txt')
    first_result = first_puzzle(file)
    print('First result :', first_result)
    second_result = second_puzzle(file)
    print('Second result :', second_result)

