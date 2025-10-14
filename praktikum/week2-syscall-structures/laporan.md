
# Laporan Praktikum Minggu [X]
Topik: Arsitektur Sistem Operasi dan Kernel

---

## Identitas
- **Nama**  : [Faris Azhar]  
- **NIM**   : [250202978]  
- **Kelas** : [1IKRA]

---

## Tujuan
1. Fungsi utama Sistim Operasi
Sistim operasi penghubung antara pengguna dan perangkat keras komputer.
Fungsi utamanya:
1.Manajemen Proses
Mengatur jalannya program yang sedang berjalan misalnya multitasking,kapan proses dijalankan,dihentikan,atau dilanjutkan.
2.Manajemen Memori
Mengatur penggunaan RAM agar setiap program mendapatkan ruang memori yang cukup tanpa, saling bertabrakan.
3.Menejemen Perangkat
Mengatur komunikasi antara komputer dengan perangkat keras (printer,keyboard,hard disk) melalui driver.
4.Manajemen File
Mengatur penyimpanan,penghapusan, penamaan, dan akses file di penyimpanan.
5.menejemen Keamanan dan Akses
Melindungi data dan sistem dari akses tidak sah.
6.Manajemen User Interface
-Menyediakan antarmuka bagi pengguna.

2.Kernel
inti dari sebuah sistem paling dasar berhubungan dengan perangkat keras.
Fungsi kernel ialah:
1. Mengatur sumber daya komputer(CPU,memori,perangkatI/O).
2. Menangani sistem file dan manajemen proses
3. Menjadi penghubung antara perangkat keras dan perangkat lunak
4. Menjalankan perintah-perintah dasar dari system call.

3. System call
sistem call adalah jembatan antara program aplikasi dengan kernel. Ketika program ini melakukan sesuatu yang berhubungan dengan perangkat keras, dia tidak bisa langsung berhubungan dengan hardware,tetapi harus meminta bantuan kernel lewat sistem call.
Contoh system call:
open:membuka file
read:membaca isi file
write:menulis ke file
fork:membuat proses baru
exit:mengakhiri proses


---

## Dasar Teori


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
