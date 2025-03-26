# H1D023045-PraktikumKB-Pertemuan3

# Penjelasan!
Ini adalah code python minigame batu kertas gunting.


import random -> untuk memilih pilihan secara acak
import time -> untuk menambahkan jeda


pilihan = ["batu", "kertas", "gunting"] -> opsi pilihan batu kertas gunting


def main():
  print("==|| Minigame Batu, Kertas, Gunting! ||==") -> tampilan awal

    
  while True: -> membuat permainan terus berjalan sampai pemain memillih untuk berhenti bermain
    print("\nMana pilihanmu: Batu, Kertas, atau Gunting?")
    pemain = input("Pilihanmu: ").lower() -> untuk memasukkan input

        
  if pemain not in pilihan: -> pengecekan input, jika tidak benar akan menginputkan ulang
      print("Pilihanmu aneh! Coba tulis ulang.")
      continue


  komputer = random.choice(pilihan) -> komputer memilih pilihan random


  print("Tunggu bentar, komputer memilih...")
  time.sleep(1) -> menambahkan efek jeda sebelum menampilkan hasil pilihannya
  print(f"Komputer memilih: {komputer}") -> menampilkan pilihan


  if pemain == komputer: -> menentukan pilihan, jika sama maka seri
    print("Aduh, Seri!")
  elif (pemain == "batu" and komputer == "gunting") or \ -> aturan menang
    (pemain == "kertas" and komputer == "batu") or \
    (pemain == "gunting" and komputer == "kertas"):
      print("Yayy! Kamu menang!")
  else: -> jika kalah
    print("Yahh.. Kamu kalah!")


  ulang = input("Mau main lagi? (y/n): ").lower() -> apakah pemain ingin bermain lagi
  if ulang != "y": -> jika tidak maka while akan dihentikan
    print("Byee.. makasih dah main!")
    break


if __name__ == "__main__":
    main()
