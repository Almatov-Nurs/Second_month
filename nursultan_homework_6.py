class Sum_num:
    def __init__(self):
        self.numbers = [2, 7, 11, 15]
        self.desired_sum = 9

    def summ(self, numbers, desired_sum):
        for i in numbers:
            for a in numbers:
                if i + a == desired_sum:
                    print([numbers.index(i),numbers.index(a)])
test = Sum_num()
test.summ(test.numbers,test.desired_sum)
