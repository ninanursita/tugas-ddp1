# Nama: Nina Nursita Ramadhan
# NPM: 1606834573
# Kelas: DDP1 - C
# Nama Asisten: Prakash Divy

# Penjelasan:
# Program ini berjalan dengan menggunakan dua file. File pertama adalah file yang diinput oleh user dan TIDAK AKAN berubah.
# File kedua adalah file untuk menuliskan hasil konversi. Penjelasan lebih lanjut ada di dalam kode.

# Tambahan:
# Masih terdapat bug seperti jumlah spasi yang kurang tepat.

############################################################################################################

#### Angka terbilang 1 ####

satuan  = {"0":"", "1":"satu", "2": "dua", "3":"tiga", "4":"empat", "5":"lima", "6":"enam", "7":"tujuh", "8":"delapan", "9":"sembilan"}
belasan = {"10":"sepuluh", "11":"sebelas", "12": "dua belas", "13":"tiga belas", "14":"empat belas", "15":"lima belas", "16":"enam belas", "17":"tujuh belas", 
			"18":"delapan belas", "19":"sembilan belas"}
puluhan = {"0":"", "10":"sepuluh", "20": "dua puluh", "30":"tiga puluh", "40":"empat puluh", "50":"lima puluh", "60":"enam puluh", 
			"70":"tujuh puluh", "80":"delapan puluh", "90":"sembilan puluh"}
desimal = {"0":"nol","1":"satu", "2": "dua", "3":"tiga", "4":"empat", "5":"lima", "6":"enam", "7":"tujuh", "8":"delapan", "9":"sembilan"}

def satu(num):

	if num.isdigit() == True:
		if len(num) == 1:
			st = desimal[num]
			return st
		else:
			if 10 <= int(num[-2:]) < 20:
				st = satuan["0"]
				return st
			else:
				st = satuan[num[-1]]
				return st

def puluh(num):

	raw_pl = num[-2:]

	if 10 <= int(raw_pl) < 20:
		pl = belasan[num[-2:]] + " "
		return pl

	if num[-1] != "0" and num[-2] != "0" and int(num[-2:]) >= 20:
		pl = puluhan[num[-2] + "0"] + " "
		return pl

	if num[-1] == "0" and num[-2] != "0":
		pl = puluhan[(num[-2] + "0")] + " "
		return pl

	if num[-2] == "0" and num[-1] != "0":
		pl = satuan[num[-1]] + " "
		return pl

	if raw_pl == "00":
		pl = "" + " "
		return pl
		
def ratus(num):
	
	if int(num[-3]) == 1:
		rt = " seratus "

	else:
		if int(num[-3]) != 0:
			rt = (satuan[num[-3]]) + " ratus "
		else:
			rt = "" + " "

	return rt

def ribu(num):

	if len(num) == 4:
		if num[0] == "1":
			rb = "seribu "
		else:
			rb = satuan[num[0]] + " ribu "

	if len(num) == 5:
		if 10 <= int(num[:2]) < 20:
			rb = belasan[num[:2]] + " ribu "
		else:
			rb = puluhan[num[0] + "0"] + " " + satuan[num[1]] + " ribu "

	return rb

def koma(num):

	hasil = ""
	part1 = ""
	part2 = ""
	
	sep = num.index(",")

	if (num[:sep] and num[sep+1:]).isdigit() == True:
		if num[0] == "0":
			part1 = "nol koma "

		else:
			if len(num[:sep]) == 5:
				part1 = (str(ribu(num[:sep]))+ " " + str(ratus(num[:sep])) + " " + str(puluh(num[:sep])) + " " + str(satu(num[:sep]))) + " koma "

			if len(num[:sep]) == 4:
				part1 = (str(ribu(num[:sep])) + " " + str(ratus(num[:sep])) + " " + str(puluh(num[:sep])) + " " + str(satu(num[:sep]))) + " koma "

			if len(num[:sep]) == 3:
				part1 = (str(ratus(num[:sep])) + " " + str(puluh(num[:sep])) + " " + str(satu(num[:sep]))) + " koma "

			if len(num[:sep]) == 2:
				part1 = (str(puluh(num[:sep])) + " " + str(satu(num[:sep]))) + " koma " 

			if len(num[:sep]) == 1:
				part1 = (str(satu(num[:sep]))) + " koma "

		for digit in num[sep+1:]:
			part2 += (desimal[digit] + " ")
			
		hasil = part1 + part2

		return hasil

############################################################################################################

#### Angka terbilang 2 ####

# Persiapan mengolah file

filename = input("Masukkan nama file: ")

openfile = open(filename, "r")

readfile = openfile.read()

filestring = str(readfile)

newstring = filestring

oldlist = newstring.split()

wordlist = oldlist

# Pengubahan string yang terdiri atas angka melalui mekanisme fungsi angka terbilang

for word in wordlist:
	if word.isdigit() == True:
		if len(word) == 5:
			wordlist[wordlist.index(word)] = (ribu(word) + ratus(word) + puluh(word) + satu(word))
		elif len(word) == 4:
			wordlist[wordlist.index(word)] = (ribu(word) + ratus(word) + puluh(word) + satu(word))
		elif len(word) == 3:
			wordlist[wordlist.index(word)] = (ratus(word) + puluh(word) + satu(word))
		elif len(word) == 2:
			wordlist[wordlist.index(word)] = (puluh(word) + satu(word))
		elif len(word) == 1:
			wordlist[wordlist.index(word)] = (satu(word))
	else:
	 	if "," in word:
	 		wordlist[wordlist.index(word)] = koma(word)

# Penggabungan hasil konversi dengan for loop. Jika ada anggota list yang ternyata tipe datanya adalah NoneType,
# tipe data akan berubah menjadi string dengan mengubah "" (string kosong) ke anggota list tersebut.

result = ""

for member in oldlist:
	try:
		result += (member + " ")
	except TypeError:
		member = ""
		continue

# Hasil konversi akan ditulis ke dalam file output.
# Mekanisme file output:
# File output akan selalu berubah mengikuti hasil konversi teks yang diinput user. 

openout = open("output.txt", "w+")
outwrite = openout.write(result)
closeout = openout.close()

# Pencetakan output dengan menampilkan teks yang diinput dan input teks yang sudah dikonversi.

print ("Teks yang anda masukkan adalah: ")
print ("")
print (readfile)
print ("")

print ("Teks hasil konversi anda: ")
print ("")
print (open("output.txt", "r").read())

# Penutupan file untuk mengurangi beban pada memori dengan mematikan (shutdown) koneksi ke file

openfile.close()
openout.close()

		
############################################################################################################
