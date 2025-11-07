
# Laporan Praktikum Minggu 5
Topik: Penjadwalan CPU – FCFS dan SJF

---

## Identitas
- **Nama**  : Faris Azhar
- **NIM**   : 250202978 
- **Kelas** : 1 IKRA
---

## Tujuan
1. Menghitung *waiting time* dan *turnaround time* untuk algoritma FCFS dan SJF.  
2. Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.  
3. Membandingkan performa FCFS dan SJF berdasarkan hasil analisis.  
4. Menjelaskan kelebihan dan kekurangan masing-masing algoritma.  
5. Menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan.  
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
   Gunakan tabel proses berikut sebagai contoh (boleh dimodifikasi dengan data baru):
   | Proses | Burst Time | Arrival Time |
   |:--:|:--:|:--:|
   | P1 | 6 | 0 |
   | P2 | 8 | 1 |
   | P3 | 7 | 2 |
   | P4 | 3 | 3 |

2. **Eksperimen 1 – FCFS (First Come First Served)**
   - Urutkan proses berdasarkan *Arrival Time*.  
   - Hitung nilai berikut untuk tiap proses:
     ```
     Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
     Turnaround Time (TAT) = WT + Burst Time
     ```
   - Hitung rata-rata Waiting Time dan Turnaround Time.  
   - Buat Gantt Chart sederhana:  
     ```
     | P1 | P2 | P3 | P4 |
     0    6    14   21   24
     ```

3. **Eksperimen 2 – SJF (Shortest Job First)**
   - Urutkan proses berdasarkan *Burst Time* terpendek (dengan memperhatikan waktu kedatangan).  
   - Lakukan perhitungan WT dan TAT seperti langkah sebelumnya.  
   - Bandingkan hasil FCFS dan SJF pada tabel berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | FCFS | ... | ... | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
     | SJF | ... | ... | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |
4. **Eksperimen 3 – Visualisasi Spreadsheet (Opsional)**
   - Gunakan Excel/Google Sheets untuk membuat perhitungan otomatis:
     - Kolom: Arrival, Burst, Start, Waiting, Turnaround, Finish.
     - Gunakan formula dasar penjumlahan/subtraksi.
   - Screenshot hasil perhitungan dan simpan di:
     ```
     praktikum/week5-scheduling-fcfs-sjf/screenshots/
     ```

5. **Analisis**
   - Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.
   *FCFS
   - Waiting Time:8,75
   - Turnaround Time:14,75
   *SJF
   - Waiting Time:6,25
   - Turnaround Time:12,25
     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | FCFS | 8,75 | 14,75 | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
     | SJF | 6,25 | 12,25 | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |
     
   - Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.
     SJF Lebih Unggul dari FCFS
     SJF (Shortest Job First) biasanya lebih unggul dari FCFS dalam hal metrik kinerja seperti Waktu Tunggu (Waiting Time) dan Waktu Penyelesaian (Turnaround           Time), seperti yang tercermin dalam data Anda (SJF memiliki waktu tunggu 6,25 dan turnaround time 12,25, yang lebih rendah dari FCFS) dan sebaliknya FCFS          Lebih Unggul dari SJF
     Meskipun SJF unggul secara metrik rata-rata, FCFS (First-Come, First-Served) dapat dianggap lebih unggul dalam kondisi tertentu, terutama terkait                  implementasi dan keadilan (fairness).
     Kondisi Unggul FCFS:
     Implementasi Sederhana: FCFS jauh lebih mudah diimplementasikan karena hanya membutuhkan queue (antrian) sederhana dan tidak perlu memprediksi atau                mengetahui waktu burst CPU proses sebelumnya.    
   - Tambahkan kesimpulan singkat di akhir laporan.
   - SJF lebih unggul dari FCFS
  
   

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 5 - CPU Scheduling FCFS & SJF"
   git push origin main
   ```
## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![alt text](<screenshots/excellinux.png>)

---

## Tugas
1. Hitung *waiting time* dan *turnaround time* dari minimal 2 skenario FCFS dan SJF.

  - FCFS Pertama
1.Skenario 1

| Proses | Arrival Time | Burst Time |
| :----: | :----------: | :--------: |
|   P1   |       0      |      5     |
|   P2   |       1      |      3     |
|   P3   |       2      |      8     |
|   P4   |       3      |      6     |

- FCFS (First Come First Serve)

| Proses | Arrival | Burst | Start | Finish | Waiting Time | Turnaround Time |
| :----: | :-----: | :---: | :---: | :----: | :----------: | :-------------: |
|   P1   |    0    |   5   |   0   |    5   |     0−0=0    |      5−0=5      |
|   P2   |    1    |   3   |   5   |    8   |     5−1=4    |      8−1=7      |
|   P3   |    2    |   8   |   8   |   16   |     8−2=6    |     16−2=14     |
|   P4   |    3    |   6   |   16  |   22   |    16−3=13   |     22−3=19     |

Rata-rata:

Waiting Time = (0 + 4 + 6 + 13) / 4 = 5.75

Turnaround Time = (5 + 7 + 14 + 19) / 4 = 11.25

- SJF (Shortest Job First, Non-preemptive)

| Urutan | Proses | Arrival | Burst | Start | Finish |    WT   |   TAT   |
| :----: | :----: | :-----: | :---: | :---: | :----: | :-----: | :-----: |
|    1   |   P1   |    0    |   5   |   0   |    5   |  0−0=0  |  5−0=5  |
|    2   |   P2   |    1    |   3   |   5   |    8   |  5−1=4  |  8−1=7  |
|    3   |   P4   |    3    |   6   |   8   |   14   |  8−3=5  | 14−3=11 |
|    4   |   P3   |    2    |   8   |   14  |   22   | 14−2=12 | 22−2=20 |

Rata-rata:

Waiting Time = (0 + 4 + 5 + 12) / 4 = 5.25

Turnaround Time = (5 + 7 + 11 + 20) / 4 = 10.75

2.Skenario 2

| Proses | Arrival Time | Burst Time |
| :----: | :----------: | :--------: |
|   P1   |       0      |      6     |
|   P2   |       2      |      2     |
|   P3   |       4      |      4     |


- FCFS (First Come First Serve)

| Proses | Arrival | Burst | Start | Finish |   WT  |   TAT  |
| :----: | :-----: | :---: | :---: | :----: | :---: | :----: |
|   P1   |    0    |   6   |   0   |    6   |   0   |    6   |
|   P2   |    2    |   2   |   6   |    8   | 6−2=4 |  8−2=6 |
|   P3   |    4    |   4   |   8   |   12   | 8−4=4 | 12−4=8 |

Rata-rata:

Waiting Time = (0 + 4 + 4) / 3 = 2.67

Turnaround Time = (6 + 6 + 8) / 3 = 6.67

- SJF (Non-preemptive)

| Urutan | Proses | Arrival | Burst | Start | Finish |   WT  |   TAT  |
| :----: | :----: | :-----: | :---: | :---: | :----: | :---: | :----: |
|    1   |   P1   |    0    |   6   |   0   |    6   |   0   |    6   |
|    2   |   P2   |    2    |   2   |   6   |    8   | 6−2=4 |  8−2=6 |
|    3   |   P3   |    4    |   4   |   8   |   12   | 8−4=4 | 12−4=8 |

Karena urutannya sama dengan FCFS (karena proses P2 baru datang setelah P1 selesai), maka:

WT rata-rata = 2.67

TAT rata-rata = 6.67

- Ringkasan Akhir
  
| Algoritma | Skenario | Avg WT | Avg TAT |
| :-------- | :------- | :----: | :-----: |
| FCFS      | 1        |  5.75  |  11.25  |
| SJF       | 1        |  5.25  |  10.75  |
| FCFS      | 2        |  2.67  |   6.67  |
| SJF       | 2        |  2.67  |   6.67  |

2. Sajikan hasil perhitungan dalam tabel perbandingan (FCFS vs SJF).

Eksperimen 1 – FCFS (First Come First Served)
|    Proses   | Burst Time | Arrival Time | Start Time | Finish Time | Waiting Time | Turnaround Time |
| :---------: | :--------: | :----------: | :--------: | :---------: | :----------: | :-------------: |
|      P1     |      6     |       0      |      0     |      6      |       0      |        6        |
|      P2     |      8     |       1      |      6     |      14     |       5      |        13       |
|      P3     |      7     |       2      |     14     |      21     |      12      |        19       |
|      P4     |      3     |       3      |     21     |      24     |      18      |        21       |
|  **Total**  |            |              |            |             |    **35**    |      **59**     |
| **Average** |            |              |            |             |   **8.75**   |    **14.75**    |

Eksperimen 2 – SJF (Shortest Job First)

|    Proses   | Arrival Time | Burst Time | Start Time | Finish Time | Waiting Time | Turnaround Time |
| :---------: | :----------: | :--------: | :--------: | :---------: | :----------: | :-------------: |
|      P1     |       0      |      6     |      0     |      6      |       0      |        6        |
|      P2     |       3      |      3     |      6     |      9      |       3      |        6        |
|      P3     |       2      |      7     |      9     |      16     |       7      |        14       |
|      P4     |       1      |      8     |     16     |      24     |      15      |        23       |
|  **Total**  |              |            |            |             |    **25**    |      **49**     |
| **Average** |              |            |            |             |   **6.25**   |    **12.25**    |

Kesimpulan:

FCFS memiliki rata-rata Waiting Time 8.75 dan Turnaround Time 14.75.

SJF memiliki rata-rata Waiting Time 6.25 dan Turnaround Time 12.25.

Artinya, SJF lebih efisien dibanding FCFS karena menghasilkan waktu tunggu dan penyelesaian lebih rendah.

3. Analisis kelebihan dan kelemahan tiap algoritma.
## Analisis Kelebihan dan Kelemahan Algoritma Populer

| **Algoritma**                   | **Kategori**                                        | **Kelebihan Utama (Strengths)**                                                                                                                                   | **Kelemahan Utama (Weaknesses)**                                                                                                                                                                    |
| :------------------------------ | :-------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **K-Means**                     | Clustering (Pengelompokan)                          | Sederhana dan mudah diimplementasikan. Skalabel untuk dataset besar.                                                                                              | Wajib menentukan jumlah cluster (k) di awal. Sensitif terhadap outlier dan inisialisasi centroid awal. Sulit untuk cluster dengan ukuran/kepadatan berbeda.                                         |
| **Decision Tree (C4.5/CART)**   | Classification & Regression (Klasifikasi & Regresi) | Mudah dipahami dan diinterpretasikan (mirip alur keputusan manusia). Tidak memerlukan penskalaan/normalisasi data. Mampu menangani data kategorikal dan numerik.  | Rentan terhadap overfitting, terutama jika pohon terlalu dalam/kompleks. Ketidakstabilan (sensitif terhadap perubahan kecil dalam data).                                                            |
| **K-Nearest Neighbor (K-NN)**   | Classification & Regression                         | Sederhana dan fleksibel untuk data dengan distribusi non-linier. Tidak memerlukan asumsi distribusi data.                                                         | Memerlukan memori besar (menyimpan semua data training). Lambat saat proses prediksi jika dataset besar (karena harus menghitung jarak ke semua titik). Sensitif terhadap fitur yang tidak relevan. |
| **Naïve Bayes**                 | Classification                                      | Sangat cepat dan efisien untuk data besar. Bekerja dengan baik pada data dengan dimensi tinggi (seperti klasifikasi teks). Sederhana dan mudah diimplementasikan. | Berasumsi bahwa semua fitur independen secara kondisional, yang jarang terjadi di dunia nyata. Akurasi bisa lebih rendah jika asumsi independensi dilanggar.                                        |
| **Apriori**                     | Association Rule Mining (Aturan Asosiasi)           | Mudah dipahami dan diimplementasikan. Efektif untuk menemukan pola (frequent itemset) yang berharga.                                                              | Kinerja lambat pada dataset yang sangat besar karena harus menghitung banyak kombinasi item (candidate generation). Konsumsi memori tinggi untuk menyimpan semua candidate yang mungkin.            |
| **Boosting (XGBoost/LightGBM)** | Ensemble Learning                                   | Akurasi tinggi dan performa superior di banyak kompetisi data science. Mampu mengurangi bias dan variance.                                                        | Proses pelatihan bisa lambat dan membutuhkan sumber daya komputasi yang besar. Rentan terhadap overfitting jika parameter tidak diatur dengan benar (terutama learning rate).                       |

4. Simpan seluruh hasil dan analisis ke `laporan.md`.  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
1.
---

## Quiz
1. Apa perbedaan utama antara FCFS dan SJF?

| **Kriteria**      | **FCFS (First-Come, First-Served)**                                                                                          | **SJF (Shortest Job First)**                                                                          |
| :---------------- | :--------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------- |
| **Prinsip Dasar** | Proses yang tiba di *ready queue* pertama kali dilayani terlebih dahulu.                                                     | Proses dengan waktu eksekusi (*CPU burst*) terpendek dilayani terlebih dahulu.                        |
| **Sifat**         | Non-Preemptive (umumnya). Sekali proses dimulai, ia berjalan sampai selesai tanpa interupsi.                                 | Bisa **Non-Preemptive** atau **Preemptive** (dikenal sebagai *Shortest Remaining Time First / SRTF*). |
| **Kinerja**       | Menghasilkan waktu tunggu rata-rata yang lebih lama, terutama jika ada proses panjang yang datang di awal (*Convoy Effect*). | Menghasilkan waktu tunggu rata-rata yang minimum (optimal) untuk sekumpulan proses.                   |
| **Implementasi**  | Sangat sederhana (mirip antrian FIFO).                                                                                       | Lebih kompleks karena memerlukan estimasi waktu *CPU burst* yang akan datang.                         |



2. Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?
SJF dikenal sebagai algoritma penjadwalan yang optimal karena menghasilkan rata-rata waktu tunggu (Average Waiting Time - AWT) yang paling kecil untuk sekumpulan proses yang diberikan.

- 1.Prioritas pada Proses Singkat: SJF secara inheren memprioritaskan proses dengan waktu eksekusi (burst time) terpendek.

- 2.Mengurangi Penundaan: Dengan melayani proses singkat terlebih dahulu, SJF memastikan bahwa proses-proses ini tidak perlu menunggu lama (waiting time yang 
singkat) di belakang proses yang sangat panjang.

- 3.Dampak Kolektif: Meskipun proses yang panjang mungkin harus menunggu lebih lama, "penghematan" total waktu tunggu yang dihasilkan dari penyelesaian banyak proses singkat secara cepat lebih besar daripada penalti waktu tunggu tambahan pada proses panjang.

Secara matematis, memindahkan proses yang lebih pendek di depan proses yang lebih panjang akan mengurangi total waktu tunggu yang dialami oleh semua proses secara 
keseluruhan, sehingga rata-rata waktu tunggu menjadi minimum.

3. Apa kelemahan SJF jika diterapkan pada sistem interaktif?
Sistem interaktif (seperti sistem operasi desktop modern atau timesharing) sangat bergantung pada responsivitas dan keadilan (fairness). SJF memiliki kelemahan signifikan dalam konteks ini:

- 1. Kesulitan Estimasi Burst Time:
Di sistem interaktif, OS tidak dapat mengetahui secara pasti berapa lama waktu burst CPU yang dibutuhkan oleh suatu proses yang baru datang. SJF memerlukan estimasi yang akurat dari waktu eksekusi berikutnya, yang mustahil dilakukan secara sempurna. Sistem hanya bisa memprediksi menggunakan rata-rata eksponensial dari perilaku masa lalu.

- 2. Masalah Starvation:
Ini adalah kelemahan terbesar SJF (terutama non-preemptive). Proses dengan waktu eksekusi (burst time) yang sangat panjang mungkin tidak akan pernah dieksekusi jika ada aliran proses-proses baru yang terus-menerus datang dengan waktu burst yang lebih pendek. Dalam sistem interaktif, proses yang tidak pernah mendapat respons akan membuat pengguna frustrasi.

- 3. Mengabaikan Response Time:
Meskipun SJF meminimalkan waiting time rata-rata, algoritma ini tidak menjamin response time (waktu tanggap) yang cepat dan konsisten untuk semua proses. Sistem interaktif memerlukan response time yang rendah dan seragam untuk menjaga interaksi pengguna tetap lancar.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
