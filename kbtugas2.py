import random
import time

pilihan = ["batu", "kertas", "gunting"]

def main():
    print("==|| Minigame Batu, Kertas, Gunting! ||==")

    while True:
        print("\nMana pilihanmu: Batu, Kertas, atau Gunting?")
        pemain = input("Pilihanmu: ").lower()
        
        if pemain not in pilihan:
            print("Pilihanmu aneh! Coba tulis ulang.")
            continue

        komputer = random.choice(pilihan)

        print("Tunggu bentar, komputer memilih...")
        time.sleep(1)
        print(f"Komputer memilih: {komputer}")

        if pemain == komputer:
            print("Aduh, Seri!")
        elif (pemain == "batu" and komputer == "gunting") or \
             (pemain == "kertas" and komputer == "batu") or \
             (pemain == "gunting" and komputer == "kertas"):
            print("Yayy! Kamu menang!")
        else:
            print("Yahh.. Kamu kalah!")

        ulang = input("Mau main lagi? (y/n): ").lower()
        if ulang != "y":
            print("Byee.. makasih dah main!")
            break

if __name__ == "__main__":
    main()
