
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : Faris Azhar
- **NIM**   : 250202978  
- **Kelas** : 1 IKRA

---

## Tujuan
1.Menggunakan perintah ls, pwd, cd, cat untuk navigasi file dan direktori.
2.Menggunakan `chmod` dan `chown` untuk manajemen hak akses file.
3. Menjelaskan hasil output dari perintah Linux dasar.
4. Menyusun laporan praktikum dengan struktur yang benar.
5. Mengunggah dokumentasi hasil ke Git Repository tepat waktu.
---

## Dasar Teori
Linux adalah sebuah sistem operasi (OS) sumber terbuka (open-source) yang berbasis Unix, dikembangkan pertama kali oleh Linus Torvalds pada tahun 1991.

Dalam praktiknya, Linux sering merujuk pada keseluruhan sistem operasi yang terdiri dari kernel Linux (inti dari OS yang mengelola perangkat keras) dan berbagai perangkat lunak pendukung, yang keseluruhannya dikenal sebagai distribusi Linux (atau "distro," seperti Ubuntu, Fedora, Debian, atau Mint).
Tujuan Mengoperasikan Linux
Tujuan utama seseorang atau organisasi memilih dan mengoperasikan Linux seringkali berkaitan dengan sifatnya yang sumber terbuka, gratis, dan sangat andal.
Keuntungan Utama Linux
Gratis dan Sumber Terbuka (Open Source) 
Linux dapat diunduh dan digunakan tanpa biaya lisensi (tidak perlu membayar untuk menggunakannya).
Kode sumbernya terbuka untuk publik, memungkinkan siapa saja untuk melihat, memodifikasi, dan mendistribusikannya. Tujuannya adalah mendorong transparansi, inovasi, dan kolaborasi global.
Keamanan dan Stabilitas 

Linux dikenal memiliki keamanan yang kuat karena sistem izin penggunanya yang ketat dan struktur yang secara inheren membuatnya lebih tahan terhadap virus dan malware dibandingkan sistem operasi komersial lainnya.

Sistem ini sangat stabil dan dapat berjalan dalam jangka waktu lama (berbulan-bulan) tanpa perlu di-reboot. Hal ini menjadikannya pilihan utama untuk server web, database, dan sistem komputasi awan (cloud computing).

Fleksibilitas dan Kustomisasi (Penyesuaian) ️

Tersedia banyak distribusi Linux (distro) yang dapat dipilih sesuai kebutuhan spesifik, misalnya untuk desktop, server, komputasi berkinerja tinggi (superkomputer), pengembangan perangkat lunak, atau perangkat tersemat (embedded devices) seperti smart TV dan router.

Pengguna memiliki kontrol penuh untuk memodifikasi dan menyesuaikan hampir setiap aspek sistem, mulai dari tampilan antarmuka hingga komponen kernel.

Kinerja dan Efisiensi 

Linux umumnya ringan dan tidak memerlukan banyak sumber daya perangkat keras (RAM dan CPU), menjadikannya ideal untuk menghidupkan kembali komputer lama atau menjalankan sistem di perangkat dengan spesifikasi rendah.

Kinerjanya yang tinggi juga cocok untuk lingkungan kerja yang membutuhkan multitasking dan manajemen sumber daya yang efisien.

Secara ringkas, orang menggunakan Linux untuk mencapai kebebasan biaya, kontrol sistem penuh, keamanan, dan kinerja yang unggul dalam berbagai aplikasi, mulai dari penggunaan desktop harian, pengembangan perangkat lunak, hingga infrastruktur server skala besar (misalnya, Android, sistem operasi ponsel paling populer di dunia, juga dibangun di atas kernel Linux).

---

## Langkah Praktikum1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan folder kerja berada di dalam direktori repositori Git praktikum:
     ```
     praktikum/week3-linux-fs-permission/
     ```

2. **Eksperimen 1 – Navigasi Sistem File**
   Jalankan perintah berikut:
   ```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   ```
   - Jelaskan hasil tiap perintah.
   - Catat direktori aktif, isi folder, dan file tersembunyi (jika ada).

3. **Eksperimen 2 – Membaca File**
   Jalankan perintah:
   ```bash
   cat /etc/passwd | head -n 5
   ```
   - Jelaskan isi file dan struktur barisnya (user, UID, GID, home, shell).

4. **Eksperimen 3 – Permission & Ownership**
   Buat file baru:
   ```bash
   echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt
   ```
   - Analisis perbedaan sebelum dan sesudah chmod.  
   - Ubah pemilik file (jika memiliki izin sudo):
   ```bash
   sudo chown root percobaan.txt
   ls -l percobaan.txt
   ```
   - Catat hasilnya.

5. **Eksperimen 4 – Dokumentasi**
   - Ambil screenshot hasil terminal dan simpan di:
     ```
     praktikum/week3-linux-fs-permission/screenshots/
     ```
   - Tambahkan analisis hasil pada `laporan.md`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 3 - Linux File System & Permission"
   git push origin main
   ```
   
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   ```
```bash
   cat /etc/passwd | head -n 5
```
  ```bash
   echo "Hello Faris Azhar- > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt
   ```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:

![alt text](<screenshots/Screenshot 2025-10-26 144149.png>)


---

## Analisis
##1.Analisis File
No.,Perintah,Deskripsi/Hasil Observasi,Penjelasan
1.,pwd,Menampilkan jalur direktori kerja saat ini (contoh: /home/user/dokumen).,"Perintah ini kependekan dari ""Print Working Directory"" dan digunakan untuk mengetahui lokasi direktori (folder) tempat pengguna sedang berada di sistem berkas."


2.,ls -l,Menampilkan daftar isi direktori saat ini dalam format panjang (detail).,"Perintah ls (list) menampilkan isi direktori. Opsi -l menambahkan detail seperti hak akses, jumlah link, pemilik, grup, ukuran berkas, dan tanggal modifikasi."


3.,cd /tmp,Berpindah ke direktori /tmp.,Perintah cd (Change Directory) digunakan untuk navigasi. Direktori /tmp adalah lokasi sementara untuk berkas yang tidak perlu disimpan secara permanen.


4.,ls -a,"Menampilkan seluruh isi direktori /tmp, termasuk berkas tersembunyi.","Perintah ls menampilkan isi direktori. Opsi -a (all) memastikan semua berkas, termasuk berkas yang diawali dengan titik (.) yang biasanya tersembunyi, ikut ditampilkan."
##2.Membaca File Jalankan perintah:
No.,Perintah,Deskripsi/Hasil Observasi (Contoh Output),Penjelasan
1.,cat /etc/passwd | head -n 5,Contoh Output 5 Baris Pertama:root:x:0:0:root:/root:/bin/bashdaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologinbin:x:2:2:bin:/bin:/usr/sbin/nologinsys:x:3:3:sys:/dev:/usr/sbin/nologinsync:x:4:65534:sync:/bin:/bin/sync,Perintah ini menggabungkan dua perintah:1. cat /etc/passwd: Menampilkan seluruh isi file /etc/passwd.2. 
No.,Nama Field,Keterangan,Contoh Nilai
1.,User (Username),Nama unik akun pengguna. Digunakan saat login.,"root, gemini"
2.,Password,"Placeholder Sandi. Karakter x menunjukkan bahwa sandi akun yang dienkripsi disimpan di file terpisah yang lebih aman, yaitu /etc/shadow.",x
3.,UID (User ID),Nomor Identifikasi Pengguna unik. UID 0 selalu dicadangkan untuk pengguna root (administrator).,"0, 1000"
4.,GID (Group ID),Nomor Identifikasi Kelompok utama (Primary Group) tempat pengguna tersebut berada.,"0, 1000"
5.,GECOS,"Informasi deskriptif (Opsional). Biasanya berisi nama lengkap pengguna, nomor kantor, dan detail kontak lainnya.","root, Gemini User"
6.,Home Directory,Jalur absolut ke direktori home pengguna. Tempat pengguna memulai sesi kerjanya setelah login.,"/root, /home/gemini"
7.,Shell,"Jalur ke program shell yang akan dijalankan ketika pengguna login (misalnya, untuk antarmuka baris perintah). Jika nilainya adalah /usr/sbin/nologin atau sejenisnya, berarti akun tersebut tidak dapat digunakan untuk login interaktif.","/bin/bash, /usr/sbin/nologin"
##3.Permission & Ownership Buat file baru:
Untuk memasukkan kode dengan nama yang bisa di sesuaikan dengan nick dan nim tersendiri


---

## Kesimpulan
1.Perintah dasar Linux seperti echo, ls, cd, dan cat digunakan untuk membuat, menampilkan, dan mengelola file serta direktori. Contohnya, echo "Hello <Faris>" > percobaan.txt berhasil membuat file teks baru.
2.Kepemilikan file (ownership) dapat diubah dengan chown, yang menentukan siapa pemilik dan grup dari file tersebut. Setelah sudo chown root percobaan.txt, file berpindah kepemilikan ke root, sehingga hanya superuser yang bisa mengaksesnya.


---

## Quiz
1.Apa fungsi dari perintah `chmod`? Fungsi utama dari perintah **chmod** (Change Mode) adalah untuk mengubah hak akses (permission) dari suatu file atau direktori pada sistem operasi berbasis Unix/Linux.
Hak akses ini mengatur siapa saja yang dapat membaca (read), menulis (write), dan menjalankan (execute) file atau direktori tersebut.
Hak akses dapat diubah menggunakan dua mode:
1.Mode Simbolik (Symbolic Mode): Menggunakan huruf (u, g, o, a) dan simbol (+, -, =).
2.Mode Numerik/Oktal (Octal Mode): Menggunakan angka tiga digit (0-7), di mana setiap digit mewakili hak akses untuk Pemilik (User), Grup (Group), dan Lainnya (Others).


2.Apa arti dari kode permission `rwxr-xr--`? Kode permission **rwxr-xr--** terdiri dari tiga segmen utama, yang masing-masing mengatur hak akses untuk Pemilik (User), Grup (Group), dan Lainnya (Others).


3.Jelaskan perbedaan antara `chown` dan `chmod`.?Meskipun keduanya digunakan untuk mengelola file dan direktori, chown dan chmod memiliki fungsi yang sangat berbeda:Fitur,chown (Change Owner),chmod (Change Mode)
Fungsi Utama,Mengubah Pemilik (Owner) dan/atau Grup (Group) dari suatu file atau direktori.,Mengubah Hak Akses (Permissions) dari suatu file atau direktori.
Apa yang Diubah,Metadata kepemilikan. Siapa yang memiliki file tersebut dan grup utama mana yang terkait dengannya.,"Aturan hak akses (read, write, execute)."
Sintaks Contoh,chown namauser:namagrup namafile,chmod 755 namafile atau chmod +x namafile
Tujuan,Menetapkan kontrol administratif atas file (siapa yang bertanggung jawab/memiliki hak tertinggi).,"Menetapkan apa yang dapat dilakukan pengguna (Pemilik, Grup, Lainnya) terhadap file."

  ## E. Output yang Diharapkan
- Hasil observasi perintah Linux dimasukkan ke dalam `laporan.md`.  
- Screenshot hasil eksekusi disimpan di `screenshots/`.  
- Laporan lengkap tersimpan di `laporan.md`.  
- Semua hasil telah di-*commit* ke GitHub tepat waktu.  

   
 
   

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?memahami konsep bab ini yang lumayann pusing untuk memahamik
- Bagaimana cara Anda mengatasinya?dengan menyeduhkan kopi di situlah saya memahami dasar konsep tentang linux 

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
