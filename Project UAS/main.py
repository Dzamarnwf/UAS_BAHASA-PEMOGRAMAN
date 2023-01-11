import model
import view
import os
view.tampilan()
while True:
    print()
    lanjut = str(input('    MENU\n==============\n(L) LIHAT\n(T) TAMBAH\n(U) UBAH\n'
                       '(H) HAPUS\n(C) CARI\n(K) KELUAR\n==============\nPilihan : '))
    os.system("cls")
    if lanjut.lower() == 'l':
        view.cetak_daftar_nilai()
    elif lanjut.lower() == 't':
        model.tambah_data()
    elif lanjut.lower() == 'h':
        model.hapus_data()
    elif lanjut.lower() == 'u':
        model.ubah_data()
    elif lanjut.lower() == 'c':
        model.cari_data()
    elif lanjut.lower() == 'k':
        break
    else :
        print('PILIH MENU YANG TERSEDIA')
print('=' * 84)
print(f"|{'KELUAR DARI PROGRAM':^82}|")
print('=' * 84)
