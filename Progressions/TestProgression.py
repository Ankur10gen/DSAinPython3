import unittest
from Progressions.Progression import Progression

class TestProgression(unittest.TestCase):
    def test_print_progression(self):
        prog = Progression(3)
        self.(prog.print_progression(5), sys.'3 4 5 6 7')


if __name__ == '__main__':
    unittest.main()
