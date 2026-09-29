# Sistem Informasi Mahasiswa (SIM)

Aplikasi console-based untuk mengelola data mahasiswa
pada Program Studi Sistem Informasi.

## Identitas
- Nama: Fakhry Ahmad Fauzan
- NIM: 20241320038

## Fitur
- Tambah data mahasiswa (NIM, nama, prodi, angkatan, IPK)
- Tampilkan seluruh data dalam tabel
- Cari mahasiswa berdasarkan NIM
- Hapus data mahasiswa
- Edit IPK mahasiswa (validasi 0.0-4.0)
- Validasi data input

## Prasyarat
- Python 3.10+
- pip

## Instalasi
```bash
git clone https://github.com/USERNAME/sim-mahasiswa.git
cd sim-mahasiswa
python -m venv venv
venv\Scripts\Activate.ps1   # Windows PowerShell
source venv/bin/activate    # Linux/macOS
pip install -r requirements.txt
```

## Penggunaan
```bash
python -m src.main
```

## Pengujian
```bash
pytest tests/ -v
```

## Struktur Proyek
- src/models.py — Model data Mahasiswa
- src/main.py — Program utama & menu
- tests/ — Unit test
- docs/ — Dokumentasi & screenshot
