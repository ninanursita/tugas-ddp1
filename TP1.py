# Nama: Nina Nursita Ramadhan
# NPM: 1606834573
# Kelas: Dasar-Dasar Pemrograman C (Dosen: Pak Hadaiq, Asdos: Kak Prakash)

# Pembuatan dictionary untuk mempermudah penerjemahan angka menjadi kata-kata

satuan  = {"0":"", "1":"satu", "2": "dua", "3":"tiga", "4":"empat", "5":"lima", "6":"enam", "7":"tujuh", "8":"delapan", "9":"sembilan"}
belasan = {"10":"sepuluh", "11":"sebelas", "12": "dua belas", "13":"tiga belas", "14":"empat belas", "15":"lima belas", "16":"enam belas", "17":"tujuh belas", 
			"18":"delapan belas", "19":"sembilan belas"}
puluhan = {"0":"", "10":"sepuluh", "20": "dua puluh", "30":"tiga puluh", "40":"empat puluh", "50":"lima puluh", "60":"enam puluh", 
			"70":"tujuh puluh", "80":"delapan puluh", "90":"sembilan puluh"}

# Pencetakan welcome message untuk user agar program menjadi lebih user-friendly

print (" ======== KONVERSI BILANGAN MENJADI KATA-KATA ========")
print ("")
print ("Halo! Selamat datang di program konversi bilangan!")
print ("Di sini, anda bisa mengubah angka menjadi kata-kata loh! Tapi gimana caranya?")
print ("Gampang! Tinggal ikutin aja nih, langkah-langkah yang ada di bawah!")
print ("")
print ("Peraturan:")
print ("1) Angka yang bisa dikonversi hanya dari 1 (satu) sampai 100000 (seratus ribu)")
print ("2) Jangan ketik angka dengan menyisipkan 0 di depannya, misal: 056 atau 0099 atau 00004")
print ("")
print ("Nah, selamat mencoba!")
print ("")

# Input angka dari user dan konversi ke string

inp = input("Masukkan angka 1 - 100000: ") 
wrd = str(inp) 

# Validasi input dari user

if inp.isdigit() == True:
    print ("Selamat, input anda valid.")

else:
    print ("Maaf, input anda tidak valid.")	

pr = "" # Setting variabel pr (puluhan ribu)
rb = "" # Setting variabel rb (ribuan)
rt = "" # Setting variabel rt (ratusan)
pl = "" # Setting variabel pl (puluhan)
st = "" # Setting variabel st (satuan)

if inp.isdigit() == True:

        print ("")
        print ("Hasil konversi dari angka yang anda masukkan: ")

        # Untuk angka berjumlah 6 digit:

        if len(wrd) == 6:
                if int(wrd) == 100000:
                        pr = "seratus ribu"
                        print (pr)
                else:
                        print ("Maaf, angka yang anda input di luar jangkauan. Cek kembali input Anda! :)")

        # Untuk angka berjumlah 5 digit

        if len(wrd) == 5:
                
                # Puluhan ribu dan ribuan

                if 20 > int(wrd[:2]) >= 10:
                        pr = belasan[wrd[:2]] + " ribu"
                if int(wrd[0] + "0") >= 20 and wrd[1] != "0": 
                        pr = (puluhan[wrd[0] + "0"]) + " " + (satuan[wrd[1]]) + " ribu " 
                if int(wrd[0] + "0") >= 20 and wrd[1] == "0": 
                        pr = (puluhan[wrd[0] + "0"]) + " ribu "
                
                # Ratusan 

                if wrd[2] != "0" and wrd[2] != "1":
                        rt = satuan[wrd[2]] + " ratus "
                if wrd[2] == "0":
                        rt = ""
                if wrd[2] == "1":
                        rt = "seratus "

                # Puluhan

                if wrd[3] != "0" and wrd[3] != "1":
                        pl = satuan[wrd[3]] + " puluh "
                if wrd[3] == "0":
                        pl = ""
                if wrd[3:] in belasan:
                        pl = belasan[wrd[3:]]
                        st = ""

                # Satuan

                if wrd[4] != "0" and wrd[3] != "1" and wrd[4] != "1" :
                        st = satuan[wrd[4]]

                print (str(pr) + str(rt) + str(pl) + str(st))

        # Untuk angka berjumlah 4  digit

        if len(wrd) == 4:

                # Ribuan

                if wrd[0] != "1":
                        rb = satuan[wrd[0]] + " ribu "
                if wrd[0] == "1":
                        rb = "seribu "

                # Ratusan

                if wrd[1] != "1" and wrd[1] != "0":
                        rt = satuan[wrd[1]] + " ratus "
                if wrd[1] == "1":
                        rt = "seratus "

                # Puluhan

                if wrd[2] != "1" and wrd[2] != "0":
                        pl = puluhan[wrd[2] + "0"] + " "
                if 20 > int(wrd[2:]) >= 10:
                        pl = belasan[wrd[2:]]
                        st = ""

                # Satuan 

                if wrd[3] != "0" and wrd[2] != "1":
                        st = satuan[wrd[3]]		 

                print (str(rb) + str(rt) + str(pl) + str(st))

        # Untuk angka berjumlah 3 digit

        if len(wrd) == 3:

                # Ratusan

                if wrd[0] != "1" and wrd[0] != "0":
                        rt = satuan[wrd[0]] + " ratus "
                if wrd[0] == "1":
                        rt = "seratus "

                # Puluhan

                if wrd[1] != "1" and wrd[1] != "0":
                        pl = puluhan[wrd[1] + "0"] + " "
                if 20 > int(wrd[1:]) >= 10:
                        pl = belasan[wrd[1:]]
                        st = ""

                # Satuan 

                if wrd[2] != "0" and wrd[2] != "1":
                        st = satuan[wrd[2]]	

                print (str(rt) + str(pl) + str(st))	

        # Untuk angka berjumlah 2 digit

        if len(wrd) == 2:

                # Puluhan

                if wrd[0] != "1" and wrd[0] != "0":
                        pl = puluhan[wrd[0] + "0"] + " "
                if 20 > int(wrd[0:]) >= 10:
                        pl = belasan[wrd[0:]]
                        st = ""

                # Satuan 

                if wrd[1] != "0" and wrd[1] != "1":
                        st = satuan[wrd[1]]	

                print (str(pl) + str(st))

        # Untuk angka berjumlah 1 digit

        if len(wrd) == 1:
                st = satuan[wrd[0]]	

                print (str(st))
