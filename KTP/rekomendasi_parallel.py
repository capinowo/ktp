import pandas as pd
from math import ceil

# Membaca file CSV yang berisi data pins
def load_pins(file_path):
    return pd.read_csv(file_path)

# Fungsi yang merekomendasikan pins berdasarkan minat pengguna
def rekomendasi_pins_paralel(pengguna, minat, pins_by_category, num_threads):
    # Membagi minat pengguna menjadi batch paralel berdasarkan jumlah thread
    chunk_size = max(1, ceil(len(minat) / num_threads))
    user_interest_batches = [minat[i:i + chunk_size] for i in range(0, len(minat), chunk_size)]
    
    recommended_pins = []
    
    # Memproses batch minat pengguna
    for thread_id, batch in enumerate(user_interest_batches, start=1):
        print(f"Thread {thread_id} memproses minat: {batch}")
        hasil_batch = rekomendasi_pins_per_batch(thread_id, batch, pins_by_category)
        recommended_pins.extend(hasil_batch)
    
    # Output pin yang disukai
    return recommended_pins

# Fungsi yang menangani rekomendasi pins per batch minat
def rekomendasi_pins_per_batch(thread_id, batch, pins_by_category):
    hasil_batch = []
    for interest in batch:
        if interest in pins_by_category:
            for pin in pins_by_category[interest]:
                print(f"Thread {thread_id} menambahkan pin {pin} dari kategori {interest}")
                hasil_batch.append(pin)
    return hasil_batch

# Contoh penggunaan
file_path = 'D:\Semester 5\KTP\pin_data.csv'
pins_data = load_pins(file_path)

# Mengubah dataframe menjadi dictionary {category: list of pins}
pins_by_category = pins_data.groupby('Category')['Pin'].apply(list).to_dict()

# Data input pengguna
pengguna = 'User1'
minat = ['Food', 'Gaming']  # minat pengguna
num_threads = 2  # jumlah threads

# Memanggil fungsi rekomendasi
recommended_pins = rekomendasi_pins_paralel(pengguna, minat, pins_by_category, num_threads)

print("Pin yang disukai oleh", pengguna, ":", recommended_pins)
