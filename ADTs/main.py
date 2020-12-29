import sys


class ADT(list):
    def __init__(self, length: int):
        self.array = [0]*length
        self.size = length
        self.length = 0

    def Display(self):
        for i in range(self.length):
            print(self.array[i], end="\t")

    def AppendIn(self, element: int):
        if(self.length >= self.size):
            print("Array is fully filled")
            return
        self.array[self.length] = element
        self.length += 1

    def Sum(self):
        total = 0
        for i in range(self.length):
            if(i > self.length-i-1):

                return total
            elif i == self.length-i-1:
                total += self.array[i]
                return total

            total += (self.array[i] + self.array[self.length-i-1])

    def Average(self):
        total_sum = self.Sum()
        return total_sum/self.length

    def Max(self):
        max = -(sys.maxsize - 1)
        for i in range(self.length):
            if self.array[i] > max:
                max = self.array[i]
        return max

    def Min(self):
        min = sys.maxsize
        for i in range(self.length):
            if self.array[i] < min:
                min = self.array[i]
        return min

    def ReverseArray(self):
        for i in range(self.length):
            if(i >= self.length-i-1):
                self.Display()
                return
            temp = self.array[i]
            self.array[i] = self.array[self.length - i - 1]
            self.array[self.length - i - 1] = temp

    def RotateLeft(self):
        temp = self.array[0]
        for i in range(self.length):
            if(i == self.length-1):
                self.array[i] = temp
                return
            self.array[i] = self.array[i+1]
