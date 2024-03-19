#PT2
#Problem 1


def replace_chars(string, char1, char2):
    a = string.replace(char1, char2)
    return a
def main():
    b = input('Nhap vao 1 chuoi(khong co khoang trong): ')
    char1 = input('Chon ki tu bi thay the: ')
    char2 = input(f'Chon ki tu de thay the ki tu {char1}: ')

    res = replace_chars(b, char1, char2)
    print(res)

if __name__ == '__main__':
    main()
    
    
    
#Problem 2
    
import csv
import os

class Employee:
    def __init__(self, code, name, salary, allowance):
        self.code = code
        self.name = name
        self.salary = salary
        self.allowance = allowance

def add(code, name, salary, allowance):
    with open('input.txt', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([code, name, salary, allowance])
        
def binary_search(name):
    with open('input.txt', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        sorted_data = sorted(data[1:], key=lambda x: x[1])
        left = 0
        right = len(sorted_data) - 1
        while left <= right:
            mid = (left + right) // 2
            if sorted_data[mid][1] == name:
                return sorted_data[mid]
            elif sorted_data[mid][1] < name:
                left = mid + 1
            else:
                right = mid - 1
    return None

def remove(code):
    with open('input.txt', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    with open('input.txt', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            if row and row[0] == code:
                continue
            writer.writerow(row)

def sort_and_save():
    with open('input.txt', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        sorted_data = sorted(data[1:], key=lambda x: int(x[2]) + int(x[3]), reverse=True)
    with open('result.txt', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Code', 'Name', 'Salary', 'Allowance'])
        for row in sorted_data:
            writer.writerow(row)
    print('Data sorted and saved in result.txt')

def main():
    while True:
        print('1. Add Employee')
        print('2. Find Employee')
        print('3. Remove Employee')
        print('4. Print Sorted Data and save the result in result.txt file')
        print('5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            code = input('Enter employee code: ')
            name = input('Enter employee name: ')
            salary = input('Enter employee salary: ')
            allowance = input('Enter employee allowance: ')
            add(code, name, salary, allowance)
        elif choice == '2':
            name = input('Enter employee name to search: ')
            employee = binary_search(name)
            if employee:
                print('Employee found:')
                print('Code: ', employee[0])
                print('Name: ', employee[1])
                print('Salary: ', employee[2])
                print('Allowance: ', employee[3])
            else:
                print('Employee not found.')
        elif choice == '3':
            code = input('Enter employee code to remove: ')
            remove(code)
        elif choice == '4':
            sort_and_save()
        elif choice == '5':
            print('Exit!')
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()



#Problem 3
    
def kn(N, W, items):
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        weight_i, profit_i, name_i = items[i - 1]
        for w in range(1, W + 1):
            if weight_i <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight_i] + profit_i)
            else:
                dp[i][w] = dp[i - 1][w]
    result = dp[N][W]
    weight = W
    items_selected = []
    for i in range(N, 0, -1):
        if result <= 0:
            break
        if result == dp[i - 1][weight]:
            continue
        else:
            weight_i, profit_i, name_i = items[i - 1]
            items_selected.append((name_i, result // profit_i))
            result -= profit_i
            weight -= weight_i

    return dp[N][W], items_selected

def main():
    with open("BAG.INP", "r") as file:
        N, W = map(int, file.readline().strip().split())
        items = [list(map(int, line.strip().split())) for line in file]

    max_profit, items_selected = kn(N, W, items)

    print(max_profit)
    for item in items_selected:
        print(item[0], item[1])

if __name__ == "__main__":
    main()











