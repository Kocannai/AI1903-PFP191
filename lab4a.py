#Q1
#1

file=open('sales.txt','w')
file.close()

#2

from datetime import datetime
x = datetime.now().strftime('%d-%m-%Y')
y = datetime.now().strftime('%d-%m-%Y-%H-%M-%S')
str_current_date = str(x)
str_current_datetime = str(y)
file_name1 = str_current_date+'.txt'
file_name2 = str_current_datetime+'.txt'
file_name3 = r'E:\download\\'+str_current_datetime+'.txt'
file1 = open(file_name1, 'w')
file2 = open(file_name2, 'w')
file3 = open(file_name3, 'w')
print('created', file1.name)
print('created', file2.name)
print('created', file3.name)
file1.close()
file2.close()
file3.close()

#3

import os
file_path = r'E:\download\sample.txt'
os.umask(0)
with open(os.open(file_path, os.O_CREAT|os.O_WRONLY, 0o777), 'w') as fh:
    fh.write('XD')
    
#Q2
#1

f=open('file1.txt','w')
with open('file1.txt', 'w') as file:
    file.write('Done Writing')
f.close()
f=open('file1.txt','r')
print(f.read())
f.close()

f=open('file1.txt','w')
with open('file1.txt', 'w') as file:
    file.write('This is new content')
f.close()
f=open('file1.txt','r')
print(f.read())
f.close()

#2

print('Opening file again..')
f=open('file1.txt','w')
with open('file1.txt', 'w') as file:
    file.write('This is overwritten content')
f.close()
f=open('file1.txt','r')
print(f.read())
f.close()

#3

list1=['Name: Emma', 'Address: 221 Baker Street', 'City: London']
with open('file1.txt', 'w') as file:
    for i in list1:
        file.write('%s\n'%i)
f.close()
f=open('file1.txt','r')
print(f.read())
f.close()

#Q3
#1

f1=open('test.txt','a')
with open('test.txt', 'w+') as fil:
    fil.write('My First Line\n')
    fil.write('My Second Line')
    fil.seek(0)


#2

with open('test.txt', 'r+') as fil:
    fil.seek(0,2)
    fil.write('\nThis content is added to the end of the file')
    fil.seek(0)
    print(fil.read())
    
#3
    
with open('test.txt', 'rb') as fil:
    fil.seek(3)
    print(fil.read(5).decode('utf-8'))
    fil.seek(10, 1)
    print(fil.read(6).decode('utf-8'))
    
#4
    
with open('test.txt', 'rb') as fil:
    fil.seek(-75, 2)
    print(fil.read(8).decode('utf-8'))
    
    fil.seek(-72, 2)
    print(fil.read(10).decode('utf-8'))
    
#5
    
with open('test.txt', 'r+') as fil:
    fil.seek(0, 2)
    print('file handle at:', fil.tell())

    fil.write('\nDemonstrating tell')

    print('file handle at:', fil.tell())

    fil.seek(0)
    print('file handle at:', fil.tell())
    
    print('***Printing File Content***')
    print(fil.read())
    print('***Done***')

    print('file handle at:', fil.tell())
    
#Q4
    
#1
    
import os

old_name = r'E:\download\details.txt'
new_name = r'E:\download\new_details.txt'

if os.path.isfile(new_name):
    print("File name already exists. Cannot rename")
else:
    os.rename(old_name, new_name)

#2
    
import os

folder = r'E:\download\\'
count = 1
for file_name in os.listdir(folder):
    source = folder + file_name
    destination = folder + "sales_" + str(count) + ".txt"
    os.rename(source, destination)
    count += 1
print('All Files Renamed')
print('New Names are')
res = os.listdir(folder)
print(res)

#3

import os

files_to_rename = ['sales_1.txt', 'sales_4.txt']
folder = r"E:\download\\"

for file in os.listdir(folder):
    if file in files_to_rename:
        old_name = os.path.join(folder, file)
        only_name = os.path.splitext(file)[0]
        new_base = only_name + '_new' + '.txt'
        new_name = os.path.join(folder, new_base)
        os.rename(old_name, new_name)
res = os.listdir(folder)
print(res)

#4

import os
from datetime import datetime
current_timestamp = datetime.today().strftime('%d-%b-%Y')
old_name = r"E:\download\sales.txt"
new_name = r"E:\download\sales" + current_timestamp + ".txt"
os.rename(old_name, new_name)

#5

import os

folder = r"E:\download\\"
print('Before rename')
files = os.listdir(folder)
print(files)
for file_name in files:
    old_name = os.path.join(folder, file_name)
    new_name = old_name.replace('.txt', '.pdf')
    os.rename(old_name, new_name)
print('After rename')
print(os.listdir(folder))

#6

import glob
import os

old_folder = r"E:\download\\"
new_folder = r"E:\download\\"

old_name = old_folder + "expense.txt"
new_name = new_folder + "expense.txt"

os.rename(old_name, new_name)




    
    









