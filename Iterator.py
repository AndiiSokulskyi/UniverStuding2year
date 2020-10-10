class GN_Iterator:

    def __init__(self):
        self.a, self.b = 1, 1

    def __iter__(self):
        return self

    def __devsum(self, k):
        sum = 0
        for i in range(1, k):
            if k % i == 0:
                sum += i
        return sum

    def __isfriend(self, a, b):
        if (a == self.__devsum(b)) & (b == self.__devsum(a)):
            return True
        else:
            return False

    def __next__(self):
        while True:
            for i in range(1, self.a):
                if self.__isfriend(self.a, i) == True:
                    self.b = i
                    self.a += 1
                    return (self.b, self.a - 1)
            self.a += 1