def check_user_input(input):
    try:
        ValueError = int(input)
    except ValueError:
        print('Error')
a = input("Nhap diem: ")
check_user_input(a)
a = float(input("Nhap Diem: "))
if 8.5 <= a <= 10:
    print("Điểm chữ: A Điểm hệ 4 : 4")
elif 7.0 <= a <= 8.4:
    print("Điểm chữ: B - Điểm hệ 4 : 3")
elif 5.5 <= a <= 6.9:
    print("Điểm chữ: C - Điểm hệ 4 : 2")
elif 4.0 <= a <= 5.4:
    print("Điểm chữ: D - Điểm hệ 4 : 1")
else:
    print("Điểm chữ: F - Điểm hệ 4 : 0")