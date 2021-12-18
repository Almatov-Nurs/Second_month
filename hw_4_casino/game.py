from month_2.casino import win_or_lose, fart
import random


class Game:
    def __init__(self):
        self.slot1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        self.wallet = 1000

    def game(self):
        while True:
            print(f'ваш баланс: {self.wallet}$')
            test = win_or_lose.WinOrLose(slot=random.choice(self.slot1), wallet=self.wallet,
                                         bet=int(input('ваша ставка: ')),
                                         choose=int(input('выберите слот от 1-30: ')))
            test.game_result()
            self.wallet = test.wallet
            while test.wallet <= 0:
                print('-' * 40)
                ans = input('вы хотите сыграть в фортуну? да или нет?: ')
                if ans == 'да':
                    test1 = fart.Fartun(wallet=self.wallet)
                    test1.game1()
                    self.wallet = test1.wallet
                elif ans == 'нет':
                    print('\nвы вернулись в казино!')
                    print('-' * 40)
                    break
                else:
                    print('-'*40)
                    print('вводите только да или нет!')
                    continue
                if self.wallet >= 1000:
                    break
            if test.bet <= 0:
                print('вы не сделали ставку!')
                print('-'*40)
                self.wallet += test.bet
                continue
            if self.wallet <= 0:
                print('вы в долгу! игра не может продолжаться!')
                break


gaming = Game()
gaming.game()
