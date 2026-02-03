import json
import datetime

catatan = []

try:
    with open('catatan.json', 'r') as f:
        catatan = json.load(f)
except FileNotFoundError:
    pass

def tambah_catatan():
    mapel = input("Masukkan mapel: ")
    topik = input("Masukkan topik: ")
    durasi = int(input("Masukkan durasi belajar (menit): "))
    tanggal = datetime.date.today().isoformat()
    catatan.append({'mapel': mapel, 'topik': topik, 'durasi': durasi, 'tanggal': tanggal})
    print("Catatan berhasil ditambahkan!")

def lihat_catatan():
    if not catatan:
        print("Belum ada catatan belajar.")
    else:
        for i, c in enumerate(catatan, 1):
            print(f"\nCatatan {i}:")
            print(f"Mapel: {c['mapel']}")
            print(f"Topik: {c['topik']}")
            print(f"Durasi: {c['durasi']} menit")

def total_waktu():
    total = sum(c['durasi'] for c in catatan)
    print(f"Total waktu belajar: {total} menit")

def ringkasan_mingguan():
    today = datetime.date.today()
    current_week = today.isocalendar()[1]
    current_year = today.isocalendar()[0]
    mingguan_catatan = []
    for c in catatan:
        try:
            cat_date = datetime.date.fromisoformat(c['tanggal'])
            if cat_date.isocalendar()[:2] == (current_year, current_week):
                mingguan_catatan.append(c)
        except KeyError:
            pass  # Skip catatan lama tanpa tanggal
    if not mingguan_catatan:
        print("Belum ada catatan belajar minggu ini.")
    else:
        total_minggu = sum(c['durasi'] for c in mingguan_catatan)
        print(f"Ringkasan Mingguan (Minggu {current_week}, {current_year}):")
        print(f"Total waktu belajar: {total_minggu} menit")
        print(f"Jumlah catatan: {len(mingguan_catatan)}")

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Ringkasan Mingguan")
    print("5. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        ringkasan_mingguan()
    elif pilihan == "5":
        with open('catatan.json', 'w') as f:
            json.dump(catatan, f)
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")