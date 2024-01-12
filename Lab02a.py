#Q3
#1
def func1(*n):
    print('Printing values')
    for x in n:
        print(x)
func1(20,40,60)
func1(80,100)
#2
def calculation(a, b):
    add=a+b
    minus=a-b
    return add, minus
res=calculation(40, 10)
print(res)
#Q2
#1
def showEmployee(Name, Salary, x="Name:", y="salary:"):
    print(f"{x} {Name} {y} {Salary}")
showEmployee('Ben', '12000')
showEmployee('Jessa', '9000')
#2
def outer_fun(a, b):
    def inner_fun():
        x=a+b
        return x
    addition_result = inner_fun()
    final_result = addition_result + 5
    return final_result
result = outer_fun(3, 7)
print(result)
#Q3
#1
def sum(i):
    if i==0:
        return 0
    else:
        return i+sum(i-1)
result=sum(10)
print('Tong tu 0 den 10 la', result)
#2
def display_student(name, age):
    print(name, age)
show_student=display_student
display_student('Emma', 26)
show_student('Emma', 26)
#Q4
#1
def palindrome(n):
    number_str=str(n)
    reverse_number=number_str[::-1]
    return reverse_number==number_str
number=int(input('Nhap so:'))
if palindrome(number):
    print(f'{number} is palindrome number')
else:
    print(f'{number} is not palindrome number')
#2
x=(4, 6, 8, 24, 12, 2)
n=max(x)
print(n)







