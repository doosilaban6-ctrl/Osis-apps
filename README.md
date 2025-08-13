
# 🚀 Sistem Informasi OSIS
### Aplikasi Web Modern untuk Manajemen Anggota

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3-black.svg)
![Database](https://img.shields.io/badge/Database-SQLite-green.svg)

Aplikasi ini adalah solusi modern untuk mengelola data anggota, jadwal, dan administrasi organisasi OSIS. Dibangun dengan framework **Flask**, aplikasi ini menawarkan antarmuka pengguna yang bersih, fungsionalitas lengkap, dan pengalaman yang mudah digunakan.

---

## ✨ Fitur Unggulan

-   **Autentikasi Pengguna:** Sistem login dan registrasi yang aman untuk administrator.
-   **Dashboard Interaktif:** Halaman utama yang intuitif dengan navigasi cepat.
-   **Manajemen Anggota:**
    -   **Pencarian Canggih:** Temukan anggota dengan cepat berdasarkan nama, jabatan, atau kelas.
    -   **Tambah Anggota:** Formulir khusus untuk mendaftarkan anggota baru dengan mudah.
    -   **Edit Anggota:** Perbarui data anggota yang sudah ada dengan beberapa klik.
-   **Tampilan Modern:** Desain antarmuka yang minimalis, responsif, dan nyaman di mata.

---

## 🛠️ Instalasi dan Persiapan

Berikut adalah langkah-langkah untuk menjalankan aplikasi di lingkungan lokal Anda.

### 1. Prasyarat

Pastikan Anda sudah menginstal **Python 3.11** atau versi yang lebih baru, serta **pip**.

### 2. Jalankan Perintah

```bash
# Klon repositori (jika Anda menggunakan Git)
git clone [URL-REPOSITORY-ANDA]
cd osis-app

# Buat dan aktifkan virtual environment
python3 -m venv venv
source venv/bin/activate

# Instal semua library yang dibutuhkan
pip install Flask Flask-SQLAlchemy Flask-Login Werkzeug


🚀 Cara Penggunaan
  1. Jalankan Aplikasi:

  Bash
  python3 app.py


 
 Buka browser Anda dan kunjungi http://127.0.0.1:5000.

 Login sebagai Admin:

 Gunakan akun admin default: Username: admin | Password: admin123.

 Kelola Anggota:

 Klik tombol "Kelola Anggota OSIS" di dashboard untuk melihat daftar.

 Gunakan kolom pencarian untuk mencari anggota tertentu.

 Klik tombol "Tambah Anggota" untuk mendaftarkan anggota baru.

 Klik tombol "Edit Anggota" di setiap kartu anggota untuk mengubah datanya.

 📂 Struktur Proyek
.
├── venv/                 # Virtual environment
├── static/
│   └── css/
│       └── style.css     # File CSS untuk tampilan modern
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── anggota.html
│   ├── edit_anggota.html # Form untuk mengedit data anggota
│   └── tambah_anggota.html # Form untuk menambah data anggota
├── app.py                # Logika utama aplikasi
├── models.py             # Definisi model database
└── README.md             # File dokumentasi proyek
