Day_so = input("Nhap vao 1 day so: ")
Cac_so = [float(x) for x in Day_so.split()]
N = list(set(Cac_so))
print(N)
