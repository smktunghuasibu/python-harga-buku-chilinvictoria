buku = {
    "buku1": {"hargaRM": 6.00, "kadar_diskaun%": 10},
    "buku2": {"hargaRM": 7.50, "kadar_diskaun%": 8},
    "buku3": {"hargaRM": 8.90, "kadar_diskaun%": 5}
}
def harga_bayaran(jenisbuku, kuantiti):
    buku_key = f"buku{jenisbuku}"
    harga = buku[buku_key]["hargaRM"] 
    kadar_diskaun = buku[buku_key]["kadar_diskaun%"] 
    diskaun = harga * (kadar_diskaun / 100)
    harga_diskaun = harga - diskaun  
    jumlah_harga = harga_diskaun * kuantiti  
    return diskaun * kuantiti, jumlah_harga 
def main():
    print("Senarai belian buku:")
    print("1.Latihan Pasti A,Bahasa Melayu,Tingkatan 1")
    print("2.Latihan Pasti A,Bahasa Melayu,Tingkatan 2")
    print("3.Latihan Pasti A,Bahasa Melayu,Tingkatan 3")
    while True:
        jenisbuku = int(input("Masukkan jenis buku yang dibeli (1-3): "))
        if jenisbuku > 3 or jenisbuku < 1:
            print("Sila masukkan nombor 1 hingga 3 sahaja.")
        else:
            break # exit when no error 
    kuantiti=int(input("Masukkan kuantiti buku yang dibeli:"))
    potongan_harga,harga_total = harga_bayaran(jenisbuku,kuantiti)
    print("Potongan harga yang diperoleh ialah RM", round(potongan_harga,2))
    print("Jumlah harga yang perlu dibayar ialah RM", round(harga_total,2))
    
if __name__ == "__main__":
    main()
