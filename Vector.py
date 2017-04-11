class Vector:
    """Vector Operations"""

    def __init__(self,d):
        """Initialise a d-dimension vector"""
        self._coord = [0] * d

    def __len__(self):
        """Return: Length of coordinates"""
        return len(self._coord)

    def __setitem__(self, key, value):
        """Set a coordinate to a value"""
        self._coord[key] = value

    def __getitem__(self, item):
        """Return: A coordinate"""
        return self._coord[item]

    def __add__(self, other):
        """Add another vector"""
        if len(self._coord) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return: True if vector has same coordinates as other"""
        return self._coord == other._coord

    def __ne__(self, other):
        """Return: True is Vector differs"""
        return not self == other

    def __str__(self):
        """Produce str representation of vector"""
        return '<' + str(self._coord)[1:-1] + '>'

v1 = Vector(3)
v1.__setitem__(1,10)
v2 = Vector(3)
v2.__setitem__(2,20)
print(v1+v2)