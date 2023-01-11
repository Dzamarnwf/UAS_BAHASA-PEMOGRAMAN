# UAS-BAHASA-PEMROGRAMAN
**Project UAS Bahasa Pemrograman**
```
NAMA    : Dipca Anugrah 
NIM     : 312210666 TI.22.A.4
STUDI   : TEKNIK INFORMATIKA
KELAS   : TI.22.A.4
```

## Deskripsi
1. Fungsi file `model-> daftar_nilai.py` model adalah sebuah package, package adalah sebuah file yang berisi module, sedangkan daftar_nilai.py adalah sebuah module, module adalah sebuah file yang berisi program. Didalam file `daftar_nilai.py` berisi program untuk `tambah_data(), ubah_data(), hapus_data() dan cari_data()`.

2. Fungsi file `model-> __init__.py` adalah memberikan label untuk suatu paket yang berupa sekumpulan file pada direktori sehingga mampu mencegah direktori dengan nama yang umum. Didalam file `__init__.py` adalah `from .daftar_nilai import *` kegunaan dari perintah program tersebut adalah untuk menghubungkan semua module yang terdapat pada package `model`, jadi kita tidak harus mengimport panjang-panjang atau satu-satu di dalam file-filenya nanti.

3. Fungsi file `view-> input_nilai.py` view adalah sebuah package, sedangkan file `input_nilai.py` adalah sebuah modul yang berisi perintah program untuk menginputkan data yang terdiri dari nama, nim, tugas, uts, uas dari user/pengguna, yang nantinya kita akan simpan di dalam array dictionary dan ditampilkan di dalam file `viewe_nilai.py`.

4. Fungsi file `view-> view_nilai.py` adalah untuk menampilkan inputan dari file `input_nilai.py` yang akan diinput oleh user dan nantinya di tampilkan di file `view_nilai.py`. Di file ini berisi perintah untuk menampilkan cetak_daftar_nilai() dan cetak_hasil_pencarian().

5. Fungsi file `view-> __init__.py` sama seperti yang ada di package `model` yakni berfungsi sebagai memberikan label untuk suatu paket yang berupa sekumpulan file pada direktori sehingga mampu mencegah direktori dengan nama yang umum. singkatnya untuk merantai semua file yang ada di dalam pakcage.

## Detail Tutorial & Penjelasan Program 
Untuk penjelasan program lebih detailnya terdapat pada file dan link dibawah ini:

* Untuk penjelasan program, tutorial dan dokumentasi program ada pada folder `"file Pdf"`

* Untuk file script project programnya ada pada folder `"Project UAS"`

* Berikut adalah link YouTube Penjelasan dan Tutorial https://youtu.be/HNA_r9EL-i8 
