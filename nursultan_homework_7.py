num = 655

def revers_num(num):
    n = num
    num1 = 0
    while num > 0:
        digit = num % 10
        num = num // 10
        num1 = num1 * 10 + digit
    print('ваше перевернутое число',num1)
    if num1 == n:
        print(num1,'универсальное число!')
    else:
        print('число:',n,'не универсальна!')
revers_num(num)