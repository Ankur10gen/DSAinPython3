from Progressions.Progression import Progression

class FibonacciProgression(Progression):

    def __init__(self, first=0, second=1):

        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        # Update current value by taking sum of previous two
        self._prev, self._current = self._current, self._prev + self._current

fp1 = FibonacciProgression()
fp1.print_progression(10)