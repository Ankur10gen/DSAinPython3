import unittest
from Progressions.ArithmeticProgression import ArithmeticProgression

class TestArithmeticProgression(unittest.TestCase):
    def test_print_progression(self):
        prog = ArithmeticProgression(0,2)
        self.assertEqual(prog.print_progression(5), print('5 7 9 11 13'))


if __name__ == '__main__':
    unittest.main()
