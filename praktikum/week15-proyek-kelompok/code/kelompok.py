import sys
import time

def menu_SJF():
    BAR_LENGTH = 30
    # Data: (ID, Nama File, Durasi (detik), Ukuran (MB))
    downloads = [
        (1, "Persentasi-week15.mp4", 8, 800),
        (2, "hasil-percobaan.jpg", 2, 2),
        (3, "laporan.md", 3, 3),
        (4, "musik.mp3", 5, 5)
    ]

    # SJF (Shortest Job First) → Urutkan berdasarkan durasi (indeks ke-2)
    downloads.sort(key=lambda x: x[2])

    print("\n" + "="*40)
    print(" DOWNLOAD MANAGER (SJF) ".center(40))
    print("="*40 + "\n")

    for job_id, name, duration, size in downloads:
        print(f"Memproses: {name} ({size} MB)")
        for second in range(duration + 1):
            filled = int(BAR_LENGTH * second / duration)
            bar = "█" * filled + "-" * (BAR_LENGTH - filled)
            percent = int((second / duration) * 100)
            
            # Menggunakan \r untuk animasi progress bar di satu baris
            sys.stdout.write(f"\r[{bar}] {percent}% - {second}/{duration}s")
            sys.stdout.flush()
            time.sleep(1)
        print("\nCompleted ✅\n")

    print("-" * 40)
    print("Semua download selesai.")
    print("-" * 40)

def lru_browser(tab_sequence, kapasitas):
    memory = []
    hit = 0
    fault = 0

    print("\n" + "="*40)
    print(" SIMULASI LRU BROWSER ".center(40))
    print("="*40 + "\n")

    for tab in tab_sequence:
        if tab in memory:
            # HIT: Pindahkan tab yang baru diakses ke posisi paling akhir (paling baru)
            memory.remove(tab)
            memory.append(tab)
            hit += 1
            status = "HIT → Tab masih aktif (Refresh)"
        else:
            # PAGE FAULT: Tambahkan tab baru
            fault += 1
            if len(memory) >= kapasitas:
                # Hapus tab yang paling lama tidak digunakan (indeks 0)
                memory.pop(0)
            memory.append(tab)
            status = "PAGE FAULT → Tab di-reload"

        print(f"Membuka Tab : {tab}")
        print(f"Tab Aktif   : {memory}")
        print(f"Status      : {status}\n")

    print("=== HASIL AKHIR ===")
    print(f"Total Hit      : {hit}")
    print(f"Total Fault    : {fault}")
    total_akses = hit + fault
    print(f"Hit Ratio      : {round(hit / total_akses, 2) if total_akses > 0 else 0}")
    print("-" * 40)

def browser_scenario():
    # Skenario akses tab
    tab_akses = [
        "YouTube", "Instagram", "WhatsApp",
        "YouTube", "Instagram",
        "Spotify", "YouTube"
    ]
    kapasitas = 3
    lru_browser(tab_akses, kapasitas)

def main():
    while True:
        print("\n" + "╔══════════════════════════════╗")
        print("║      MINI SIMULASI OS        ║")
        print("╠══════════════════════════════╣")
        print("║ 1. CPU Scheduling (SJF)      ║")
        print("║ 2. Page Replacement (LRU)    ║")
        print("║ 3. Keluar                    ║")
        print("╚══════════════════════════════╝")
        
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == '1':
            menu_SJF()
        elif pilihan == '2':
            browser_scenario()
        elif pilihan == '3':
            print("\nTerima kasih! Program selesai.")
            break
        else:
            print("\n❌ Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    try:
        main()
    except EOFError:
        # Menangani error jika dijalankan di Docker tanpa -it
        pass
    except KeyboardInterrupt:
        print("\nProgram dihentikan paksa.")
