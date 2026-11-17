import numpy as np # mengandung array (kumpulan angka)
import matplotlib.pyplot as plt # membuat grafik

rng = np.random.default_rng() # default_rng = membuat generator angka secara acak

# SOAL:
# Ada 3 pintu: 1 mobil, 2 kambing. Kamu memilih satu pintu. Host (yang tahu isi semua pintu) membuka satu pintu lain yang berisi kambing. 
# Kamu boleh tetap atau ganti pintu. Mana yang lebih baik?

def main_monty_hall(ganti):
  mobil = rng.integers(3)   # mobil diletakkan
  pilihan = rng.integers(3)

  kandidat_buka = [d for d in range(3) if d != pilihan and d !=mobil]
  buka = rng.choice(kandidat_buka)

  if ganti:
    pilihan = [d for d in range (3) if d != pilihan and d != mobil][0] # [0] = 

  return pilihan == mobil # menghasilkan true jika pilihan = mobil dan false jika sebaliknya
