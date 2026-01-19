import time

def stress_test():
    print("--- Memulai Stress Test ---")
    
    # 1. Uji CPU (Menghitung angka besar)
    print("Menguji CPU (perhitungan berat)...")
    start = time.time()
    for i in range(10**7):
        _ = i * i
    print(f"Selesai dalam: {time.time() - start:.2f} detik\n")

    # 2. Uji Memori (Alokasi bertahap)
    print("Menguji Memori (alokasi bertahap)...")
    data = []
    try:
        for i in range(1, 11):
            # Alokasi sekitar 20MB setiap tahap
            data.append(' ' * (20 * 1024 * 1024))
            print(f"Berhasil mengalokasi ~{i * 20} MB")
            time.sleep(1)
    except MemoryError:
        print("Error: Memori tidak cukup!")
    
    print("--- Test Selesai ---")

if __name__ == "__main__":
    stress_test()