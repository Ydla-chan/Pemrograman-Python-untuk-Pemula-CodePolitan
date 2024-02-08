# Program Maangement Kontak
import function

# List Of Dictionary
daftar_kontak = []


# Menu program
while True:
    print("Menu")
    print("1. Daftar Kontak")
    print("2. Tambah kontak ")
    print("3. Hapus Kontak ")
    print("4. Cari Kontak ")
    print("0. Keluar ")

    menu = input("Pilih menu : ")

    if menu == "0":
        break
    elif menu == "1":
        function.display_kontak(daftar_kontak)
    elif menu =="2":
        daftar_kontak.append((function.new_kontak()))
    elif menu == "3":
        function.hapus_kontak(daftar_kontak)
    elif menu == "4" :
        function.cari_kontak(daftar_kontak)
    else:
        print("Program tidak tersedia ")

print("Progam Selesai dijalankan , sampai jumpa lagi ")