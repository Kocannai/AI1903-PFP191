#Q1
#1
def calculate_sum(n):
    return sum(range(1,n+1))
#2
def factorial(n):
        if n==0:
             return 1
        else:
             return n*factorial(n-1)
#3
def tong(n):
    S3_sum=0
    for i in range(1, n+1):
        S3_sum+=1/i
    return S3_sum
while True:
    try:
        n=int(input('Nhap so lon hon 5:'))
        if n>5:
             break
        else:
            print('So vua nhap nho hon 5. Hay thu lai')
    except ValueError:
        print('So vua nhap khong hop le')
Sum=calculate_sum(n)
S2=factorial(n)
S3=tong(n)
print(f'1+2+3+...+{n}=', Sum)
print(f'{n}!=', S2)
print(f'1+1/2+1/3+...+1/{n}=', S3)
#4
def is_prime(n):
     if n<2:
          return False
     for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
     return True
while True:
    try:
          n=int(input('Nhap so lon hon 1:'))
          if n>1:
               break
          else:
               print('So vua nhap nho hon 1. Hay thu lai')
    except ValueError:
         print('So vua nhap khong hop le')
if is_prime(n):
    print(f'{n} is a prime number.')
else:
    print(f'{n} is not a prime number.')
#Q2
def find_primes(n):
    primes = []
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes
#1
def common_prime_dividers(m, n):
    primes_m = set(find_primes(m))
    primes_n = set(find_primes(n))
    common_dividers = primes_m.intersection(primes_n)
    return sorted(list(common_dividers))
#2
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
#3
def lcm(a, b):
    return (a * b) // gcd(a, b)
while True:
    try:
        m = int(input('Nhap m: '))
        n = int(input('Nhap n: '))
        break
    except ValueError:
        print('Nhap so khong hop le.')
common_dividers = common_prime_dividers(m, n)
print(f'Cac uoc so nguyen to chung cua {m} va {n}: {common_dividers}')
gcd_result = gcd(m, n)
print(f'Uoc so lon nhat (GCD) cua {m} va {n}: {gcd_result}')
lcm_result = lcm(m, n)
print(f'Boi sp nho nhat (LCM) cua {m} va {n}: {lcm_result}')
#Q3
def decimal_to_binary(n):
    return bin(n).replace('0b', '')
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
def reverse_number(n):
    return int(str(n)[::-1])
#1
while True:
    try:
        n = int(input('Nhap 1 so nguyen: '))
        break
    except ValueError:
        print('So vua nhap khong hop le')
#2
binary_representation = decimal_to_binary(n)
print(f'Bieu dien nhi phan cua {n}: {binary_representation}')
#3
n_for_sum = int(input('Nhap lai so:'))
digit_sum = sum_of_digits(n_for_sum)
print(f'Tong cac digits cua {n_for_sum}: {digit_sum}')
#4
reverse_n = reverse_number(n)
print(f'So dao nguoc cua {n}: {reverse_n}')
#Q4
def dao_nguoc(number):
    return str(number)==str(number)[::-1]
while True:
    try:
        m=int(input('Nhap 1 so m = '))
        n=int(input('Nhap 1 so n lon hon so vua nhap = '))
        if n>m:
            break
        else:
            print('2 so vua nhap khong hop le, hay thu lai')
    except ValueError:
        print('So khong hop le')
print(f'Cac so palindrome trong khoang[{m},{n}] la ')
for i in range(m, n+1):
    if dao_nguoc(i):
        print(i) 


               
          
     
