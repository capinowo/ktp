import pandas as pd

# Membaca file CSV yang berisi data pins
def load_pins(file_path):
    return pd.read_csv(file_path)

# Fungsi yang merekomendasikan pins berdasarkan kategori secara berurutan (serial)
def recommend_pins_serial(pengguna, minat, pins_by_category):
    recommended_pins = []
    
    # Menghasilkan rekomendasi pins berdasarkan minat pengguna
    for interest in minat:
        if interest in pins_by_category:
            for pin in pins_by_category[interest]:
                print(f"Menambahkan pin {pin} dari kategori {interest}")
                recommended_pins.append(pin)
    
    # Output pin yang disukai
    return recommended_pins

# Contoh penggunaan
file_path = 'D:\Semester 5\KTP\pin_data.csv'
pins_data = load_pins(file_path)

# Mengubah dataframe menjadi dictionary {category: list of pins}
pins_by_category = pins_data.groupby('Category')['Pin'].apply(list).to_dict()

# Data input pengguna
pengguna = 'User1'
minat = ['Food', 'Gaming']  # minat pengguna

# Memanggil fungsi rekomendasi
recommended_pins = recommend_pins_serial(pengguna, minat, pins_by_category)

print("Pin yang disukai oleh", pengguna, ":", recommended_pins)
