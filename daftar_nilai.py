import Database
def tambah(nama, nilai):
  if nama in Database.data:
    print("=== Maaf, Nama yang anda masukkan sudah terdaftar ===")
  else:
    Database.tambahdata(nama,nilai)
    print('Berhasil')

def hapus(nama):
  if nama in Database.data:
    del Database.data[nama]
    print("Berhasil")
  else:
    print("tidak ditemukan")

def ubah(nama, nilai):
  if nama in Database.data:
    Database.data[nama] = nilai
    print("Berhasil")
  else:
    print("Gagal")

def cari(nama):
  print(f'Nama = {nama}')
  print(f'Nilai = {Database.data[nama]}')
