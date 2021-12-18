import random
class Fartun:
    def __init__(self, wallet):
        self.door = ['медуза','цербер','дракон']
        self.door1 = random.choice(self.door)
        self.door2 = random.choice(self.door)
        self.wallet = wallet
    def game1(self):
        print('-'*100)
        print("\nесть дверь и 3 существа: дракон, цербер и медуза,"
              " судья говорит кто за дверью, вы должны ответить 'верю' или 'не верю'")
        # print(f'\nподсказка: {self.door2}')
        referee = input(f'\nсудья:\nза дверью {self.door1}: ')
        if referee == 'верю' and self.door1 == self.door2:
            self.wallet += 1000
            print(f'вы угадали! за дверью было существо {self.door2}\n'
                  f'на ваш баланс зачислено 1000$!\n'
                  f'судья был не прав!\n'
                  f'\nваш баланс {self.wallet}$')
            print('-'*40)
            return True
        elif referee == 'верю' and self.door1 != self.door2:
            self.wallet -= 1000
            print(f'вы не угадали! за дверью было существо {self.door2}\n'
                  f'с вас сняли 1000$\n'
                  f'судья был прав!\n'
                  f'\n ваш баланс {self.wallet}$')
            print('-'*40)
            return True
        elif referee == 'не верю' and self.door1 != self.door2:
            self.wallet += 1000
            print(f'вы угадали! за дверью было существо {self.door2}\n'
                  f'на ваш баланс зачислино 1000$!\n'
                  f'судья был не прав!\n'
                  f'\nваш баланс {self.wallet}$')
            print('-'*40)
            return True
        elif referee == 'не верю' and self.door1 == self.door2:
            self.wallet -= 1000
            print(f'вы не угадали! за дверью было существо {self.door}\n'
                  f'с вас сняли 1000$\n'
                  f'судья был прав!\n'
                  f'\nваш баланс {self.wallet}$')
            print('-'*40)
            return True
        else:
            print('вы можете вводить только верю или не верю')
            return True