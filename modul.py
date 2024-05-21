import exercise as mod

print("Selamat datang di program manajemen stock barang!")
print("Pilihan :")
print("1. Tambah data barang")
print("2. edit data")
print("3. Hapus data barang")
print("4. Tampilkan data barang")
print("5. Keluar")
print('\n')

while True:
    pilihan = int(input("Masukkan pilihan : "))
    print("=====================================")
    if pilihan == 1:
        print(mod.tambah())
        print("")
    elif pilihan == 2:
        print(mod.edit())
        print("")
    elif pilihan == 3:
        print(mod.hapus())
        print("")
    elif pilihan == 4:
        print(mod.search())
        print("")
    elif pilihan == 5:
        print(mod.tampil())
        print("")
    elif pilihan == 6:
        print(mod.view_item_cout)
    elif pilihan == 7:
        exit()