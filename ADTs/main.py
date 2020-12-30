import sys


class ADT(list):
    def __init__(self, length: int):
        self.array = [0]*length
        self.size = length
        self.length = 0

    def __init__(self, array: list):
        self.array = array
        self.size = len(array)
        self.length = self.size

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

    def RotateRight(self, rotaion_amount: int):
        # * in rotation from where we will start come back to that palce again
        # * [Fromula used] : (current Index + rotation)%arraylength ,and store new index value to temp and perfom the same thing untill we reach to the place from where we have started
        temp_index = -1
        temp_val = -10000
        start_index = 0
        # emulating do while in python
        while True:
            if(start_index == temp_index):
                break
            if temp_index == -1:

                temp_index = (start_index+rotaion_amount) % self.size
                temp_val = self.array[temp_index]
                self.array[temp_index] = self.array[start_index]
            else:
                temp_index = (temp_index+rotaion_amount) % self.size
                temp = self.array[temp_index]
                self.array[temp_index] = temp_val
                temp_val = temp

        self.Display()  # show the result

    def NegativePositiveSeprator(self):
        ptr_i = 0
        ptr_j = self.size-1
        while True:
            if ptr_i == ptr_j or ptr_i >= self.size or ptr_j <= 0:
                break
            if self.array[ptr_i] < 0:
                ptr_i += 1
            if self.array[ptr_j] >= 0:
                ptr_j -= 1

            if self.array[ptr_i] >= 0 and self.array[ptr_j] < 0:
                temp = self.array[ptr_i]
                self.array[ptr_i] = self.array[ptr_j]
                self.array[ptr_j] = temp
                ptr_i += 1
                ptr_j -= 1
        self.Display()
