#Q3
#1
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
x = float(input('x = '))
#2
S1 = a*x**2 + b*x + c
print('S1 = ', S1)
#3
import math
N = b**2-4*a*c
if N > 0:
    S2 = math.sqrt(b**2 - 4*a*c)
else:
    S2=0
print('S2 = ', S2)
#4
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a+b>c and a+c>b and b+c>a:
    print('a, b and c are sides of a triangle')
else:
    print('a, b and c are not sides of a triangle')
#5
if a+b>c and a+c>b and b+c>a:
    p=(a+b+c)/2
    S3=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('S3 = ', S3)
else:
    print('a, b and c are not sides of a triangle')
#Q4
#1
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a > b and a > c and b > c:
    print('Maximun is ', a)
    print('Minimun is ', c)
    print(c,'≤',b,'≤',a)
elif a > b and a > c and c > b:
    print('Maximun is ', a)
    print('Minimun is ', b)
    print(b,'≤',c,'≤',a)
elif b > c and b > a and a > c:
    print('Maximun is ', b)
    print('Minimun is ', c)
    print(c,'≤',a,'≤',b)
elif b > c and b > a and c > a:
    print('Maximun is ', b)
    print('Minimun is ', a)
    print(a,'≤',c,'≤',b)
elif c > a and c > b and a > b:
    print('Maximun is ', c)
    print('Minimun is ', b)
    print(b,'≤',a,'≤',c)
elif c > a and c > b and b > a:
    print('Maximun is ', c)
    print('Minimun is ', a)
    print(a,'≤',b,'≤',c)




