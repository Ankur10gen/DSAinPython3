class Range:
    """Mimic built-in range class"""
    def __init__(self,start,stop=None,step=1):

        if step == 0:
            raise ValueError('step cannot be 0')

        if stop is None:    #special case of range(n)
            start,stop = 0,start

        #effective length
        self._length = max(0,(stop - start + step - 1)//step)

        self._start = start
        self._step = step

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        if k < 0:
            k += len(self)

        if not 0 <= k < self._length:
            raise IndexError('index out of range')

        return self._start + k * self._step

r = Range(10,0,-2)
print(r.__getitem__(3))