from database import Database

db = Database()

def tambah_pengguna(nama):
    db.insert_user(nama)

def tambah_skill(nama_skill, kategori, user_id):
    db.insert_skill(nama_skill, kategori, user_id)

def catat_progress(skill_id, tanggal, deskripsi, durasi, level):
    db.insert_progress(skill_id, tanggal, deskripsi, durasi, level)

def ambil_pengguna():
    return db.get_users()

def ambil_skill(user_id):
    return db.get_skills(user_id)

def ambil_progress(skill_id):
    return db.get_progress(skill_id)