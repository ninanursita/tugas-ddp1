from tkinter import *
from tkinter import messagebox
import datetime

# Variabel untuk menyimpan jumlah klik
counter = 0

# Pembuatan list kosong untuk menyimpan two-dimensional list dan variabel-variabel yang dibutuhkan
small = []
maps = []
turns = []
history = []
rule = 0
row = 0
column = 0
win1 = ""
win2 = ""
i = datetime.datetime.now()
history = open("gamehistory.txt","a+")

# Fungsi untuk membagi list menjadi list yang lebih kecil sesuai keinginan
def chunks(l, n):
    for i in range(0,len(l),n):
        yield l[i:i + n]

class Tile:

    # Fungsi untuk membuat clickable rectangle    
    def __init__(self, canvas, column, row, color, index):
        
        self.rect = canvas.create_rectangle(column * 50, row * 50, (column * 50) + 50, (row * 50) + 50, fill = color, activefill = "royal blue", tags = index-1)
        self.canvas = canvas
        self.canvas.tag_bind(self.rect,"<Button-1>",self.onClick)

    # Fungsi untuk mengganti warna setiap diklik dengan mengecek jumlah klik
    def onClick(self, event):
        
        # Pembuatan variabel yang berfungsi sebagai nilai index pada list TURNS
        tempIndex = int(self.canvas.gettags(self.rect)[0])

        # Pengambilan variabel menjadi global untuk mempermudah pengubahan dan penggunaan variabel
        global counter
        global maps
        global turns
        global rule
        global row
        global column
        global win1
        global win2
        global history
        
        # Warna diganti dengan mendeteksi apakah jumlah klik genap atau ganjil
        counter += 1
        if counter % 2 == 0:
            self.canvas.itemconfig(self.rect, fill= "#F0B775", state = "disabled")
            turns[tempIndex] = "x"
        elif counter % 2 != 0:
            self.canvas.itemconfig(self.rect, fill = "#FF895D", state = "disabled")
            turns[tempIndex] = "o"
        
        # Pembuatan two-dimensional list dari TURNS untuk mempermudah pengecekan dan list yang merupakan syarat kemenangan
        win1 = str('o') * rule
        win2 = str('x') * rule
        
        # Pengecekan kemenangan berjalan setiap ada klik, variabel boolean ditujukan untuk status kemenangan player1 dan player2

        # Cek horizontal
        tempHor = list(chunks(turns,column))
        
        for i in range(len(tempHor)):
            tempHor[i] = ((str(tempHor[i]).strip("[]")).replace(", ","")).replace("'", "")
            
        try:
            for i in range(len(tempHor)):
                if win1 in tempHor[i]:
                    messagebox.showinfo("Selamat!","Player 1 menang setelah {} giliran!".format(counter))
                    self.canvas.itemconfig("all",state="disabled")
                    history.write("{} Player 1 menang setelah {} giliran\n".format(str(datetime.datetime.now()).split(".")[0],counter))
                elif win2 in tempHor[i]:
                    messagebox.showinfo("Selamat!","Player 2 menang setelah {} giliran!".format(counter))
                    self.canvas.itemconfig("all",state="disabled")
                    history.write("{} Player 2 menang setelah {} giliran\n".format(str(datetime.datetime.now()).split(".")[0],counter))
        except IndexError:
            pass

        # Cek vertikal
        tempVer = []        

        for i in range(column):
            tempVer.append(turns[i::column])

        for i in range(len(tempVer)):
            tempVer[i] = ((str(tempVer[i]).strip("[]")).replace(", ","")).replace("'", "")

        try:
            for i in range(len(tempVer)):
                if win1 in tempVer[i]:
                    messagebox.showinfo("Selamat!","Player 1 menang setelah {} giliran!".format(counter))
                    self.canvas.itemconfig("all",state="disabled")
                elif win2 in tempVer[i]:
                    messagebox.showinfo("Selamat!","Player 2 menang setelah {} giliran!".format(counter))
                    self.canvas.itemconfig("all",state="disabled")
        except IndexError:
            pass

        # Cek diagonal
        tempDiag = []

        if row == column:
            for i in range(column):
                tempDiag.append(turns[i::column-1][:i+1])
            for i in range((2*column)-1,column*row,column):
                tempDiag.append(turns[i::column-1][:i+1])
            for i in range(column):
               tempDiag.append((turns[i::(column+1)][:(column)-i]))
            for i in range(column,column*row,column):
                tempDiag.append(turns[i::(column+1)][:5-(i//column)])

            for i in range(len(tempDiag)):
                tempDiag[i] = ((str(tempDiag[i]).strip("[]")).replace(", ","")).replace("'", "")

            try:
                for i in range(len(tempDiag)):
                    if win1 in tempDiag[i]:
                        messagebox.showinfo("Selamat!","Player 1 menang setelah {} giliran!".format(counter))
                        self.canvas.itemconfig("all",state="disabled")
                    elif win2 in tempDiag[i]:
                        messagebox.showinfo("Selamat!","Player 2 menang setelah {} giliran!".format(counter))
                        self.canvas.itemconfig("all",state="disabled")
            except IndexError:
                pass
            
class GameBoard:
    def __init__(self):
        # Pembuatan window, judul aplikasi, greeting message, dan canvas
        self.window = Tk()
        self.window.title("Simplified M,N,K Game")
        message = Label(self.window, text = "Selamat datang di Simplified M,N,K Game!\n")

        # Pembuatan label untuk menampilkan peraturan permainan
        guideline = Label(self.window, text = "Peraturan: \n 1) Klik pertama = Player 1\n2) Klik kedua = Player 2 \n3) Jika baris = kolom, maka kemenangan juga bisa\ndiperoleh dari diagonal!\n")

        # Pembuatan entry untuk user menginput ukuran board permainan
        self.rowLabel = Label(self.window, text = "Berapa besar baris permainan yang Anda inginkan?")
        self.rowSize = IntVar()
        entryRow = Entry(self.window, textvariable = self.rowSize)
        self.columnLabel = Label(self.window, text = "Berapa besar kolom permainan yang Anda inginkan?")
        self.columnSize = IntVar()
        entryColumn = Entry(self.window, textvariable = self.columnSize)

        # Pembuatan entry untuk user menginput peraturan-peraturan pada game
        ruleLabel = Label(self.window, text = "Berapa jumlah kotak yang Anda butuhkan untuk menang?")
        self.winningRule = IntVar()
        entryRule = Entry(self.window, textvariable = self.winningRule)
        
        # Pembuatan button untuk memulai permainan dan mengubah papan permainan
        startButton = Button(self.window, text="Mulai permainan!", command = self.makeTiles)
        clearLabel = Label(self.window, text = "\nIngin mengganti ukuran papan permainan?")
        clearButton = Button(self.window, text = "Ubah papan permainan!", command = self.clearBoard)

        # Pembuatan Button untuk menampilkan history
        historyLabel = Label(self.window, text = "\nSiapa saja ya yang pernah menang?")
        historyButton = Button(self.window, text = "Tampilkan riwayat permainan!",command = self.viewHistory)

        # Menampilkan attributes pada window
        message.pack()
        guideline.pack()
        self.rowLabel.pack()
        entryRow.pack()
        self.columnLabel.pack()
        entryColumn.pack()
        ruleLabel.pack()
        entryRule.pack()
        startButton.pack()
        clearLabel.pack()
        clearButton.pack()
        historyLabel.pack()
        historyButton.pack()
        self.window.mainloop()

    def makeTiles(self):
        if max(self.rowSize.get(),self.columnSize.get()) < self.winningRule.get():
            messagebox.showerror("Error","      Kotak yang anda butuhkan harus\n                    sama atau kurang\n      dengan ukuran papan permainan!")
            
        elif max(self.rowSize.get(),self.columnSize.get()) >= self.winningRule.get():
             # Pembuatan canvas
            self.gameWindow = Tk()
            self.gameWindow.title("M,N,K Game Board")
            self.canvas = Canvas(self.gameWindow, width = self.columnSize.get() * 50, height = self.rowSize.get() * 50)
            self.canvas.pack()

            # Pembuatan variabel untuk menyimpan ukuran board yang diinginkan user
            temp = self.columnSize.get()
            temp2 = self.rowSize.get()
            temp3 = 0

            global small
            global maps
            global turns
            global counter
            
            turns = []
            small = []
            maps = []
            counter = 0

            # Looping untuk membuat pemetaan pada Tiles
            for i in range(self.columnSize.get()):
                small.append(0)

            while temp2 > 0:
                maps.append(small)
                temp2 -= 1
                  
            for i in range(len(maps)):
                for j in range(len(maps[i])):
                    temp3 += 1
                    Tile(self.canvas, j, i, "#F9F296", temp3)

            for i in range(self.columnSize.get() * self.rowSize.get()):
                turns.append(0)

            GameBoard.getRule(self)
            GameBoard.getRow(self)
            GameBoard.getColumn(self)

    def clearBoard(self):
        self.gameWindow.destroy()

    def getRule(self):
        global rule
        rule = self.winningRule.get()

    def getRow(self):
        global row
        row = self.rowSize.get()

    def getColumn(self):
        global column
        column = self.columnSize.get()

    def viewHistory(self):
        temp = open("gamehistory.txt","r")
        messagebox.showinfo("Riwayat Permainan",temp.read())
        temp.close()
        
GameBoard()
