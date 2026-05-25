# Aplikasi Data Nilai Siswa

Program sederhana berbasis Python untuk mengelola data nilai siswa menggunakan terminal/CLI (Command Line Interface).

---

## Fitur

- Menambah data siswa
- Menghapus data siswa
- Menampilkan seluruh data siswa
- Menampilkan nama siswa
- Menampilkan nilai siswa
- Menampilkan nilai terbesar siswa
- Menampilkan nilai terkecil siswa
- Mencari siswa berdasarkan nama
- Menghitung rata-rata nilai kelas

---

## Teknologi

- Python 3
- Module `statistics`

---

## Struktur Data

Setiap data siswa disimpan dalam bentuk dictionary:

```python
{
    "id": 1,
    "nama": "Khoirul azam",
    "nilai": 92,
    "grade": "A"
}
```

---

## Menu Program

```text
===== DATA NILAI SISWA =====
1. Tambah Data
2. Hapus Data
3. Tampilkan Data
4. Hitung Rata-rata Kelas
5. Keluar
```

---

## Sub Menu Tampilkan Data

```text
--- TAMPILKAN DATA ---
1. Tampilkan Semua Data
2. Tampilkan Nama Siswa
3. Tampilkan Nilai Siswa
4. Tampilkan Nilai Terbesar Siswa
5. Tampilkan Nilai Terkecil Siswa
6. Cari Siswa
7. Kembali
```

---

## Cara Menjalankan Program

1. Pastikan Python sudah terinstall
2. Simpan file dengan nama `main.py`
3. Jalankan program menggunakan terminal:

```bash
python main.py
```

---

## Contoh Output

```text
--- Daftar Nilai Siswa ---
1. Khoirul azam - Nilai: 92 - Grade: A
2. M. Hafiz i - Nilai: 78 - Grade: B
```

### Contoh Nilai Terbesar

```text
--- Nilai Terbesar ---
1. Khoirul azam - Nilai: 92 - Grade: A
```

### Contoh Nilai Terkecil

```text
--- Nilai Terkecil ---
8. M. Rapli - Nilai: 30 - Grade: E
```

---

## Konsep Python yang Digunakan

- List
- Dictionary
- Function
- Looping
- Conditional (`if`, `elif`, `else`)
- Operator Perbandingan
- Import Module
- List Comprehension

---

## Author

Ananda Satria