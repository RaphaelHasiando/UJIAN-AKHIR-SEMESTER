# UJIAN-AKHIR-SEMESTER
<img width="695" alt="image" src="https://user-images.githubusercontent.com/61907877/149056466-98323c9c-b1a5-4372-a013-84d81abf67b4.png">

### 1 - Buatlah package masing - masing dengan struktur seperti ini

<img width="153" alt="image" src="https://user-images.githubusercontent.com/61907877/149056768-123a74eb-9347-42ad-8558-543f9e9ef923.png">

- main.py berisi program utama (menu pilihan yang memanggil semua menu yang ada)
- Database.py berisi kumpulan data yang akan disimpan
- daftar_nilai.py berisi modul untuk tambah_data, ubah_data, hapus_data, dan cari_data
- input_nilai.py berisi modul untuk input_data yang meminta pengguna memasukkan data
- view_nilai.py berisi modul untuk cetak_daftar_nilai, cetak_hasil_pencarian

### 2 - main.py dan menu
Buatlah package masing masing terlebih dahulu. Lalu, 
Buatlah kelas baru di dalam main.py
###
    from Model import daftar_nilai
    from View import input_nilai, view_nilai
    import Database
    
    class Universal():
        def __init__(self, nama='',nilai=''):
            self.nama=nama
            self.nilai=nilai
            self.menu()
Setelah itu, Buatlah menu pilihan
###
    def menu(self):
        print("=== MAIN MENU ===")
        print("[A] Tambah Data | [B] Hapus Data | [C] Ubah Data | [D] Cari Data | [E] Tampil Data | [F] Tampil daftar nilai | [K] Keluar")
        self.Choose = input("---> ")
        if self.Choose == 'A' or self.Choose == 'a':
            print("=== Tambah Data ===")        
  
        elif self.Choose == 'B' or self.Choose == 'b':
            print("=== Hapus Data ===")
            self.menu()

        elif self.Choose == 'C' or self.Choose == 'c':
            print("=== Ubah Data ===")

        elif self.Choose == 'D' or self.Choose == 'd':
            print("=== Cari Data ===")

        elif self.Choose == 'E' or self.Choose == 'e':
            self.menu()

        elif self.Choose == 'F' or self.Choose == 'f':
            print("=== Tampil daftar nilai ===")

        elif self.Choose == 'K' or self.Choose == 'k':
            print("Logged out...")

        else:
            print("Opsi Tidak tertera, mohon diulangi..")
            self.menu()
### 3 - Tambah data
di dalam daftar_nilai (package), import Database (sistem untuk menyimpan data. Basis data dapat menambahkan, mengubah, atau menyajikan informasi pada basis data) dan buatlah function untuk menambah data.
##
    import Database
    def tambah(nama, nilai):
        if nama in Database.data:
            print("=== Maaf, Nama yang anda masukkan sudah terdaftar ===")
        else:
            Database.tambahdata(nama,nilai)
            print('Berhasil')
di dalam parameter tersebut, variabel yang terdaftar di dalam tanda kurung dalam definisi fungsi. Argumen adalah nilai yang dikirim ke fungsi saat dipanggil.
### 4 - Hapus data
##
    def hapus(nama):
      if nama in Database.data:
          del Database.data[nama]
          print("Berhasil")
      else:
          print("tidak ditemukan")
### 5 - Ubah data
##
    def ubah(nama, nilai):
        if nama in Database.data:
            Database.data[nama] = nilai
            print("Berhasil")
        else:
            print("Gagal")
### 6 - Cari data
##
    def cari(nama):
        print(f'Nama = {nama}')
        print(f'Nilai = {Database.data[nama]}')
### 7 - Database
di dalam Database.py, buatlah dict function dengan data yang akan disimpan.
##
    data = {
        'Raphael' : 90,
        'Michael' : 80
    }
    def tambahdata(input_nama, input_nilai):
        data[input_nama] = int(input_nilai)
    def hapusdata(input_nama):
        del data[input_nama]
### 8 - Input nilai
di dalam input_nilai.py (package), buatlah dua function untuk memasukkan nama dan nilainya, dan juga kedua itu akan return valuenya.
##
    def input_nama():
        nama = input("Nama = ")
        return nama
    def input_nilai():
        while True:
            try:
                nilai = input("Nilai = ")
                return int(nilai)
            except:
                print("Pengisian tersebut harus dalam bentuk angka!")
### 9 - View nilai
di dalam view_nilai.py, buatlah 2 function untuk cetak data dan data berdasarkan nilai tertentu
##
    import Database
    def cetak():
        print("====== Data Universal ======")
        if len(Database.data.items()) == 0:
            print(" >Data masih belum tersedia<")
        else:
            for i in range(len(Database.data)):
                print(f'Nama : {list(Database.data.keys())[i]} | Nilai : {list(Database.data.values())[i]}')
        print("============================")

    def cetak_nilai(nilai):
        print("====== Hasil nilai yang lulus dengan nilai yang dimasukkan ======")
        if len(Database.data.items()) == 0:
            print(" >Data masih belum tersedia<")
        else:
            print(f'Nilai siswa > {nilai}')
            print("==================")
            for i in range(len(Database.data)):
                if nilai <= list(Database.data.values())[i]:
                    print(f'{list(Database.data.keys())[i]} | {list(Database.data.values())[i]}')
            print("============================================================")
### 10 - Memanggil dan Memuat semua modul di dalam main.py
Untuk tambah data
##
    def menu(self):
        print("=== MAIN MENU ===")
        print("[A] Tambah Data | [B] Hapus Data | [C] Ubah Data | [D] Cari Data | [E] Tampil Data | [F] Tampil daftar nilai | [K] Keluar")
        self.Choose = input("---> ")
        if self.Choose == 'A' or self.Choose == 'a':
            print("=== Tambah Data ===")
            self.nama = input_nilai.input_nama()
            self.nilai = input_nilai.input_nilai()
            daftar_nilai.tambah(self.nama, self.nilai)
            self.menu()
Untuk Hapus data
##
        elif self.Choose == 'B' or self.Choose == 'b':
            print("=== Hapus Data ===")
            for i in range(len(Database.data)):
                print(f'{i+1}. {list(Database.data.keys())[i]}')
            print("Pilih salah satu nama diatas dan ketik untuk menghapus ")
            self.nama = input_nilai.input_nama()
            daftar_nilai.hapus(self.nama)
            self.menu()
Untuk Ubah data
##
        elif self.Choose == 'C' or self.Choose == 'c':
            print("=== Ubah Data ===")
            for i in range(len(Database.data)):
                print(f'{i+1}. {list(Database.data.keys())[i]}')
            print("Pilih salah satu nama diatas dan ketik untuk mengubah ")
            self.nama = input_nilai.input_nama()
            if self.nama in Database.data:
                self.nilai = input_nilai.input_nilai()
                daftar_nilai.ubah(self.nama, self.nilai)
            else:
                print("Tidak ditemukan")
            self.menu()
Untuk cari data
##
        elif self.Choose == 'D' or self.Choose == 'd':
            print("=== Cari Data ===")
            print("Ketik nama yang sudah exist di dalam Database")
            self.nama = input_nilai.input_nama()
            if self.nama in Database.data:
                daftar_nilai.cari(self.nama)
            else:
                print("Tidak dapat ditemukan")
            self.menu()
Untuk Cetak data
##
        elif self.Choose == 'E' or self.Choose == 'e':
            view_nilai.cetak()
            self.menu()
Untuk Cetak data berdasarkan nilai
##
        elif self.Choose == 'F' or self.Choose == 'f':
            print("=== Tampil daftar nilai ===")
            self.nilai = input_nilai.input_nilai()
            view_nilai.cetak_nilai(self.nilai)
            self.menu()
         
        elif self.Choose == 'K' or self.Choose == 'k':
            print("Logged out...")

        else:
            print("Opsi Tidak tertera, mohon diulangi..")
            self.menu()
            
    Mipa1 = Universal()
![image](https://user-images.githubusercontent.com/61907877/149063119-de4bcece-6f1b-42b8-9957-8f0a0461d61d.png)
![image](https://user-images.githubusercontent.com/61907877/149063220-3d6a31fa-130a-4dcf-b69b-5d901fdc100e.png)
![image](https://user-images.githubusercontent.com/61907877/149063308-9adf1a73-a556-4806-99e5-9185da32c2a3.png)
![image](https://user-images.githubusercontent.com/61907877/149063451-4ce7d4c3-53f1-45f0-8aea-88814602850f.png)
![image](https://user-images.githubusercontent.com/61907877/149063545-90bfae9c-bc39-4512-8788-0d38eadfcbeb.png)
![image](https://user-images.githubusercontent.com/61907877/149063549-a4f230ef-e696-4ab0-8b90-5433e8c438fb.png)

