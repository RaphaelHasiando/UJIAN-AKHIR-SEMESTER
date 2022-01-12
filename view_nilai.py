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
