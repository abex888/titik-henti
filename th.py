#!/usr/bin/env python3
from tkinter import *
from math import sqrt

class tentang():
	def __init__(self, event=None):
				
		self.jendela_tentang = Toplevel()
		self.jendela_tentang.title('About')
		self.jendela_tentang.resizable(0,0)
		
		self.frame_deskripsi=Frame(self.jendela_tentang, bd=3, bg='white', relief=SUNKEN)
		self.frame_deskripsi.pack()
		
		self.label_deskripsi = Label(self.frame_deskripsi, text='', bg='white', fg='black', justify=LEFT)
		self.label_deskripsi.config(text=deskripsi)
		self.label_deskripsi.pack()			
				
		self.q = Button(self.jendela_tentang, text='Tutup')
		self.q.pack()
		self.q.bind('<Button-1>', lambda kaluar: self.jendela_tentang.destroy())
		self.jendela_tentang.bind('<Button-3>',lambda kaluar: self.jendela_tentang.destroy())
		self.jendela_tentang.bind('<Escape>',lambda kaluar: self.jendela_tentang.destroy())


def kaluar(event):
	print('Program keluar dengan normal')
	root.destroy()

def balikan(event):
	hasil.set('Tombol Ulang Ditekan')
	nama_kota_a.set('')
	nama_kota_b.set('')
	jumlah_a.set(0)
	jumlah_b.set(0)
	jarak_ab.set(0)
	hasil.set('Silahkan Masukan Data')
	
	
def th(event):
	kotab = nama_kota_b.get()
	dab = float(jarak_ab.get())
	pa = float(jumlah_a.get())
	pb = float(jumlah_b.get())	
	TH = dab/(1+sqrt(pa/pb))
	TH = 'Titik Henti ada pada\n{:.2f} km dari {}'.format(TH, kotab)
	hasil.set(TH)

root = Tk()
root.title('Titik Henti')
root.resizable(0,0)

#Deskripsi
deskripsi='''PENGHITUNGAN TITIK HENTI
Pembuat		: Aries Aprilian (abex888@gmail.com)
Versi		: 1.0.2
Lisensi		: GNU GPL versi 2
Program ini dibuat dengan python3 menggunakan beberapa
modul diantaranya adalah:
1. modul Tkinter untuk gui
2. modul math untuk menghitung akar kuadrat'''

#Frame
jendela = Frame(root, bd=3, relief=SUNKEN)
tombol = Frame()


#DEKLARASI VARIABLE
nama_kota_a = StringVar()
nama_kota_b = StringVar()
jumlah_a = IntVar()
jumlah_b = IntVar()
jarak_ab = IntVar()
hasil = StringVar()

#WIDGET MILIK ROOT
judul1 = Label(root, text = 'PENGHITUNGAN BATAS WILAYAH')
judul1.configure(font='serif 16 bold')
judul2 = Label(root, text = 'BERDASARKAN TEORI TITIK HENTI')
judul2.configure(font='serif 12 bold')

catatan1 = Label(root, text='F1 untuk deskripsi')
catatan2 = Label(root, text='F4 untuk keluar')
copyright = Label(root, text='(c)Aries Aprilian')

judul1.grid(row=0, column=0, columnspan=3)
judul2.grid(row=1, column=0, columnspan=3)
jendela.grid(row=2, column=0, columnspan=3)
tombol.grid(row=3, column=0, columnspan=3)
catatan1.grid(row=4, column=0)
catatan2.grid(row=4, column=1)
copyright.grid(row=4, column=2)


#ISI
#Label Isi
labelkotaa = Label(jendela, text = 'Wilayah Penduduk Banyak')
labelkotaa.grid(row=4, column=0, padx=2, pady=2, sticky='w')
jumlahkotaa = Label(jendela, text = 'Jumlah Penduduknya')
jumlahkotaa.grid(row=5, column=0, padx=2, pady=2, sticky='w')
labelkotab = Label(jendela, text = 'Wilayah Penduduk Sedikit')
labelkotab.grid(row=6, column=0, padx=2, pady=2, sticky='w')
jumlahkotab = Label(jendela, text = 'Jumlah Penduduknya')
jumlahkotab.grid(row=7, column=0, padx=2, pady=2, sticky='w')
labeljarak = Label(jendela, text = 'Jarak Keduanya')
labeljarak.grid(row=8, column=0, padx=2, pady=2, sticky='w')
labelhasil = Label(jendela, text = 'Hasil Perhitungan')
labelhasil.grid(row=9, column=0, padx=2, pady=2, sticky='w')
labelhasil2 = Label(jendela, textvariable=hasil, justify=LEFT)
hasil.set('Silahkan Masukkan Data')
labelhasil2.grid(row=9, column=1, padx=2, pady=2)

#Entry Isi
entrykotaa = Entry(jendela, width=20, textvariable=nama_kota_a, justify=LEFT)
entrykotaa.grid(row=4, column=1, padx=2, pady=2, sticky='e')
entrykotaa.focus()

jumlaha = Entry(jendela, width=5, textvariable=jumlah_a, justify=RIGHT)
jumlaha.grid(row=5, column=1, padx=2, pady=2, sticky='e')

entrykotab = Entry(jendela, width=20, textvariable=nama_kota_b, justify=LEFT)
entrykotab.grid(row=6, column=1, padx=2, pady=2, sticky='e')

jumlahb = Entry(jendela, width=5, textvariable=jumlah_b, justify=RIGHT)
jumlahb.grid(row=7, column=1, padx=2, pady=2, sticky='e')

jarak = Entry(jendela, width=5, textvariable=jarak_ab, justify=RIGHT)
jarak.grid(row=8, column=1, padx=2, pady=2, sticky='e')

#TOMBOL - TOMBOL
hitung = Button(tombol, text = 'Hitung')
hitung.grid(row=0, column=0, padx=2, pady=2, sticky='we')
ulang = Button(tombol, text = 'Ulang')
ulang.grid(row=0, column=1, padx=2, pady=2, sticky='we')
keluar = Button(tombol, text = 'Keluar')
keluar.grid(row=0, column=2, padx=2, pady=2, sticky='we')
tombol_tentang = Button(tombol, text = 'Tentang')
tombol_tentang.grid(row=0, column=3, padx=2, pady=2, sticky='we')

#BINDING#
jendela.bind('<Control-q>', kaluar)
jendela.bind('<Control-Q>', kaluar)
root.bind('<F1>', tentang)
root.bind('<F4>', kaluar)

hitung.bind('<Button-1>', th)
ulang.bind('<Button-1>', balikan)

keluar.bind('<Button-1>', kaluar)
#keluar.bind('<Button-3>', kaluar)
tombol_tentang.bind('<Button-1>', tentang)




#MULAI LOOP
jendela.mainloop()

