# A. Penggunaan defaultdict untuk mengeset tipe data dari values yang ada pada dictionary
from collections import defaultdict

# B. Pengesetan tipe data standar untuk values dari dictionary
classes = defaultdict(list)
quiz1 = defaultdict(int)
quiz2 = defaultdict(int)
task1 = defaultdict(int)
task2 = defaultdict(int)
task3 = defaultdict(int)
test1 = defaultdict(int)
test2 = defaultdict(int)

# C. Pembuatan variabel untuk persiapan
# NAMES berfungsi sebagai database nama-nama yang ada di seluruh kelas
names = []
# TEMP adalah variabel temporary untuk mengolah input
# TEMP berfungsi memisahkan command dengan input yang akan diolah
temp = []
# SUBTEMP adalah variabel yang murni berisikan input dari user
# SUBTEMP akan displit menjadi tiga bagian, yaitu nama, tipe berkas, dan nilai
subtemp = ""
# SMALLTEMP adalah versi lebih kecil dari SUBTEMP yang dikhususkan untuk mengolah nilai pada fungsi
smalltemp = []
#AVG_(berkas) merupakan variabel storage nilai rata-rata
avg_quiz = 0
avg_task = 0
avg_test = 0
final = 0
current = 0

#D. Fungsi pengolah untuk command UPDATE

def process2(subtemp,smalltemp,dict1,dict2):
	if subtemp[2][0] != "," and subtemp[2][1] != ",":
		try:
			dict1[subtemp[0]] = smalltemp[0]
			dict2[subtemp[0]] = smalltemp[1]
		except IndexError:
			dict1[subtemp[0]] = smalltemp[0]

	elif subtemp[2][0] == "," and subtemp[2][1] != ",":
		dict2[subtemp[0]] = smalltemp[1]

def process3(subtemp,smalltemp,dict1,dict2,dict3):
	if subtemp[2][0] != "," and subtemp[2][1] != ",":
		try:
			dict1[subtemp[0]] = smalltemp[0]
			dict2[subtemp[0]] = smalltemp[1]
			dict3[subtemp[0]] = smalltemp[2]
		except IndexError:
			dict1[subtemp[0]] = smalltemp[0]

	elif subtemp[2][0] == "," and subtemp[2][1] != ",":
		dict2[subtemp[0]] = smalltemp[1]

	elif subtemp[2][0] == "," and subtemp[2][1] == ",":
		dict3[subtemp[0]] = smalltemp[2]

#E. Penggunaan while loop agar input selalu berulang
while True:

	# Input dari user
	inp = input()

	#a. Command ADD dideteksi melalui keberadaan "ADD" dalam input dari user
	if "ADD" in inp:

		# Input displit untuk memisahkan command dengan input dari user
		temp = inp.split()		
		subtemp = (temp[1].split(";"))
		subtemp[1] = subtemp[1].upper()

		# Pembuatan database nama di seluruh kelas
		for i in classes.values():
			for j in i:
				names.append(j)

		# If statement mengenai keberadaan nama dalam database nama (list NAMES)
		if subtemp[0] not in names:
			classes[subtemp[1]].append(subtemp[0])
			print ("{} berhasil dimasukkan ke dalam buku.".format(subtemp[0]))
		elif subtemp[0] in names:
			print ("Mahasiswa {} sudah ada di dalam buku.".format(subtemp[0]))

	#b. Command UPDATE dideteksi melalui keberadaan "UPDATE" dalam input dari user
	elif "UPDATE" in inp:
		# Input displit untuk memisahkan command dengan input dari user
		temp = inp.split()
		subtemp = (temp[1].split(";"))
		smalltemp = subtemp[2].split(",")

		# Looping untuk mengubah angka bertipe string menjadi angka bertipe integer
		for i in range(0, len(smalltemp)):
			if smalltemp[i].isdigit() == True:
				smalltemp[i] = int(smalltemp[i])

		# Looping untuk mengubah '' menjadi 0, sehingga semua yang ada dalam SMALLTEMP adalah integer
		for i in range(len(smalltemp)):
			if smalltemp[i] == '':
				smalltemp[i] = 0

		# UPDATE untuk quiz
		if subtemp[1].lower() == "quiz":
			process2(subtemp,smalltemp,quiz1,quiz2)

		# UPDATE untuk tugas
		elif subtemp[1].lower() == "tugas":	
			process3(subtemp,smalltemp,task1,task2,task3)

		# UPDATE untuk ujian
		elif subtemp[1].lower() == "ujian":
			process2(subtemp,smalltemp,test1,test2)

		print("Berhasil menambah nilai {} pada mahasiswa {}.".format(subtemp[1],subtemp[0]))

	#c. Command AVERAGE dideteksi melalui keberadaan "AVERAGE" dalam input dari user
	elif "AVERAGE" in inp:

		# Input displit untuk memisahkan command dengan input dari user
		temp = inp.split()
		subtemp = temp[1].split(";")
		subtemp[0] = subtemp[0].upper()

		# If statement tentang keberadaan kelas dalam database kelas (tuple CLASSES.KEYS)
		if subtemp[0] in classes.keys():

			# Pengkategorian berkas sesuai input dari user
			if subtemp[1].lower() == "quiz":
				if subtemp[1].lower() + subtemp[2] == "quiz1":
					for i in classes[subtemp[0]]:
						avg_quiz += quiz1[i]
					avg_quiz = avg_quiz / len(classes[subtemp[0]])
					print("Rata-rata nilai {0} {1} pada kelas {2} adalah {3:.2f}.".format(subtemp[1],subtemp[2],subtemp[0],avg_quiz))

				elif subtemp[1].lower() + subtemp[2] == "quiz2":
					for i in classes[subtemp[0]]:
						avg_quiz += quiz2[i]
					avg_quiz = avg_quiz / len(classes[subtemp[0]])
					print("Rata-rata nilai {0} {1} pada kelas {2} adalah {3:.2f}.".format(subtemp[1],subtemp[2],subtemp[0],avg_quiz))

			elif subtemp[1].lower() == "tugas":
				if subtemp[1].lower() + subtemp[2] == "tugas1":
					for i in classes[subtemp[0]]:
						avg_task += task1[i]
					avg_task = avg_task / len(classes[subtemp[0]])
					print("Rata-rata nilai {0} {1} pada kelas {2} adalah {3:.2f}.".format(subtemp[1],subtemp[2],subtemp[0],avg_task))

				elif subtemp[1].lower() + subtemp[2] == "tugas2":
					for i in classes[subtemp[0]]:
						avg_task += task2[i]
					avg_task = avg_task / len(classes[subtemp[0]])
					print("Rata-rata nilai {0} {1} pada kelas {2} adalah {3:.2f}.".format(subtemp[1],subtemp[2],subtemp[0],avg_task))

				elif subtemp[1].lower() + subtemp[2] == "tugas3":
					for i in classes[subtemp[0]]:
						avg_task += task2[i]
					avg_task = avg_task / len(classes[subtemp[0]])
					print("Rata-rata nilai {0} {1} pada kelas {2} adalah {3:.2f}.".format(subtemp[1],subtemp[2],subtemp[0],avg_task))

			elif subtemp[1].lower() == "ujian":
				if subtemp[1].lower() + subtemp[2] == "ujian1":
					for i in classes[subtemp[0]]:
						avg_test += test1[i]
					avg_test = avg_test / len(classes[subtemp[0]])
					print("Rata-rata nilai {0} {1} pada kelas {2} adalah {3:.2f}.".format(subtemp[1],subtemp[2],subtemp[0],avg_test))

				elif subtemp[1].lower() + subtemp[2] == "tugas2":
					for i in classes[subtemp[0]]:
						avg_test += test2[i]
					avg_test = avg_test / len(classes[subtemp[0]])
					print("Rata-rata nilai {0} {1} pada kelas {2} adalah {3:.2f}.".format(subtemp[1],subtemp[2],subtemp[0],avg_test))	

		elif subtemp[0] not in classes.keys():
			print ("Kelas {} belum terdata. Cek kembali data {} {} yang anda inginkan.".format(subtemp[0],subtemp[1],subtemp[2]))

	elif "SUMMARY" in inp:
		temp = inp.split()
		temp[1] = temp[1].capitalize()

		for i in classes.keys():
			for j in classes[i]:
				if temp[1] == j:
					current = i

		avg_quiz = float("{0:.2f}".format((quiz1[temp[1]] + quiz2[temp[1]]) / 2))
		avg_task = float("{0:.2f}".format((task1[temp[1]] + task2[temp[1]] + task3[temp[1]]) / 3))
		avg_test = float("{0:.2f}".format((test1[temp[1]] + test2[temp[1]]) / 2))

		final = float("{0:.2f}".format(((avg_task) * 2)/10 + (3 * (avg_quiz))/10 + ((avg_test))/2))
		
		subtemp = ["Nama", "Kelas","Quiz","Tugas","Ujian","Nilai Akhir"]
		smalltemp = [temp[1],current,avg_quiz,avg_task,avg_test,final]

		for i in range(len(subtemp)):
				print("{:15}: {}".format(subtemp[i],smalltemp[i]))

	elif "SEARCH" in inp:
		temp = inp.split()
		subtemp = temp[1].split(";")
		smalltemp = subtemp[2].split("-")

		for i in range(len(smalltemp)):
			if smalltemp[i].isdigit() == True:
				smalltemp[i] = int(smalltemp[i])

		print ("Mahasiswa yang ada dalam jangkauan {}-{} adalah:".format(smalltemp[0],smalltemp[1]))

		if subtemp[0].lower() + subtemp[1] == "quiz1":
			for key, val in quiz1.items():
				if smalltemp[0] <= val <= smalltemp[1]:
					print ("Mahasiswa {} dengan nilai {}.".format(key,val))

		elif subtemp[0].lower() + subtemp[1] == "quiz2":
			for key,val in quiz2.items():
				if smalltemp[0] <= val <= smalltemp[1]:
					print ("Mahasiswa {} dengan nilai {}.".format(key,val))

		elif subtemp[0].lower() + subtemp[1] == "tugas1":
			for key,val in task1.items():
				if smalltemp[0] <= val <= smalltemp[1]:
					print ("Mahasiswa {} dengan nilai {}.".format(key,val))

		elif subtemp[0].lower() + subtemp[1] == "tugas2":
			for key,val in task2.items():
				if smalltemp[0] <= val <= smalltemp[1]:
					print ("Mahasiswa {} dengan nilai {}.".format(key,val))

		elif subtemp[0].lower() + subtemp[1] == "tugas3":
			for key,val in task3.items():
				if smalltemp[0] <= val <= smalltemp[1]:
					print ("Mahasiswa {} dengan nilai {}.".format(key,val))

		elif subtemp[0].lower() + subtemp[1] == "ujian1":
			for key,val in test1.items():
				if smalltemp[0] <= val <= smalltemp[1]:
					print ("Mahasiswa {} dengan nilai {}.".format(key,val))

		elif subtemp[0].lower() + subtemp[1] == "ujian2":
			for key,val in test2.items():
				if smalltemp[0] <= val <= smalltemp[1]:
					print ("Mahasiswa {} dengan nilai {}.".format(key,val))

	elif "Selesai" in inp or "selesai" in inp:
		break
