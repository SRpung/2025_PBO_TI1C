import streamlit as st
import pandas as pd
from management import *

st.title("SkillForge \U0001F3CB️ - Pelacak Perkembangan Skill")

menu = st.sidebar.selectbox("Menu", ["Tambah Pengguna", "Tambah Skill", "Catat Progress", "Lihat Progress"])

if menu == "Tambah Pengguna":
    st.header("Tambah Pengguna Baru")
    name = st.text_input("Nama Pengguna")
    if st.button("Simpan") and name:
        tambah_pengguna(name)
        st.success(f"Pengguna '{name}' berhasil ditambahkan.")

elif menu == "Tambah Skill":
    st.header("Tambah Skill Baru")
    users = ambil_pengguna()
    user_dict = {u[1]: u[0] for u in users}
    selected_user = st.selectbox("Pilih Pengguna", list(user_dict.keys()))
    skill_name = st.text_input("Nama Skill")
    category = st.selectbox("Kategori", ["Hard Skill", "Soft Skill", "Lainnya"])
    if st.button("Simpan") and skill_name:
        tambah_skill(skill_name, category, user_dict[selected_user])
        st.success(f"Skill '{skill_name}' berhasil ditambahkan untuk {selected_user}.")

elif menu == "Catat Progress":
    st.header("Catat Progress Skill")
    users = ambil_pengguna()
    user_dict = {u[1]: u[0] for u in users}
    selected_user = st.selectbox("Pilih Pengguna", list(user_dict.keys()))
    skills = ambil_skill(user_dict[selected_user])
    skill_dict = {s[1]: s[0] for s in skills}
    selected_skill = st.selectbox("Pilih Skill", list(skill_dict.keys()))

    date = st.date_input("Tanggal")
    desc = st.text_area("Deskripsi Kegiatan")
    duration = st.number_input("Durasi (menit)", min_value=0)
    level = st.slider("Level Saat Ini", 1, 10)
    if st.button("Catat"):
        catat_progress(skill_dict[selected_skill], str(date), desc, duration, level)
        st.success("Progress berhasil dicatat!")

elif menu == "Lihat Progress":
    st.header("Lihat Progress Skill")
    users = ambil_pengguna()
    user_dict = {u[1]: u[0] for u in users}
    selected_user = st.selectbox("Pilih Pengguna", list(user_dict.keys()))
    skills = ambil_skill(user_dict[selected_user])
    skill_dict = {s[1]: s[0] for s in skills}
    selected_skill = st.selectbox("Pilih Skill", list(skill_dict.keys()))
    progress_data = ambil_progress(skill_dict[selected_skill])

    if progress_data:
        df = pd.DataFrame(progress_data, columns=["ID", "Skill ID", "Tanggal", "Deskripsi", "Durasi", "Level"])
        df = df.drop(columns=["ID", "Skill ID"])
        st.dataframe(df)
        st.line_chart(df[["Durasi", "Level"]])
    else:
        st.info("Belum ada progress dicatat.")