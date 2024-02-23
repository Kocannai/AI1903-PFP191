#Q1

#1

def print_file(file_name):
    with open(file_name,'r') as file:
        for line in file:
            print(line.strip())

print_file('poem.txt')

#2

def count_line(file_name):
    count=0
    with open(file_name,'r') as file:
        for line in file:
            if not line.strip().startswith('T'):
                count+=1
    return count
result=count_line('story.txt')
print("No of lines not starting with 'T' = ", result)

#Q2

#1

def count_words(file_name):
        with open(file_name, 'r') as file:
            content = file.read()
            words = content.split()
            num_words = len(words)
            print('Total words are', num_words)
        
count_words('story.txt')

#2

def display_words(file_name):
        with open(file_name, 'r') as file:
            for line in file:
                words = line.split()
                for i in words:
                    if len(i) < 4:
                        print(i)

display_words('story.txt')

#Q3

#1

def count_uppercase(file_name):
    uppercase_count = 0
    try:
        with open(file_name, 'r') as file:
            for line in file:
                for char in line:
                    if char.isupper():
                        uppercase_count += 1
    except FileNotFoundError:
        print('File khong ton tai')
    return uppercase_count
result = count_uppercase('test1.txt')
print(result)


#2

def count_words1(file_name):
    count1 = 0
    try:
        with open(file_name, 'r') as file:
            for line in file:
                words = line.split()
                for i in words:
                    if i == 'this' or i == 'these':
                        count1 += 1
        return count1
    except FileNotFoundError:
        print('File khong ton tai')
result1 = count_words1('article.txt')
print(result1)

#Q4

#1

def hash_display(file_name):
        with open(file_name, 'r') as file:
            content = file.read()
            content1 = '#'.join(content)
            print(content1)

hash_display('matter.txt')

#2

def JTOI(file_name):
        with open(file_name, 'r') as file:
            content2 = file.read()
            content3 = content2.replace('J', 'I')
            print(content3)
            
JTOI('WORDS.TXT')









