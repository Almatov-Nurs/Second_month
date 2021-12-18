import  random
class WinOrLose:
    def __init__(self, slot, wallet, bet, choose):
        self.slot = slot
        self.wallet = wallet
        self.bet = bet
        self.choose = choose
    def game_result(self):
        if self.bet <= self.wallet:
            if self.choose == self.slot:
                print('↓'*40)
                self.wallet = self.wallet + self.bet
                print(f'вы выиграли! ваш слот: {self.choose}\n'
                      f'             слот был: {self.slot}\n'
                      f'ваш баланс теперь составляет: {self.wallet}$')
                print('-'*40)
                return True
            else:
                print('↓' * 40)
                self.wallet -= self.bet
                print(f'вы проиграли! ваш слот: {self.choose}\n'
                      f'             слот был: {self.slot}\n'
                      f'ваш баланс теперь составляет: {self.wallet}$')
                print('-'*40)
                return True
        elif self.bet > self.wallet:
            print('вы не можете делать ставку больше вашего баланса!')
            return True
