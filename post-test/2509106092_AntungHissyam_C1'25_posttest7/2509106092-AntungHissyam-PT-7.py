# variabel global
pengguna = {"admin": {"password": "123456789012345", "role": "admin"}}
pegawai = {}
login = None


# fungsi rekursif 
def hitung_pegawai(keys):
    if not keys:
        return 0
    else:
        return 1 + hitung_pegawai(keys[1:])


# prosedur register
def register():
    global pengguna
    try:
        print("=== REGISTER AKUN BARU ===")

        username = input("Masukkan username (maksimal 50 karakter): ")
        if len(username) > 50:
            print("Error: Username tidak boleh lebih dari 50 karakter.")
            return
        if username in pengguna:
            print("Error: Username sudah terdaftar.")
            return

        password = input("Masukkan password (minimal 15, maksimal 50 karakter): ")
        if len(password) < 15:
            print("Error: Password minimal 15 karakter.")
            return
        if len(password) > 50:
            print("Error: Password tidak boleh lebih dari 50 karakter.")
            return

        role = input("Masukkan role (admin/pengguna): ")
        if role not in ["admin", "pengguna"]:
            print("Error: Role tidak valid, hanya boleh 'admin' atau 'pengguna'.")
            return

        # kalau semua valid baru simpan
        pengguna[username] = {"password": password, "role": role}
        print("Registrasi berhasil! Silakan login.")

    except Exception as e:
        print("Terjadi kesalahan saat registrasi:", e)



# prosedur login
def login_user():
    global login
    try:
        if len(pengguna) == 0:
            print("Belum ada pengguna, silakan registrasi dahulu.")
            return

        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username not in pengguna:
            print("Error: Username tidak ditemukan.")
            return
        if pengguna[username]["password"] != password:
            print("Error: Password salah.")
            return

        login = {"username": username, "role": pengguna[username]["role"]}
        print("Login berhasil sebagai", login["role"])

    except Exception as e:
        print("Terjadi kesalahan saat login:", e)


# fungsi tanpa parameter
def tampilkan_data():
    global pegawai
    try:
        if len(pegawai) == 0:
            print("Belum ada data pegawai.")
            return False

        print("=== DATA PEGAWAI ===")
        for idp, data in pegawai.items():
            print(f"ID: {idp} | Nama: {data['nama']} | Jabatan: {data['jabatan']} | Nomor HP: {data['hp']}")
        print(f"Total pegawai: {hitung_pegawai(list(pegawai.keys()))}")
        print("================================")
        return True

    except Exception as e:
        print("Terjadi kesalahan saat menampilkan data:", e)
        return False


# fungsi tanpa parameter
def tambah_data():
    global pegawai
    try:
        idp = input("Masukkan ID Pegawai (hanya angka): ")
        if idp in pegawai:
            print("Error: ID pegawai sudah terdaftar.")
            return
        if not idp.isdigit():
            print("Error: ID harus berupa angka.")
            return

        nama = input("Masukkan Nama Pegawai: ")       
        jabatan = input("Masukkan Jabatan: ")
        if jabatan == "" or nama == "":
            print("Error: Jabatan atau Nama tidak boleh kosong.")
            return
        hp = input("Masukkan Nomor HP: ")
        if not hp.isdigit():
            print("Error: Nomor HP harus berupa angka.")
            return

        pegawai[idp] = {"nama": nama, "jabatan": jabatan, "hp": hp}
        print("Data pegawai berhasil ditambahkan.")

    except Exception as e:
        print("Terjadi kesalahan saat menambah data:", e)


# fungsi dengan parameter
def edit_data(id_edit):
    global pegawai
    try:
        if not id_edit.isdigit():
            print("Error: ID harus berupa angka.")
            return
        if id_edit not in pegawai:
            print("Error: ID pegawai tidak ditemukan.")
            return

        nama_baru = input("Masukkan Nama baru: ")
        jabatan_baru = input("Masukkan Jabatan baru: ")
        if jabatan_baru == "" or nama_baru == "":
            print("Error: Jabatan atau Nama tidak boleh kosong.")
            return
        hp_baru = input("Masukkan Nomor HP baru: ")
        if not hp_baru.isdigit():
            print("Error: Nomor HP harus berupa angka.")
            return

        pegawai[id_edit]["nama"] = nama_baru
        pegawai[id_edit]["jabatan"] = jabatan_baru
        pegawai[id_edit]["hp"] = hp_baru
        print("Data berhasil diperbarui.")

    except Exception as e:
        print("Terjadi kesalahan saat mengedit data:", e)


# fungsi dengan parameter
def hapus_data(id_hapus):
    global pegawai
    try:
        if not id_hapus.isdigit():
            print("Error: ID harus berupa angka.")
            return
        if id_hapus not in pegawai:
            print("Error: ID pegawai tidak ditemukan.")
            return

        del pegawai[id_hapus]
        print("Data pegawai berhasil dihapus.")

    except Exception as e:
        print("Terjadi kesalahan saat menghapus data:", e)

# menu utama
while True:
    print("""
=====================================
| PROGRAM MANAJEMEN PEGAWAI         |
| Perusahaan Cumi Hitam Pak Kris    |
=====================================
| 1. Register                       |
| 2. Login                          |
| 3. Keluar                         |
=====================================
""")

    menu = input("Pilih menu: ")

    if menu == "1":
        register()

    elif menu == "2":
        login_user()
        if login is not None:
            if login["role"] == "admin":
                while True:
                    print("""
==============================
| MENU ADMIN                 |
==============================
| 1. Lihat Data Pegawai      |
| 2. Tambah Pegawai          |
| 3. Edit Data Pegawai       |
| 4. Hapus Pegawai           |
| 5. Logout                  |
==============================
""")
                    pilihan = input("Pilih menu: ")

                    if pilihan == "1":
                        tampilkan_data()

                    elif pilihan == "2":
                        tambah_data()

                    elif pilihan == "3":
                        if tampilkan_data():   
                            try:
                                id_edit = input("Masukkan ID Pegawai yang ingin diubah: ")
                                edit_data(id_edit)
                            except Exception as e:
                                print("Terjadi kesalahan saat memilih ID Pegawai", e)

                    elif pilihan == "4":
                        if tampilkan_data():  
                            try:
                                id_hapus = input("Masukkan ID Pegawai yang ingin dihapus: ")
                                hapus_data(id_hapus)
                            except Exception as e:
                                print("Terjadi kesalahan saat memilih ID yang ingin dihapus", e)

                    elif pilihan == "5":
                        print("Logout berhasil.")
                        login = None
                        break
                    else:
                        print("Pilihan tidak valid.")

            elif login["role"] == "pengguna":
                while True:
                    print("""
==============================
| MENU PENGGUNA              |
==============================
| 1. Lihat Data Pegawai      |
| 2. Logout                  |
==============================
""")
                    pilihan = input("Pilih menu: ")
                    if pilihan == "1":
                        tampilkan_data()
                    elif pilihan == "2":
                        print("Logout berhasil.")
                        login = None
                        break
                    else:
                        print("Pilihan tidak valid.")

    elif menu == "3":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid.")
