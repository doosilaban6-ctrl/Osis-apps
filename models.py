from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Anggota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    jabatan = db.Column(db.String(100), nullable=False)
    kelas = db.Column(db.String(10), nullable=False)

class Kegiatan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_kegiatan = db.Column(db.String(200), nullable=False)
    tanggal = db.Column(db.String(50), nullable=False)
    lokasi = db.Column(db.String(100), nullable=False)
    deskripsi = db.Column(db.Text, nullable=True)
