from statistics import mean

data_siswa = [
    {"id": 1, 
    "nama": "Khoirul azam",  
    "nilai": 92,
    "grade": "A"
    },

    {"id": 2, 
    "nama": "M. Hafiz i",  
     "nilai": 78,
     "grade": "B"
    },
    
    {"id": 3, 
    "nama": "Azriel ataya", 
     "nilai": 65,
     "grade": "C"},

    {"id": 4, 
    "nama": "M. hikam",  
     "nilai": 50,
     "grade": "D"},

    {"id": 5, 
    "nama": "Ibnu hasan",   
     "nilai": 88,
     "grade": "A"},

    {"id": 6, 
    "nama": "Miftah akhdani.p", 
     "nilai": 73,
     "grade": "B"},

    {"id": 7, 
    "nama": "Iffat Arrayan",  
     "nilai": 45,
     "grade": "E"},

    {"id": 8, 
    "nama": "M. Rapli",
     "nilai": 30,
     "grade": "E"},
]

def tampilkan_menu():
    print("\n===== DATA NILAI SISWA =====")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Data")
    print("4. Hitung Rata-rata Kelas")
    print("5. Keluar")

def tampilkan_sub_menu():
    print("\n--- TAMPILKAN DATA ---")
    print("1. Tampilkan Semua Data")
    print("2. Tampilkan Nama Siswa")
    print("3. Tampilkan Nilai Siswa")
    print("4. Cari Siswa")
    print("5. Kembali")

def tambah_data():
    print("\n--- Tambah Data Siswa ---")

    nama = input("Nama siswa: ")
    nilai = round(input("Nilai (0-100): "))

    if nilai < 0 or nilai > 100:
        print("Nilai harus antara 0-100!")
        return

    if nilai >= 90:
        grade = "A"
    elif nilai >= 80:
        grade = "B"
    elif nilai >= 70:
        grade = "C"
    elif nilai >= 60:
        grade = "D"
    else:
        grade = "E"

    new_id = len(data_siswa) + 1

    data_siswa.append({
        "id": new_id,
        "nama": nama,
        "nilai": nilai,
        "grade": grade
    })

    print("Data berhasil ditambahkan!")

def hapus_data():
    print("\n--- Hapus Data Siswa ---")

    nama = input("Masukkan nama siswa: ")

    for siswa in data_siswa:
        if siswa["nama"].lower() == nama.lower():
            data_siswa.remove(siswa)
            print("Data berhasil dihapus!")
            return

    print("Siswa tidak ditemukan!")

def tampilkan_semua():
    if not data_siswa:
        print("\nBelum ada data siswa.")
        return
    
    print("\n--- Daftar Nilai Siswa ---")
    for siswa in data_siswa:
        print(f"{siswa['id']}. {siswa['nama']} - NIlai: {siswa['nilai']} - grade: {siswa['grade']}")

def tampilkan_nama():
    if not data_siswa:
        print("\nBelum ada data siswa.")
        return
    
    print("\n--- Nama Siswa ---")
    for siswa in data_siswa:
        print(f"{siswa['id']}. {siswa['nama']}")

def tampilkan_nilai():
    if not data_siswa:
        print("\nBelum ada data siswa.")
        return
    
    print("\n--- Nama Siswa ---")
    for siswa in data_siswa:
        print(f"{siswa['id']}. NIlai: {siswa['nilai']} - grade: {siswa['grade']}")

def hitung_rata_rata():
    if not data_siswa:
        print("Tidak ada data untuk dihitung.")
        return

    daftar_nilai = [siswa['nilai'] for siswa in data_siswa]
    rata_rata = mean(daftar_nilai)
    
    print(f"\n Rata-rata nilai kelas: {round(rata_rata, 2)}")
    print(f" Jumlah siswa: {len(data_siswa)} orang")

def cari_siswa():
    if not data_siswa:
        print("Tidak ada data.")
        return
    
    keyword = input("Masukkan nama yang dicari: ").lower()
    found = False
    for siswa in data_siswa:
        if keyword in siswa['nama'].lower():
            print(f"{siswa['id']}. {siswa['nama']} - NIlai: {siswa['nilai']} - grade: {siswa['grade']}")
            found = True
    if not found:
        print("Siswa tidak ditemukan.")

def secondary():
    while True:
        tampilkan_sub_menu()
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            tampilkan_semua()
            break
        elif pilihan == '2':
            tampilkan_nama()
            break
        elif pilihan == '3':
            tampilkan_nilai()
            break
        elif pilihan == '4':
            cari_siswa()
            break
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid!")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            tambah_data()
        elif pilihan == '2':
            hapus_data()
        elif pilihan == '3':
            secondary()
        elif pilihan == '4':
            hitung_rata_rata()
        elif pilihan == '5':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")

main()
