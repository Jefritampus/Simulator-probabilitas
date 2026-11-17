import numpy as np # mengandung array (kumpulan angka)
import matplotlib.pyplot as plt # membuat grafik

rng = np.random.default_rng() # default_rng = membuat generator angka secara acak

# SOAL:
# Ada 3 pintu: 1 mobil, 2 kambing. Kamu memilih satu pintu. Host (yang tahu isi semua pintu) membuka satu pintu lain yang berisi kambing. 
# Kamu boleh tetap atau ganti pintu. Mana yang lebih baik?

def main_monty_hall(ganti):
  mobil = rng.integers(3)   # mobil diletakkan antara 0-2
  pilihan = rng.integers(3) # pemain memilih pintu antara 0-2

  kandidat_buka = [d for d in range(3) if d != pilihan and d !=mobil] # kandidat buka jika d tidak boleh ada di pilihan dan tidak boleh ada di mobil
  buka = rng.choice(kandidat_buka)                    

  if ganti:                                                            # jika pemain ingin mengganti
    pilihan = [d for d in range (3) if d != pilihan and d != mobil][0] # [0] = menngubah dari list menjadi angka

  return pilihan == mobil # menghasilkan true jika pilihan = mobil dan false jika sebaliknya

# SIMULASINYA
n = 10000                                                   # n = jumlah ronde, lebih besar lebih akurat (LLN), tapi lebih lambat
menang_tetap = [main_monty_hall(False) for _ in range(n)]   # memainkan simulasi dengan aturan tidak mengganti (False)
menang_ganti = [main_monty_hall(True) for _ in range(n)]    # memainkan simulasi dengan aturan selalu mengganti (True)
                                                            # _ = hanya butuh mengulang fungsinya sebanyak n tanpa memperhitungkan putaran ke-berapa
print(f"Tetap: {np.mean(menang_tetap)}")
print(f"Ganti: {np.mean(menang_ganti)}")

# GRAFIKNYA
x = np.arange(1, n + 1)                   # membuat deretan angka 1-100000
rata_ganti = np.cumsum(menang_ganti) / x  # menjumlahkan total kemenangan secara beruntun di setiap ronde. 
                                          # Hasil jumlah tersebut lalu dibagi x untuk mendapatkan proporsi kemenangan berjalan bagi strategi ganti pintu
rata_tetap = np.cumsum(menang_tetap) / x  # Melakukan perhitungan rata-rata berjalan yang sama persis untuk strategi tetap pada pilihan awal

plt.plot(x, rata_ganti, label="Ganti")    # 
plt.plot(x, rata_tetap, label="Tetap")    # 
plt.axhline(2/3, ls="--", c="purple")     # ls = garis horizontal putus putus, c = color
plt.axhline(1/3, ls="--", c="gray")       # ls = garis horizontal putus putus, c = color
plt.xlabel("Jumlah Percobaan")            # Judul sumbu
plt.ylabel("Proporsi Menang")             # Judul sumbu
plt.legend()                              # menampilkan keterangan label
plt.show()                                # menampilkan grafik
