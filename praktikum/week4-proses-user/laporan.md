
# Laporan Praktikum Minggu [X]
Topik: Manajemen Proses dan User di Linux 

---

## Identitas
- **Nama**  : Faris Azhar  
- **NIM**   : 250202978  
- **Kelas** : 1 IKRA

---

## Tujuan
1. Menjelaskan konsep proses dan user dalam sistem operasi Linux.  
2. Menampilkan daftar proses yang sedang berjalan dan statusnya.  
3. Menggunakan perintah untuk membuat dan mengelola user.  
4. Menghentikan atau mengontrol proses tertentu menggunakan PID.  
5. Menjelaskan kaitan antara manajemen user dan keamanan sistem.  

---

## Dasar Teori
Manajemen proses adalah fungsi utama dari kernel Linux yang bertugas untuk mengelola pembuatan, penjadwalan, dan penghentian program yang sedang berjalan (proses).
Proses (Process): Adalah program yang sedang dieksekusi. Setiap kali Anda menjalankan perintah atau aplikasi, satu atau lebih proses akan dibuat.
PID (Process ID): Setiap proses memiliki nomor identifikasi unik (PID) yang digunakan oleh kernel untuk melacak dan berinteraksi dengan proses tersebut.
PPID (Parent Process ID): ID dari proses yang menciptakan proses saat ini (proses induk).
Penjadwalan Proses (Process Scheduling): Kernel (biasanya menggunakan Completely Fair Scheduler/CFS) bertanggung jawab membagi waktu CPU secara adil kepada setiap proses berdasarkan prioritasnya.
Pengendalian Proses: Anda dapat mengontrol proses, seperti:
Melihat Proses: Menggunakan perintah seperti ps (menampilkan snapshot proses saat ini) atau top (menampilkan daftar proses secara real-time).
Menghentikan Proses: Menggunakan perintah kill diikuti dengan PID untuk mengirim sinyal ke proses. Sinyal yang umum adalah SIGTERM (penghentian normal) dan SIGKILL (penghentian paksa, menggunakan kill -9).

Manajemen user adalah aspek penting dalam administrasi sistem Linux yang berkaitan dengan mengelola akun pengguna dan hak aksesnya. Ini bertujuan untuk memastikan keamanan, efisiensi, dan pembagian sumber daya yang tepat.
Konsep Dasar: Linux adalah sistem multi-user, yang berarti banyak pengguna dapat mengakses sistem secara bersamaan. Setiap pengguna memiliki UID (User ID) unik dan berada dalam setidaknya satu Grup, yang juga memiliki GID (Group ID).
Tujuan Utama:
Keamanan: Mengontrol siapa yang dapat mengakses sistem dan sumber daya tertentu (prinsip least privilege).
Akses Sumber Daya: Membagi akses ke file, direktori, dan perangkat keras.
Perintah Utama untuk Administrasi User:
useradd atau adduser: Untuk membuat user baru.
usermod: Untuk memodifikasi properti user yang sudah ada (misalnya, menambahkan ke grup lain).
passwd: Untuk mengubah password user.
userdel: Untuk menghapus user.
groupadd: Untuk membuat grup baru.

Manajemen user sangat erat kaitannya dengan hak akses (permission) file, di mana hak baca (r), tulis (w), dan eksekusi (x) diberikan kepada pemilik file (owner), grup, dan user lain (others).
---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).  
   - Pastikan Anda sudah login sebagai user non-root.  
   - Siapkan folder kerja:
     ```
     praktikum/week4-proses-user/
     ```

2. **Eksperimen 1 – Identitas User**
   Jalankan perintah berikut:
   ```bash
   whoami
   id
   groups
   ```
   - Jelaskan setiap output dan fungsinya.  
   - Buat user baru (jika memiliki izin sudo):
     ```bash
     sudo adduser praktikan
     sudo passwd praktikan
     ```
   - Uji login ke user baru.

3. **Eksperimen 2 – Monitoring Proses**
   Jalankan:
   ```bash
   ps aux | head -10
   top -n 1
   ```
   - Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.  
   - Simpan tangkapan layar `top` ke:
     ```
     praktikum/week4-proses-user/screenshots/top.png
     ```

4. **Eksperimen 3 – Kontrol Proses**
   - Jalankan program latar belakang:
     ```bash
     sleep 1000 &
     ps aux | grep sleep
     ```
   - Catat PID proses `sleep`.  
   - Hentikan proses:
     ```bash
     kill <PID>
     ```
   - Pastikan proses telah berhenti dengan `ps aux | grep sleep`.

5. **Eksperimen 4 – Analisis Hierarki Proses**
   Jalankan:
   ```bash
   pstree -p | head -20
   ```
   - Amati hierarki proses dan identifikasi proses induk (`init`/`systemd`).  
   - Catat hasilnya dalam laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 4 - Manajemen Proses & User"
   git push origin main
   ```


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
  ```bash
   whoami
   id
   groups
   ```
```bash
sudo adduser praktikan
sudo passwd praktikan
 ```
 ```bash
 ps aux | head -10
 top -n 1
 ```
 ```bash
 sleep 1000 &
 ps aux | grep sleep
 ```
 ```bash
 kill <PID>
 ```
 ```bash
 pstree -p | head -20
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
