# === komik.py ===
import csv

FILE_KOMIK = 'file_data/komik.csv'

# Membaca data komik dari CSV dan mengembalikan sebagai dictionary

def load_komik():
    komik_map = {}
    try:
        with open(FILE_KOMIK, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                komik_map[row['id']] = {
                    'judul': row['judul'],
                    'pengarang': row['pengarang'],
                    'harga': int(row['harga']),
                    'stok': int(row['stok'])
                }
    except FileNotFoundError:
        pass
    return komik_map

# Menyimpan data komik ke file CSV

def simpan_komik(komik_map):
    with open(FILE_KOMIK, mode='w', newline='') as file:
        fieldnames = ['id', 'judul', 'pengarang', 'harga', 'stok']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for id, data in komik_map.items():
            writer.writerow({
                'id': id,
                'judul': data['judul'],
                'pengarang': data['pengarang'],
                'harga': data['harga'],
                'stok': data['stok']
            })

# Tambah komik

def tambah_komik(komik_map):
    id = input("ID Komik: ")
    if id in komik_map:
        print("❌ ID sudah ada.")
        return
    judul = input("Judul Komik: ")
    pengarang = input("Pengarang: ")
    harga = int(input("Harga: "))
    stok = int(input("Stok: "))
    komik_map[id] = {
        'judul': judul,
        'pengarang': pengarang,
        'harga': harga,
        'stok': stok
    }
    print("✅ Komik berhasil ditambahkan.")

# Tampilkan semua komik

def tampilkan_komik(komik_map):
    if not komik_map:
        print("(Data komik kosong)")
        return
    print("\n=== Daftar Komik ===")
    for id, data in komik_map.items():
        print(f"{id} | {data['judul']} | {data['pengarang']} | Rp{data['harga']} | Stok: {data['stok']}")

# Edit komik

def edit_komik(komik_map):
    id = input("Masukkan ID Komik yang ingin diedit: ")
    if id not in komik_map:
        print("❌ Komik tidak ditemukan.")
        return
    print("(Tekan Enter untuk melewati perubahan)")
    data = komik_map[id]
    judul = input(f"Judul [{data['judul']}]: ") or data['judul']
    pengarang = input(f"Pengarang [{data['pengarang']}]: ") or data['pengarang']
    harga = input(f"Harga [{data['harga']}]: ") or data['harga']
    stok = input(f"Stok [{data['stok']}]: ") or data['stok']
    komik_map[id] = {
        'judul': judul,
        'pengarang': pengarang,
        'harga': int(harga),
        'stok': int(stok)
    }
    print("✅ Data komik berhasil diperbarui.")

# Hapus komik

def hapus_komik(komik_map):
    id = input("Masukkan ID Komik yang ingin dihapus: ")
    if id in komik_map:
        del komik_map[id]
        print("✅ Komik berhasil dihapus.")
    else:
        print("❌ Komik tidak ditemukan.")
