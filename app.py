
import os
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from models import db, User, Anggota, Kegiatan

# Konfigurasi Aplikasi
app = Flask(__name__)
app.config['SECRET_KEY'] = 'kunci-rahasia-anda'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///osis.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inisialisasi Database
db.init_app(app)

# Konfigurasi Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Rute Halaman Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Login gagal. Periksa username dan password Anda.', 'error')
    
    return render_template('login.html')

# Rute Halaman Registrasi
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user_exist = User.query.filter_by(username=username).first()
        if user_exist:
            flash('Username sudah digunakan. Silakan pilih username lain.', 'error')
        else:
            new_user = User(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registrasi berhasil! Silakan login.', 'success')
            return redirect(url_for('login'))
    
    return render_template('register.html')

# Rute Halaman Dashboard
@app.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html')

# Rute Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# --- Manajemen Anggota ---
@app.route('/anggota')
@login_required
def daftar_anggota():
    anggota_list = Anggota.query.all()
    return render_template('anggota.html', anggota_list=anggota_list)

@app.route('/anggota/tambah', methods=['POST'])
@login_required
def tambah_anggota():
    nama = request.form.get('nama')
    jabatan = request.form.get('jabatan')
    kelas = request.form.get('kelas')
    
    if nama and jabatan and kelas:
        anggota_baru = Anggota(nama=nama, jabatan=jabatan, kelas=kelas)
        db.session.add(anggota_baru)
        db.session.commit()
        flash('Data anggota berhasil ditambahkan.', 'success')
    else:
        flash('Semua kolom harus diisi.', 'error')
        
    return redirect(url_for('daftar_anggota'))

@app.route('/anggota/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_anggota(id):
    anggota = Anggota.query.get_or_404(id)
    if request.method == 'POST':
        anggota.nama = request.form.get('nama')
        anggota.jabatan = request.form.get('jabatan')
        anggota.kelas = request.form.get('kelas')
        db.session.commit()
        flash('Data anggota berhasil diperbarui.', 'success')
        return redirect(url_for('daftar_anggota'))
    
    return render_template('edit_anggota.html', anggota=anggota)

@app.route('/anggota/hapus/<int:id>', methods=['POST'])
@login_required
def hapus_anggota(id):
    anggota = Anggota.query.get_or_404(id)
    db.session.delete(anggota)
    db.session.commit()
    flash('Data anggota berhasil dihapus.', 'success')
    return redirect(url_for('daftar_anggota'))

# --- Manajemen Kegiatan ---
@app.route('/kegiatan')
@login_required
def daftar_kegiatan():
    kegiatan_list = Kegiatan.query.all()
    return render_template('kegiatan.html', kegiatan_list=kegiatan_list)

@app.route('/kegiatan/tambah', methods=['POST'])
@login_required
def tambah_kegiatan():
    nama_kegiatan = request.form.get('nama_kegiatan')
    tanggal = request.form.get('tanggal')
    lokasi = request.form.get('lokasi')
    deskripsi = request.form.get('deskripsi')
    
    if nama_kegiatan and tanggal and lokasi:
        kegiatan_baru = Kegiatan(
            nama_kegiatan=nama_kegiatan,
            tanggal=tanggal,
            lokasi=lokasi,
            deskripsi=deskripsi
        )
        db.session.add(kegiatan_baru)
        db.session.commit()
        flash('Kegiatan berhasil ditambahkan.', 'success')
    else:
        flash('Nama, tanggal, dan lokasi kegiatan harus diisi.', 'error')
        
    return redirect(url_for('daftar_kegiatan'))

@app.route('/kegiatan/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_kegiatan(id):
    kegiatan = Kegiatan.query.get_or_404(id)
    if request.method == 'POST':
        kegiatan.nama_kegiatan = request.form.get('nama_kegiatan')
        kegiatan.tanggal = request.form.get('tanggal')
        kegiatan.lokasi = request.form.get('lokasi')
        kegiatan.deskripsi = request.form.get('deskripsi')
        db.session.commit()
        flash('Data kegiatan berhasil diperbarui.', 'success')
        return redirect(url_for('daftar_kegiatan'))
    
    return render_template('edit_kegiatan.html', kegiatan=kegiatan)

@app.route('/kegiatan/hapus/<int:id>', methods=['POST'])
@login_required
def hapus_kegiatan(id):
    kegiatan = Kegiatan.query.get_or_404(id)
    db.session.delete(kegiatan)
    db.session.commit()
    flash('Data kegiatan berhasil dihapus.', 'success')
    return redirect(url_for('daftar_kegiatan'))

# Fungsi untuk membuat admin pertama kali (jalankan hanya sekali!)
def create_first_admin():
    with app.app_context():
        db.create_all()

        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin')
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print('Admin pertama berhasil dibuat. Username: admin, Password: admin123')

# Jalankan Aplikasi
if __name__ == '__main__':
    create_first_admin()
    app.run(debug=True)
