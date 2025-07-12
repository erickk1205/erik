# === main.py ===
from komik import *
from pembelian import *

queue = []  # antrean pembeli
komik_map = load_komik()  # hash map data komik

while True:
    print("\n=== SISTEM MANAJEMEN PEMBELIAN BUKU KOMIK ===")
    print("1. Tambah Data Komik")
    print("2. Lihat Daftar Komik")
    print("3. Edit Data Komik")
    print("4. Hapus Komik")
    print("5. Tambah ke Antrean Pembeli")
    print("6. Proses Antrean Pembelian")
    print("7. Lihat Antrean")
    print("8. Keluar")

    pilihan = input("Pilih menu (1-8): ")

    if pilihan == "1":
        tambah_komik(komik_map)
    elif pilihan == "2":
        tampilkan_komik(komik_map)
    elif pilihan == "3":
        edit_komik(komik_map)
    elif pilihan == "4":
        hapus_komik(komik_map)
    elif pilihan == "5":
        tambah_ke_antrean(queue)
    elif pilihan == "6":
        proses_pembelian(queue, komik_map)
    elif pilihan == "7":
        tampilkan_antrean(queue)
    elif pilihan == "8":
        simpan_komik(komik_map)
        print("\nTerima kasih telah menggunakan aplikasi!")
        break
    else:
        print("Pilihan tidak valid.")
