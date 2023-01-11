import view

data = {}

def tambah_data():
    print(f"{'TAMBAH DATA':^17}")
    print('=' * 17)
    view.data_input()
    print('=' * 84)
    print(f"|{'DATA BERHASIL DITAMBAHKAN':^82}|")
    print('=' * 84)

def hapus_data():
    cari = str(input('MASUKAN NAMA: '))
    if cari in data.keys():
        del data[cari]
        print('=' * 84)
        print(f"|{'DATA BERHASIL DIHAPUS':^82}|")
        print('=' * 84)

    else:
        print('=' * 84)
        print(f"|{'DATA TIDAK DITEMUKAN':^82}|")
        print('=' * 84)

def ubah_data():
    cari = str(input('MASUKAN NAMA: '))
    if cari in data.keys():
        print(f"{'UBAH DATA':^17}")
        print('=' * 17)
        view.data_input()
        print('=' * 84)
        print(f"|{'DATA BERHASIL DIUBAH':^82}|")
        print('=' * 84)

    else:
        print('=' * 84)
        print(f"|{'DATA TIDAK DITEMUKAN':^82}|")
        print('=' * 84)

def cari_data():
    print(f"{'DATA PENCARIAN':^17}")
    view.cetak_hasil_pencarian()
