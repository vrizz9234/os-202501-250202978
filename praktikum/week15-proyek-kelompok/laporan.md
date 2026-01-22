
# Laporan Praktikum Minggu 15
Topik: Proyek Kelompok – Mini Simulasi Sistem Operasi (Scheduling + Memory + Container)


---

## Identitas
- **Nama**  :

1. Faris Azhar(250202978)
2. Muhammad Reza Pahlevi(250202995)
3. Ammarudin Ibnu Salam(250202929)
4. Tri Agustin Wahyuningtyas(250202970)
5. Keysya Ayu Anggita (250202944)

- **Kelas** : 1 IKRA 

---

## 1. Pendahuluan

## A. Latar Belakang

Sistem operasi merupakan komponen perangkat lunak fundamental yang berfungsi sebagai jembatan antara pengguna, aplikasi, dan perangkat keras komputer. Dalam perkembangan teknologi informasi yang sangat pesat, efisiensi pengelolaan sumber daya daya komputasi menjadi tantangan utama. Dua pilar utama dalam efisiensi ini adalah manajemen waktu melalui Penjadwalan CPU (CPU Scheduling) dan manajemen ruang melalui Manajemen Memori (Memory Management).

Penjadwalan CPU yang tepat memastikan bahwa setiap proses mendapatkan jatah waktu eksekusi yang adil dan responsif, sementara manajemen memori memastikan bahwa pemakaian RAM dilakukan secara optimal tanpa menyebabkan sistem menjadi lambat atau crash. Tanpa mekanisme ini, multitasking yang lancar pada komputer modern tidak mungkin tercapai.

Lebih jauh lagi, tren teknologi saat ini telah bergeser ke arah efisiensi tingkat tinggi melalui Teknologi Kontainer (Containerization). Berbeda dengan virtualisasi tradisional yang berat, kontainer memungkinkan isolasi sumber daya bagi aplikasi dengan menggunakan kernel sistem operasi yang sama secara bersama-sama. Hal ini menciptakan kebutuhan bagi para praktisi IT untuk memahami bagaimana batasan sumber daya (resource limit) diterapkan pada suatu proses di dalam lingkungan yang terisolasi.

Namun, mempelajari cara kerja internal sistem operasi secara langsung pada kernel aslinya seringkali sulit dilakukan karena kompleksitas kode dan risiko kegagalan sistem yang nyata. Oleh karena itu, pembuatan Mini Simulasi Sistem Operasi menjadi sangat relevan. Simulasi ini dirancang untuk memodelkan interaksi antara algoritma penjadwalan, alokasi memori, dan isolasi kontainer dalam lingkungan yang terkendali.

Melalui proyek ini, kelompok kami berupaya untuk mengintegrasikan ketiga konsep tersebut ke dalam satu aplikasi simulasi tunggal. Proyek ini tidak hanya bertujuan untuk memenuhi tugas akademis, tetapi juga untuk memberikan gambaran konkret mengenai bagaimana sebuah sistem operasi modern mengatur antrean proses, mengalokasikan RAM, dan menerapkan batasan sumber daya pada setiap unit kontainer.


## Tujuan
B. Tujuan
Setelah menyelesaikan proyek ini, mahasiswa mampu:
1. Bekerja kolaboratif dalam tim dengan pembagian peran yang jelas.
2. Mengintegrasikan beberapa konsep sistem operasi dalam satu aplikasi sederhana.
3. Mengelola proyek menggunakan Git (branch/PR/commit yang rapi).
4. Menyusun dokumentasi dan laporan proyek yang sistematis.
5. Melakukan presentasi dan demo hasil proyek.
---

Struktur folder:
week15-proyek-kelompok
 ┣ code
 ┃ ┣ data
 ┃ ┃ ┗ database
 ┃ ┣ CPU.py
 ┃ ┣ dockerfile
 ┃ ┣ example.txt
 ┃ ┣ kelompok.py
 ┃ ┗ LRU.py
 ┣ screenshots
 ┃ ┣ cpuscheduling.png
 ┃ ┣ dockerbuild.png
 ┃ ┣ example.png
 ┃ ┣ keluar.png
 ┃ ┗ pagereplacemen.png
 ┣ laporan.md
 ┗ presentasi.md
## 2. Arsitektur Aplikasi










## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi

Sertakan screenshot hasil percobaan atau diagram:


---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. [Pertanyaan 1]  
   **Jawaban:**  
2. [Pertanyaan 2]  
   **Jawaban:**  
3. [Pertanyaan 3]  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
