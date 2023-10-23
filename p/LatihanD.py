#mulai
bil = int(input("Masukan Bilangan: "))
hasil = bil % 3
if hasil == 1:
    nilai = input(int("Masukan Nilai: "))
    r = hasil + nilai
    if r > 50:
        print(r)
    else:
        print("y")
else:
    print("x")
#selesai
