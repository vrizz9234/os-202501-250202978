
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

Fleksibilitas dan Kustomisasi (Penyesuaian) �️

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
