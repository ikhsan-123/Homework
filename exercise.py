stok = []
def tambah():
    nama_barang = input("Masukkan nama barang : ")
    stok_barang = input("Masukkan stok barang : ")
    barang = {"nama" : nama_barang, "stok" : stok_barang}
    stok.append(barang)
    return "--- Data berhasil ditambahkan ---"

def edit():
    nama = input('Masukkan barang yang ingin diubah: ')
    if nama not in stok:
        print(f'Barang {nama} tidak tersedia')
        return

    print(f"List Barang Saat Ini '{nama}':")
    print(f"\tJumlah: {stok[nama][0]}")

    pilihan = input('Pilihan Ubah\n1. Jumlah\n2. Batal')
    if pilihan == 1:
        jumlah = int(input('Masukkan Jumlah: '))
        stok[nama][0] = jumlah
        print(f'Jumlah {nama} telah diubah')
    elif pilihan == 2:
        exit
  
def hapus():
    delete = int(input("Hapus data index ke : "))
    delete -= 1
    del stok[delete]
    return "--- Data berhasil dihapus ---"
def search():
    lihat = input('Cari Barang: ')
    if lihat in stok:
        print(f'Barang {lihat} tersedia {stok[lihat]} pcs')
    else:
        print(f'Barang {lihat} tidak tersedia')
def tampil():
    print("--- Data barang ---")
    number = 1
    for i in stok:
        print(f"{number}. {i["nama"]} , Stok : {i["stok"]}")
        number += 1
    return ""
def view_item_cout():
    if not stok:
        print('Tidak ada data')
        return
    print(f"List Barang Saat Ini:")
    for nama,data in stok.items():
        kuantitas = data
        print(f'{nama}: ')
        print(f'\tJumlah: {kuantitas}')