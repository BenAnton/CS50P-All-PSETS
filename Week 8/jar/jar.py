class Jar:
    def __init__(self, capacity=12):
        if capacity > 0:
            self._capacity = capacity
            self._size = 0
        else:
            raise ValueError("Must be positive")

    def __str__(self, ):
        return self._size * "🍪"

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Exceeded size")
        else:
            self._size += n

            return self._size

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError("Not enough cookies to withdraw")
        else:
            self._size -= n
            return self._size

    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size

