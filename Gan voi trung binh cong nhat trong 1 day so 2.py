Day_so = input("Nhap vao 1 day so: ")
Cac_so = [float(x) for x in Day_so.split()]
if not Cac_so:
    print("Danh sach rong.")
else:
    Tong = sum(Cac_so)
    Avg = Tong/len(Cac_so)
    So_gan_nhat = Cac_so[0]
    for i in Cac_so[1:]:
        if abs(i - Avg) < abs(So_gan_nhat - Avg):
            So_gan_nhat = i
    print(f"So gan voi gia tri trung binh trong day so nhat la: {So_gan_nhat}")