# Membuat Program menggunakan For-Loop , List dan range

banyak = int(input("Masukan Banyak data ? "))

nama = []
umur =[]

for i in range(0,banyak):
    print(f"data ke {i}")
    Input_nama = input("Masukan Nama ")
    Input_umur = int(input("Masukan Umur "))

    nama.append(Input_nama)
    umur.append(Input_umur)

for i in range(0,len(nama)):
    data_nama = nama[i]
    data_umur = umur[i]
    print(f"{data_nama} berumur {data_umur} tahuan")