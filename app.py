import os
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from models import db, User, Anggota
from werkzeug.security import generate_password_hash, check_password_hash

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
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username sudah digunakan. Silakan pilih yang lain.', 'error')
            return redirect(url_for('register'))
            
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

# Rute Halaman Manajemen Anggota (Termasuk Pencarian)
@app.route('/anggota', methods=['GET'])
@login_required
def anggota():
    search_query = request.args.get('q')
    if search_query:
        anggota_list = Anggota.query.filter(
            Anggota.nama.like(f'%{search_query}%') |
            Anggota.jabatan.like(f'%{search_query}%') |
            Anggota.kelas.like(f'%{search_query}%')
        ).all()
    else:
        anggota_list = Anggota.query.all()
    
    return render_template('anggota.html', anggota_list=anggota_list, search_query=search_query)

# Rute Halaman Tambah Anggota (BARU!)
@app.route('/tambah_anggota', methods=['GET', 'POST'])
@login_required
def tambah_anggota():
    if request.method == 'POST':
        nama = request.form.get('nama')
        jabatan = request.form.get('jabatan')
        kelas = request.form.get('kelas')
        email = request.form.get('email')
        
        new_anggota = Anggota(nama=nama, jabatan=jabatan, kelas=kelas, email=email)
        db.session.add(new_anggota)
        db.session.commit()
        
        flash('Anggota baru berhasil ditambahkan!', 'success')
        return redirect(url_for('anggota'))
    
    return render_template('tambah_anggota.html')

# Rute Halaman Edit Anggota
@app.route('/edit_anggota/<int:anggota_id>', methods=['GET', 'POST'])
@login_required
def edit_anggota(anggota_id):
    anggota_to_edit = Anggota.query.get_or_404(anggota_id)
    
    if request.method == 'POST':
        anggota_to_edit.nama = request.form.get('nama')
        anggota_to_edit.jabatan = request.form.get('jabatan')
        anggota_to_edit.kelas = request.form.get('kelas')
        anggota_to_edit.email = request.form.get('email')
        db.session.commit()
        flash('Data anggota berhasil diperbarui!', 'success')
        return redirect(url_for('anggota'))
    
    return render_template('edit_anggota.html', anggota=anggota_to_edit)

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

        if not Anggota.query.first():
            data_anggota = [
                Anggota(nama="Budi Santoso", jabatan="Ketua OSIS", kelas="XI IPA 1", email="budi@osis.sch.id"),
                Anggota(nama="Dewi Permata", jabatan="Wakil Ketua OSIS", kelas="XI IPS 2", email="dewi@osis.sch.id"),
                Anggota(nama="Agus Salim", jabatan="Sekretaris", kelas="X MIPA 3", email="agus@osis.sch.id"),
                Anggota(nama="Siti Aminah", jabatan="Bendahara", kelas="X MIPA 1", email="siti@osis.sch.id"),
            ]
            for anggota_baru in data_anggota:
                db.session.add(anggota_baru)
            db.session.commit()
            print("Contoh data anggota berhasil ditambahkan.")

# Jalankan Aplikasi
if __name__ == '__main__':
    create_first_admin()
    app.run(debug=True)
