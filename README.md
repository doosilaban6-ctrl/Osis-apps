
# 📋 Todo List App

## 1. 🎯 Tujuan Aplikasi
Aplikasi **Todo List App** ini dibuat untuk membantu pengguna dalam:
- Mencatat daftar tugas yang harus diselesaikan.
- Mengelola pekerjaan agar lebih teratur dan efisien.
- Memberikan pengingat visual untuk setiap tugas.

---

## 2. 🛠 Tech Stack
Aplikasi ini dibangun menggunakan:
- **Backend**: Python 3, Flask
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite
- **Template Engine**: Jinja2

---

## 3. ✨ Fitur-fitur

### **Functional Requirements**
1. **Menambahkan tugas** dengan judul dan deskripsi.
2. **Mengedit tugas** yang sudah ada.
3. **Menghapus tugas** dari daftar.
4. **Menandai tugas sebagai selesai**.
5. **Menyimpan data** secara permanen di database.

### **Non-Functional Requirements**
1. **User Friendly** — Tampilan sederhana dan mudah digunakan.
2. **Responsive** — Bisa diakses dari perangkat desktop maupun mobile.
3. **Ringan** — Waktu load cepat, tidak membebani memori.
4. **Maintainable** — Struktur kode rapi dan mudah dikembangkan.

---

## 4. 📦 Cara Instalasi

### 1️⃣ Clone Repository
```bash
git clone https://github.com/username/todolistapp.git
cd todolistapp


# Aplikasi Sistem Informasi OSIS

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

1.  **Clone repositori:** Jika Anda menggunakan Git.
    ```bash
    git clone [https://github.com/nama-pengguna/osis-app.git](https://github.com/nama-pengguna/osis-app.git)
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
    *(atau menggunakan file requirements.txt jika ada: `pip install -r requirements.txt`)*

---

## Menjalankan Aplikasi

Jalankan perintah berikut di terminal Anda:

```bash
python3 app.py
 eabeeaf (Initial commit of the OSIS web app)
