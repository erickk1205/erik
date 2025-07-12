# === pembelian.py ===
import csv

FILE_ANTRIAN = 'file_data/antrean_pembelian.csv'

# Tambah pembeli ke antrean

def tambah_ke_antrean(queue):
    print("\n=== Tambah ke Antrean Pembelian ===")
    nama = input("Nama Pembeli: ")
    id_komik = input("ID Komik: ")
    jumlah = int(input("Jumlah Pembelian: "))
    queue.append({
        'nama': nama,
        'id_komik': id_komik,
        'jumlah': jumlah
    })
    print("✅ Pembeli ditambahkan ke antrean.")

# Proses pembelian komik

def proses_pembelian(queue, komik_map):
    if not queue:
        print("(Antrean kosong)")
        return

    pembeli = queue.pop(0)  # FIFO
    id_komik = pembeli['id_komik']

    if id_komik not in komik_map:
        print("❌ ID Komik tidak ditemukan. Transaksi dibatalkan.")
        return

    komik = komik_map[id_komik]
    if pembeli['jumlah'] > komik['stok']:
        print("❌ Stok tidak mencukupi. Transaksi dibatalkan.")
        return

    komik['stok'] -= pembeli['jumlah']

    with open(FILE_ANTRIAN, mode='a', newline='') as file:
        fieldnames = ['nama_pembeli', 'id_komik', 'jumlah', 'judul_komik', 'harga_total']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow({
            'nama_pembeli': pembeli['nama'],
            'id_komik': id_komik,
            'jumlah': pembeli['jumlah'],
            'judul_komik': komik['judul'],
            'harga_total': komik['harga'] * pembeli['jumlah']
        })
    print(f"✅ Transaksi berhasil: {pembeli['nama']} membeli {pembeli['jumlah']}x {komik['judul']}")

# Tampilkan antrean

def tampilkan_antrean(queue):
    print("\n=== Daftar Antrean Pembeli ===")
    if not queue:
        print("(Tidak ada antrean)")
    else:
        for i, pembeli in enumerate(queue, 1):
            print(f"{i}. {pembeli['nama']} - ID Komik: {pembeli['id_komik']} x{pembeli['jumlah']}")
