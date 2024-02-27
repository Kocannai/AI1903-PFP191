#Question 1

#1

a=[1, 2, 3]
b=[]
c=[1.0, 'Jessa', 3]
print(a)
print(c)
print(b)

#2

list1 = ['M', 'na', 'i', 'Ke']
list2 = ['y', 'me', 's', 'lly']

list3 = []
for i, j in zip(list1, list2):
    list3.append(f'{i}{j}')
print(list3)

#Question 2

#1
n=[]
numbers=[1,2,3,4,5,6,7]
for i in numbers:
    x=i**2
    n.append(x)
print(n)

#2

list4 = ['Hello', 'take']
list5 = ['Dear', 'Sir']

list6 = []
for m in list4:
    for k in list5:
        list6.append(f'{m} {k}')
print(list6)

#Question 3

#1

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)

#2

sampleDict = {
    'class': {
        'student': {
            'name': 'Mike',
            'marks': {
                'physics': 70,
                'history': 80
            }
        }
    }
}

print(sampleDict['class']['student']['marks']['history'])

#3

employees = ['Kelly', 'Emma']
defaults = {'designation': 'Developer', 'salary': 8000}
result=dict.fromkeys(employees, defaults)
print(result)

#Question 4

#1

tuple1 = ('Orange', [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])

#2

tuple1 = (10, 20, 30, 40)
a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)

#3

tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple1)
print(tuple2)

#Question 5

str1 = 'hello,world!'
all_freq = {}

for i in str1:
    if i.isalpha():
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
            
with open('output.txt','w') as file1:
    for letter, count in sorted(all_freq.items()):
        file1.write(f"{letter}: {count}\n")
        
#Question 6
        
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def sequential_search(arr, key):
    for i, num in enumerate(arr):
        if num == key:
            return i
    return -1

def binary_search_recursive(arr, key, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search_recursive(arr, key, low, mid - 1)
    else:
        return binary_search_recursive(arr, key, mid + 1, high)

def binary_search_iterative(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def main():
    n = int(input('Enter the number of integers: '))
    if n < 1 or n > 100:
        print('Please enter a number between 1 and 100.')
        return

    arr = []
    for i in range(n):
        num = int(input(f'Enter number {i+1}: '))
        arr.append(num)

    selection_sort(arr)
    print('Sorted list:', arr)

    key = int(input('Enter the key to search: '))

    index = sequential_search(arr, key)
    if index != -1:
        print(f'Found key at position {index} in the list.')
    else:
        print('Not Found! (Sequential Search)')

    index = binary_search_recursive(arr, key, 0, len(arr)-1)
    if index != -1:
        print(f'Found key at position {index} in the list. (Binary Search - Recursive)')
    else:
        print('Not Found! (Binary Search - Recursive)')

    index = binary_search_iterative(arr, key)
    if index != -1:
        print(f'Found key at position {index} in the list. (Binary Search - Iterative)')
    else:
        print('Not Found! (Binary Search - Iterative)')

if __name__ == "__main__":
    main()






















    