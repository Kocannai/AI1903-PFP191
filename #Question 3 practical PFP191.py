import random
def Doan():
    while True:
        n = random.randint(1, 100)
        x = int(input('Nhap so x de doan: '))
        if x > n:
            print('n<x')
        elif x < n:
            print('n>x')
        elif x == n:
            print('EXACTLY!')
            break
Doan()
