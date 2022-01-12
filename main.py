from Model import daftar_nilai
from View import input_nilai, view_nilai
import Database

Data = {
    'Raphael' : 90
}
class Universal():
    def __init__(self, nama='',nilai=''):
        self.nama=nama
        self.nilai=nilai
        self.menu()

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

        elif self.Choose == 'B' or self.Choose == 'b':
            print("=== Hapus Data ===")
            for i in range(len(Database.data)):
                print(f'{i+1}. {list(Database.data.keys())[i]}')
            print("Pilih salah satu nama diatas dan ketik untuk menghapus ")
            self.nama = input_nilai.input_nama()
            daftar_nilai.hapus(self.nama)
            self.menu()

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

        elif self.Choose == 'D' or self.Choose == 'd':
            print("=== Cari Data ===")
            print("Ketik nama yang sudah exist di dalam Database")
            self.nama = input_nilai.input_nama()
            if self.nama in Database.data:
                daftar_nilai.cari(self.nama)
            else:
                print("Tidak dapat ditemukan")
            self.menu()

        elif self.Choose == 'E' or self.Choose == 'e':
            view_nilai.cetak()
            self.menu()

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

mipa1 = Universal()
