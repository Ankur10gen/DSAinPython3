from Progressions.Progression import Progression

class GeometricProgression(Progression):

    def __init__(self,start=1,common_ratio=2):

        super().__init__(start)
        self._cr = common_ratio

    def _advance(self):
        self._current *= self._cr

gp1 = GeometricProgression(3,3)
gp1.print_progression(5)