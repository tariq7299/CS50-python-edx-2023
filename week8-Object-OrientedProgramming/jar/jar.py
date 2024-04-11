class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return '🍪' * self.size

    def deposit(self, n):
        total = n+self.size
        if n+self.size > self.capacity:
            raise ValueError
        self.size = n + self.size

    def withdraw(self, n):

        if n > self.size:
            raise ValueError
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 12:
            raise ValueError("Enter a valid capacity number")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

def main():


    jar1 = Jar(15)
    print(jar1)
    jar1.deposit(2)
    print(jar1)
    jar1.deposit(10)
    print(jar1)
    jar1.withdraw(2)
    jar1.withdraw(2)
    jar1.deposit(3)
    print(jar1)
    print(jar1.capacity)
    jar1.deposit(3)
    print(jar1.size)

if __name__ == "__main__":
    main()
