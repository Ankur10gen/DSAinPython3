class SequenceIterator:
    """Iterator for python's sequence types"""

    def __init__(self,sequence):
        """Create: Iterator for sequence"""
        self._seq = sequence
        self._k = -1    # will inc to 0 on first call

    def __next__(self):
        """Return: Next element/Raise StopIteration error"""
        self._k += 1
        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration('STOP') # No more elements

    def __iter__(self):
        """Iterator must return itself as iterator"""
        return self

    def __len__(self):
        return len(self._seq)



seq = SequenceIterator([x for x in range(100)])
for i in range(len(seq)):
    print(seq.__next__())