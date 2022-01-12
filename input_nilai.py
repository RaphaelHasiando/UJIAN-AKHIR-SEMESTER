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
