
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : Faris Azhar  
- **NIM**   : 250202978  
- **Kelas** : 1 IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menghitung *waiting time* dan *turnaround time* pada algoritma RR dan Priority.  
2. Menyusun tabel hasil perhitungan dengan benar dan sistematis.  
3. Membandingkan performa algoritma RR dan Priority.  
4. Menjelaskan pengaruh *time quantum* dan prioritas terhadap keadilan eksekusi proses.  
5. Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.  
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
1. **Siapkan Data Proses**
   Gunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan):
   | Proses | Burst Time | Arrival Time | Priority |
   |:--:|:--:|:--:|:--:|
   | P1 | 5 | 0 | 2 |
   | P2 | 3 | 1 | 1 |
   | P3 | 8 | 2 | 4 |
   | P4 | 6 | 3 | 3 |

2. **Eksperimen 1 – Round Robin (RR)**
   - Gunakan *time quantum (q)* = 3.  
   - Hitung *waiting time* dan *turnaround time* untuk tiap proses.  
   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).  
     ```
     | P1 | P2 | P3 | P4 | P1 | P3 | ...
     0    3    6    9   12   15   18  ...
     ```
   - Catat sisa *burst time* tiap putaran.

3. **Eksperimen 2 – Priority Scheduling (Non-Preemptive)**
   - Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).  
   - Lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]
     ```
   - Buat tabel perbandingan hasil RR dan Priority.

4. **Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**
   - Ubah *quantum* menjadi 2 dan 5.  
   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.  
   - Buat tabel perbandingan efek *quantum*.

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua hasil tabel dan screenshot ke:
     ```
     praktikum/week6-scheduling-rr-priority/screenshots/
     ```
   - Buat tabel perbandingan seperti berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | ... | ... | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | ... | ... | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
   git push origin main
   ```


---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![alt text](<screenshots/Screenshot 2025-11-25 133846.png>)
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
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling?

| Fitur | Round Robin (RR) | Priority Scheduling (PS) |
|-------|------------------|--------------------------|
| **Kriteria Utama** | Waktu (Time Quantum). Setiap proses mendapatkan jatah waktu CPU yang sama (disebut time quantum atau kuanta waktu) secara bergilir. | Prioritas. Proses dengan prioritas tertinggi akan dieksekusi terlebih dahulu. |
| **Antrian** | Antrian melingkar (Circular Queue). Proses yang dihentikan (karena kuanta waktu habis) kembali ke belakang antrian. | Antrian dapat diurutkan berdasarkan prioritas. Proses baru dengan prioritas lebih tinggi dapat menyela proses yang sedang berjalan (preemptif). |
| **Keadilan (Fairness)** | **Adil (Fair)**, karena setiap proses dijamin mendapat waktu CPU secara berkala. | **Kurang adil**, karena proses berprioritas rendah bisa menunggu lama atau bahkan tidak terproses. |
| **Penggunaan** | Didesain untuk sistem *time-sharing* (berbagi waktu) untuk memberikan waktu respons yang cepat. | Didesain untuk sistem yang memerlukan proses krusial (prioritas tinggi) untuk diselesaikan secepatnya. |

2.Apa pengaruh besar/kecilnya *time quantum* terhadap performa sistem?
Pengaruh Besar/Kecilnya Time Quantum pada Performa Round RobinDalam Round Robin, time quantum (q) adalah kunci yang sangat memengaruhi performa sistem:

Jika Time Quantum ($q$) Terlalu Besar:
- Sistem akan cenderung berperilaku seperti algoritma First-Come, First-Served (FCFS).
- Keuntungan: Jumlah context switch (pengalihan proses) menjadi lebih sedikit, sehingga overhead CPU (waktu yang dihabiskan untuk switching) berkurang.
- Kelemahan: Waktu respons (response time) akan menjadi lebih lama, terutama untuk proses-proses kecil, karena proses lain yang lebih besar mungkin menghabiskan seluruh kuanta waktunya.
Jika Time Quantum ($q$) Terlalu Kecil:
- Sistem akan menjadi sangat responsif, memberikan kesan setiap proses berjalan bersamaan.
- Keuntungan: Waktu respons menjadi lebih cepat.
- Kelemahan: Jumlah context switch akan meningkat tajam, menyebabkan overhead CPU yang sangat besar. CPU akan lebih banyak menghabiskan waktu untuk berganti proses daripada benar-benar mengeksekusi instruksi proses, sehingga utilisasi CPU yang sebenarnya menurun.

3.Mengapa algoritma Priority dapat menyebabkan *starvation*?  

Starvation (kelaparan) adalah kondisi di mana suatu proses tidak pernah mendapatkan alokasi CPU dan menunggu tanpa batas waktu untuk dieksekusi.

Priority Scheduling dapat menyebabkan starvation karena:

1.Prioritas Tinggi Selalu Mendominasi: Jika ada aliran konstan proses-proses baru yang masuk ke sistem dengan prioritas yang lebih tinggi daripada proses yang sudah menunggu, maka proses berprioritas rendah tersebut akan terus-menerus disela (dalam mode preemptif) atau selalu didahului (dalam mode non-preemptif).

2.Penantian Tak Terbatas: Proses berprioritas rendah tersebut akan tertahan di ready queue (antrian siap) dan tidak pernah mendapat giliran untuk dieksekusi, sehingga mengalami starvation.

Solusi untuk Starvation: Mekanisme Aging (penuaan) sering digunakan untuk mengatasi masalah ini. Aging adalah teknik yang secara bertahap meningkatkan prioritas dari proses yang telah menunggu terlalu lama di dalam sistem. Dengan demikian, proses yang awalnya berprioritas rendah pada akhirnya akan mencapai prioritas yang cukup tinggi untuk dieksekusi, mencegah starvation.





---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
