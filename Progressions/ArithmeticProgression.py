from Progressions.Progression import Progression

class ArithmeticProgression(Progression):

    """Base class is Progression. This class will additionally accept common difference value"""

    def __init__(self, start=0, common_difference=1):
        super().__init__(start)
        self._cd = common_difference

    def _advance(self):
        self._current += self._cd

ap1 = ArithmeticProgression(0,-2)
ap1.print_progression(10)