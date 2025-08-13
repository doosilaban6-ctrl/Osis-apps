
i# Aplikasi Sistem Informasi OSIS

Sebuah aplikasi web sederhana untuk mengelola data anggota, jadwal kegiatan, dan administrasi OSIS. Aplikasi ini dibuat menggunakan framework Flask, Python, dan database SQLite.

---

## Fitur Aplikasi

- **Otentikasi Pengguna:** Sistem login dan registrasi untuk administrator.
- **Manajemen Anggota:** Fitur CRUD (Create, Read, Update, Delete) untuk mengelola data anggota OSIS.
- **Manajemen Kegiatan:** Fitur CRUD untuk mengelola jadwal dan detail kegiatan OSIS.

---

## Persiapan Lingkungan

Berikut adalah langkah-langkah untuk menjalankan aplikasi di lingkungan lokal Anda.

### Prasyarat

Pastikan Anda sudah menginstal **Python 3** dan **pip** (manajer paket Python).

### Instalasi

1.  **Clone repositori:**
    ```bash
    git clone [https://github.com/doosilaban6-ctrl/osis-app.git](https://github.com/doosilaban6-ctrl/osis-app.git)
    cd osis-app
    ```

2.  **Buat Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instal library yang dibutuhkan:**
    ```bash
    pip install Flask Flask-SQLAlchemy Flask-Login Werkzeug
    ```

---

## Menjalankan Aplikasi

Jalankan perintah berikut di terminal Anda:

```bash
python3 app.py
