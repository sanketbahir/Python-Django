class Number:
    def __init__(self):
        self.Size = 0
        self.Arr = list()
        print(type(self.Arr))

    def Accept(self):
        print('Enter the number of elements you want:')
        self.Size = int(input())

        print('Enter the values:')
        for i in range(self.Size):
            value = int(input())
            self.Arr.append(value)

    def Display(self):
        print('Elements from the list:')
        for i in range(self.Size):
            print(self.Arr[i])

    def Summation(self):
        sum = 0
        for i in range(self.Size):
            sum += self.Arr[i]
        return sum

    def Average(self):
        sum = 0
        for i in range(self.Size):
            sum += self.Arr[i]
        return sum / self.Size

    def Max(self):
        num = self.Arr[0]
        for i in range(1, self.Size):
            if (i > num):
                self.Arr = num
        return num

def main():
    obj = Number()
    obj.Accept()
    obj.Display()
    Output = obj.Summation()
    print('Summation of all elements is:', Output)
    Average = obj.Average()
    print('Average of all elements is:', Average)
    maximum = obj.Max()
    print(maximum)

if __name__ == "__main__":
    main()
