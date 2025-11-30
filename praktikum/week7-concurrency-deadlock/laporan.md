
# Laporan Praktikum Minggu 7
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : Faris Azhar
- **NIM**   : 250202978 
- **Kelas** : 1 IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> Mahasiswa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

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
![Screenshot hasil](screenshots/example.png)

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
1.Sebutkan empat kondisi utama penyebab deadlock.

Deadlock adalah situasi di mana serangkaian proses terhenti karena setiap proses menunggu sumber daya (resource) yang sedang dipegang oleh proses lain. Menurut Coffman Conditions, deadlock hanya akan terjadi jika keempat kondisi berikut terpenuhi secara bersamaan:

1.Mutual Exclusion (Saling Mengunci): Setidaknya ada satu sumber daya yang bersifat non-sharable (tidak dapat dibagi). Artinya, hanya satu proses yang dapat menggunakan sumber daya tersebut pada satu waktu.

2.Hold and Wait (Genggam dan Tunggu): Sebuah proses sedang memegang setidaknya satu sumber daya dan sedang menunggu untuk mendapatkan sumber daya tambahan yang saat ini sedang dipegang oleh proses lain.

3.No Preemption (Tidak Ada Preemption): Sumber daya tidak dapat diambil paksa dari proses yang memegangnya. Sumber daya hanya dapat dilepaskan secara sukarela oleh proses itu sendiri setelah tugasnya selesai.

4.Circular Wait (Menunggu Melingkar): Terdapat rantai proses (P1, P2, ..., Pn) di mana P1 menunggu sumber daya yang dipegang P2, P2 menunggu P3, dan seterusnya 
hingga Pn menunggu sumber daya yang dipegang kembali oleh P1.


2. Mengapa sinkronisasi diperlukan dalam sistem operasi?


Sinkronisasi proses mutlak diperlukan dalam sistem operasi, terutama pada sistem multiprogramming atau multithreading, karena alasan berikut:

Mencegah Race Condition: Ini adalah kondisi paling kritis. Race condition terjadi ketika beberapa proses mengakses dan memanipulasi data yang sama secara bersamaan. Tanpa sinkronisasi, hasil akhirnya bergantung pada urutan eksekusi yang tidak terprediksi, menyebabkan data menjadi korup atau tidak konsisten.

Menjaga Konsistensi Data: Sinkronisasi memastikan bahwa ketika satu proses sedang menulis data ke variabel bersama (shared variable), proses lain tidak boleh membaca atau menulis ke variabel yang sama sampai proses pertama selesai.

Mengatur Urutan Eksekusi: Dalam beberapa kasus, proses B mungkin membutuhkan hasil output dari proses A sebelum bisa berjalan. Sinkronisasi memastikan proses B "menunggu" hingga A selesai.

Analogi: Bayangkan dua orang mencoba menarik uang dari rekening bank yang sama pada detik yang persis sama di ATM berbeda. Tanpa sinkronisasi (penguncian database), saldo bisa menjadi negatif atau transaksi ganda bisa terjadi. 

3.Jelaskan perbedaan antara *semaphore* dan *monitor*.

| Fitur             | Semaphore                                                                 | Monitor                                                                                   |
|-------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Definisi          | Variabel integer yang digunakan untuk memberi sinyal antar proses.        | Tipe data abstrak (ADT) atau modul tingkat tinggi yang mengenkapsulasi data dan prosedur. |
| Tingkat Abstraksi | Low-level: Lebih dekat ke mesin/bahasa assembly atau C.                   | High-level: Fitur bahasa pemrograman (seperti `synchronized` di Java).                    |
| Mekanisme         | Menggunakan operasi atomik `Wait()` (P) dan `Signal()` (V).               | Menggunakan prosedur di dalam monitor; mutual exclusion diatur otomatis oleh monitor.      |
| Fleksibilitas     | Sangat fleksibel tapi rawan error. Jika programmer lupa memanggil `Signal()`, deadlock mudah terjadi. | Lebih kaku tapi lebih aman dan mudah dikelola karena penanganan dilakukan oleh compiler/bahasa. |
| Kepemilikan       | Tidak ada konsep kepemilikan; proses manapun bisa melakukan signal.       | Hanya proses yang berada dalam monitor yang memiliki akses.                                |


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
