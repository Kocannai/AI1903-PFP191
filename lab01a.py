#1
number1 = 20
number2 = 30
number3 = 30
number4 = 40
x=number1*number2
y=number3+number4
print(x)
print(y)
#2
for i in range(10):
    if i == 0:
        current_number = i
        previous_number = 0
    else:
        current_number = i
        previous_number = i-1
        Sum=current_number+previous_number
        print(f"Current number: {current_number}, Previous number: {previous_number}, Sum: {Sum}")
#3
print("Name", "Is", "James", sep="**")
#4
decimal_number = 8
print(f"The octal number of decimal number {decimal_number} is 10")
#5
float_number = 458.541315
formatted_float = f"{float_number:.2f}"
print("The float number with 2 decimal places is:", formatted_float)




