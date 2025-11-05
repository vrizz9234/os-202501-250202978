
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
![alt text](<screenshots/code sleep.png>)
![alt text](<screenshots/code sleep2.png>)

---

## Analisis
1.hasilkan hiearki proses dalam bentuk diagram pohon
systemd(1)-+-agetty(190)
           |-agetty(198)
           |-cron(155)
           |-dbus-daemon(156)
           |-init-systemd(Ub(2)-+-SessionLeader(305)---Relay(307)(306)---bash(307)-+-head(1150)
           |                    |                                                  `-pstree(1149)
           |                    |-init(7)---{init}(8)
           |                    |-login(308)---bash(376)
           |                    `-{init-systemd(Ub}(9)
           |-packagekitd(974)-+-{packagekitd}(975)
           |                  |-{packagekitd}(976)
           |                  `-{packagekitd}(977)
           |-polkitd(979)-+-{polkitd}(981)
           |              |-{polkitd}(982)
           |              `-{polkitd}(983)
           |-rsyslogd(192)-+-{rsyslogd}(216)
           |               |-{rsyslogd}(217)
           |               `-{rsyslogd}(219)
           |-systemd(354)---(sd-pam)(356)
           |-systemd-journal(43)

2.Hubungan antara Manajemen User dan Keamanan Sistem Linux sangatlah fundamental dan bersifat langsung. Manajemen user adalah dasar dari keamanan Linux karena ia menentukan siapa yang dapat mengakses sistem dan apa yang dapat mereka lakukan.

Ini adalah perwujudan dari Prinsip Hak Akses Paling Rendah (Principle of Least Privilege/PoLP), di mana setiap pengguna (user) dan proses hanya diberi hak akses minimal yang mereka butuhkan untuk menjalankan tugasnya.

Berikut adalah poin-poin utama yang menjelaskan hubungan tersebut:

 1. Kontrol Akses (Authentication & Authorization)
Manajemen user menyediakan mekanisme kontrol dua langkah yang krusial untuk keamanan:

Autentikasi: Dengan mewajibkan setiap user memiliki kata sandi (password) yang kuat dan unik, sistem memastikan bahwa hanya individu yang berwenang (yang mengetahui kredensial) yang dapat masuk (login). Ini mencegah akses tidak sah ke sistem.

Otorisasi: Setelah user terautentikasi, sistem user dan grup menentukan hak (permission) apa yang dimilikinya. Misalnya, user biasa tidak diizinkan mengakses atau mengubah file konfigurasi sistem, yang hanya bisa dilakukan oleh Superuser (root).

 2. Manajemen Hak Akses File (Permissions)
Setiap file dan direktori di Linux memiliki kepemilikan (ownership) oleh seorang user dan satu grup. Manajemen user memungkinkan Administrator untuk:

Pembatasan: Menggunakan perintah seperti chmod dan chown, Administrator dapat mengatur hak baca (r), tulis (w), dan eksekusi (x) secara spesifik untuk Owner, Grup, dan Others.

Pencegahan Perubahan Tidak Sah: Dengan pembatasan hak akses, user biasa tidak dapat memodifikasi atau menghapus file sistem yang penting (misalnya, file di direktori /etc), sehingga mencegah kerusakan sistem yang tidak disengaja maupun serangan berbahaya.

 3. Isolasi User Biasa dan Akun Root
Pemisahan Tugas: Manajemen user secara ketat memisahkan akun root (yang memiliki hak akses penuh/tidak terbatas) dari akun user biasa.

Pengurangan Risiko: Dalam praktik keamanan terbaik, user tidak disarankan untuk bekerja menggunakan akun root. Sebaliknya, mereka menggunakan akun user biasa dan hanya menggunakan perintah sudo (Superuser Do) untuk menjalankan perintah yang memerlukan hak administratif. Hal ini mengurangi risiko jika akun user biasa disusupi, karena penyerang hanya mendapatkan akses terbatas (bukan akses penuh sistem).

 4. Audit dan Akuntabilitas
Pelacakan Aktivitas: Setiap tindakan yang dilakukan di sistem Linux (seperti login, modifikasi file, dan perintah sudo) dicatat dalam log sistem. Karena setiap aktivitas dikaitkan dengan User ID (UID) tertentu, manajemen user yang baik memungkinkan Administrator untuk melacak siapa yang melakukan apa, dan kapan.

Akuntabilitas: Kemampuan untuk mengaudit aktivitas ini sangat penting untuk mendeteksi ancaman, menginvestigasi insiden keamanan, dan menegakkan akuntabilitas di antara pengguna sistem.
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
