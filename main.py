import streamlit as st

def angka_ke_teks(angka):
    angka_teks = {
        0: "nol", 1: "satu", 2: "dua", 3: "tiga", 4: "empat", 
        5: "lima", 6: "enam", 7: "tujuh", 8: "delapan", 9: "sembilan",
        10: "sepuluh", 11: "sebelas", 12: "dua belas", 13: "tiga belas", 
        14: "empat belas", 15: "lima belas", 16: "enam belas", 17: "tujuh belas",
        18: "delapan belas", 19: "sembilan belas", 20: "dua puluh", 
        30: "tiga puluh", 40: "empat puluh", 50: "lima puluh", 60: "enam puluh",
        70: "tujuh puluh", 80: "delapan puluh", 90: "sembilan puluh", 
        100: "seratus", 200: "dua ratus", 300: "tiga ratus", 400: "empat ratus",
        500: "lima ratus", 600: "enam ratus", 700: "tujuh ratus", 
        800: "delapan ratus", 900: "sembilan ratus", 
        1000: "seribu", 10000: "sepuluh ribu", 100000: "seratus ribu", 
        1000000: "satu juta"
    }

    if angka in angka_teks:
        return angka_teks[angka]

    if angka < 100:
        puluhan, satuan = divmod(angka, 10)
        return f"{angka_teks[puluhan * 10]} {angka_teks[satuan]}"

    if angka < 1000:
        ratusan, sisa = divmod(angka, 100)
        return f"{angka_teks[ratusan]} ratus {angka_ke_teks(sisa)}" if sisa else f"{angka_teks[ratusan]} ratus"

    if angka < 10000:
        ribuan, sisa = divmod(angka, 1000)
        return f"{angka_teks[ribuan]} ribu {angka_ke_teks(sisa)}" if sisa else f"{angka_teks[ribuan]} ribu"

    if angka < 1000000:
        ribuan, sisa = divmod(angka, 1000)
        return f"{angka_ke_teks(ribuan)} ribu {angka_ke_teks(sisa)}" if sisa else f"{angka_ke_teks(ribuan)} ribu"

    jutaan, sisa = divmod(angka, 1000000)
    return f"{angka_ke_teks(jutaan)} juta {angka_ke_teks(sisa)}" if sisa else f"{angka_ke_teks(jutaan)} juta"

def konversi_rupiah_ke_teks(nominal):
    nominal = nominal.replace("Rp", "").replace(".", "").strip()
    angka = int(nominal)
    teks = angka_ke_teks(angka)
    return f"{teks.title()} Rupiah"

st.title("Konversi Nominal Gaji ke Teks")

nominal_gaji = st.text_input("Masukkan nominal gaji (misalnya: Rp 2.486.200 atau 2486200): ")

if st.button("Konversi"):
    if nominal_gaji:
        hasil_teks = konversi_rupiah_ke_teks(nominal_gaji)
        st.write(hasil_teks)
    else:
        st.write("Harap masukkan nominal gaji.")
