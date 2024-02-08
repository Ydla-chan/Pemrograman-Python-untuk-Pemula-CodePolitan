def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("=============")
        print(f"Nama    : {kontak['nama']} ")
        print(f"Email   : {kontak['email']} ")
        print(f"No.Telp : {kontak['notelp']} ")

def new_kontak():
    nama  = input("Masukan Nama : ")
    email  = input("Masukan email : ")
    notelp = input("Masukan notelp : ")
    kontak = {
        "nama"   : nama,
        "email"  : email,
        "notelp" : notelp
    }
    return kontak

def hapus_kontak(daftar_kontak):
    telepon = input("No Telepon yang akan di hapus : ")

    index = -1

    for i in range(len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if telepon == kontak["notelp"]:
            index = i
            break

    if index == -1:
        print("Data tidak ditemukan ")
    else:
        del daftar_kontak[index]
        print("Kontak berhasil dihapus")

def cari_kontak(daftar_kontak):
    namaFind = input("Nama yang di cari : ")

    for kontak in daftar_kontak:
        nama = kontak["nama"]
        if nama.lower().find(namaFind.lower()) != -1:
            print("=============")
            print(f"Nama    : {kontak['nama']} ")
            print(f"Email   : {kontak['email']} ")
            print(f"No.Telp : {kontak['notelp']} ")
