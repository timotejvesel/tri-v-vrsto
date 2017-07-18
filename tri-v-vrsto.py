import tkinter as tk
import model
import tkinter.messagebox
import pickle

PRAZNO = " "
IGRALEC_CLOVEK = "X"
IGRALEC_RACUNALNIK = "O"

VELIKOST_TABLICE = 100
ODMIK = 10

class Gui:
	def __init__(self, okno):
		# Nastavimo model
		self.igra = model.Igra()

		# Pripravimo grafični vmesnik
		self.okno = okno
		self.igralna_plosca = tk.Canvas(
			width=3 * VELIKOST_TABLICE + ODMIK,
			height=3 * VELIKOST_TABLICE + ODMIK
		)

		self.igralna_plosca.pack()
		self.osvezi_prikaz()
		self.klik()

		# Meni z gumbi
		menu = tk.Menu(okno)
		filemenu = tk.Menu(menu)
		okno.config(menu=menu)
		menu.add_cascade(label="Možnosti", menu=filemenu)
		filemenu.add_command(label="Nova igra", command=self.konec)
		filemenu.add_command(label="Shrani", command=self.shrani)
		filemenu.add_command(label="Nadaljuj igro", command=self.nadaljuj)
		filemenu.add_separator()
		filemenu.add_command(label="Izhod", command=self.okno.destroy)


	def narisi_krizec(self, z):
		# Matrične koordinate
		x = z % 3
		y = z // 3

		self.igralna_plosca.create_line(
				2 * ODMIK + x * VELIKOST_TABLICE,
				2 * ODMIK + y * VELIKOST_TABLICE,
				(x + 1) * VELIKOST_TABLICE - ODMIK, 
				(y + 1) * VELIKOST_TABLICE - ODMIK,
				width=3
			)

		self.igralna_plosca.create_line(
			2* ODMIK + x * VELIKOST_TABLICE,
			(y + 1) * VELIKOST_TABLICE - ODMIK,
			(x + 1) * VELIKOST_TABLICE - ODMIK,
			2 * ODMIK + y * VELIKOST_TABLICE,
			width=3
		)

	def narisi_krozec(self, z):	
		# Matrične koordinate
		x = z % 3
		y = z // 3

		self.igralna_plosca.create_oval(
			2 * ODMIK + x * VELIKOST_TABLICE,
			2 * ODMIK + y * VELIKOST_TABLICE,
			VELIKOST_TABLICE - ODMIK + x * VELIKOST_TABLICE, 
			VELIKOST_TABLICE - ODMIK + y * VELIKOST_TABLICE,
			width=3
		)

		
	# Shrani trenutno stanje na igralni tablici
	def shrani(self):
		with open ("tri-v-vrsto.txt", "wb") as f:
			pickle.dump(self.igra.tablica, f)

	# Nadaljuje shranjeno igro
	def nadaljuj(self):
		try:
			with open("tri-v-vrsto.txt", "rb") as f:
				sez = pickle.load(f)

			self.igra.nova_igra()
			self.osvezi_prikaz()

			for i, j in enumerate(sez):
				if j == IGRALEC_CLOVEK:
					self.narisi_krizec(i)
					self.igra.tablica[i] = IGRALEC_CLOVEK

				elif j == IGRALEC_RACUNALNIK:
					self.narisi_krozec(i)
					self.igra.tablica[i] = IGRALEC_RACUNALNIK

			if self.igra.zmagovalne_kombinacije(IGRALEC_CLOVEK):
				tk.messagebox.showinfo(" ", "Zmagal si!")
				self.odstrani_klik()

			elif self.igra.polna_tablica():
				tk.messagebox.showinfo(" ", "Neodločeno!")
				self.odstrani_klik()
			
			elif self.igra.zmagovalne_kombinacije(IGRALEC_RACUNALNIK):
				tk.messagebox.showinfo(" ", "Izgubil si!")
				self.odstrani_klik()

		except IOError:
			tk.messagebox.showinfo(" ", "Igra ni shranjena!")


	def konec(self):
		if self.igra.zmagovalne_kombinacije(IGRALEC_RACUNALNIK) or \
		self.igra.zmagovalne_kombinacije(IGRALEC_RACUNALNIK) or \
		self.igra.polna_tablica():
			self.igra.nova_igra()
			self.osvezi_prikaz()
			self.klik()

		else:
			izbira = tk.messagebox.askokcancel("Potrdi", "Konec igre?")
			if izbira == True:
				self.igra.nova_igra()
				self.osvezi_prikaz()
				self.klik()

	def kvadrat(self, event, n):
		if self.igra.clovek(n) == False:
			tk.messagebox.showinfo(" ", "To polje je že zasedeno!")
		else:
			self.igra.clovek(n)
			self.narisi_krizec(n)
		
			if self.igra.zmagovalne_kombinacije(IGRALEC_CLOVEK):
				tk.messagebox.showinfo(" ", "Zmagal si!")
				self.odstrani_klik()

			elif self.igra.polna_tablica():
				tk.messagebox.showinfo(" ", "Neodločeno!")
				self.odstrani_klik()
			else:
				self.krog()
				if self.igra.zmagovalne_kombinacije(IGRALEC_RACUNALNIK):
					tk.messagebox.showinfo(" ", "Izgubil si!")
					self.odstrani_klik()

	def krog(self):
		m = self.igra.racunalnik()
		self.narisi_krozec(m)

		
	def osvezi_prikaz(self):
		self.igralna_plosca.delete('all')

		kvadratki = {
			(0, 1, 0, 1, 1, 0, 1, 0, 0),
		 	(1, 1, 0, 1, 2, 0, 1, 0, 1),
		 	(2, 1, 0, 1, 3, 0, 1, 0, 2),
		 	(0, 1, 2, 0, 1, 0, 1, 1, 3),
		 	(1, 1, 2, 0, 2, 0, 1, 1, 4),
		 	(2, 1, 2, 0, 3, 0, 1, 1, 5),
		 	(0, 1, 3, 0, 1, 0, 2, 1, 6),
		 	(1, 1, 3, 0, 2, 0, 2, 1, 7),
		 	(2, 1, 3, 0, 3, 0, 2, 1, 8),
		 }

		for x in kvadratki:
			self.igralna_plosca.create_rectangle(
				x[0] * VELIKOST_TABLICE + x[1] * ODMIK,
		 		x[2] * VELIKOST_TABLICE + x[3] * ODMIK,
		 		x[4] * VELIKOST_TABLICE + x[5] * ODMIK,
		 		x[6] * VELIKOST_TABLICE + x[7] * ODMIK,
		 		fill="FloralWhite", 
		 		tags="kvadrat" + str(x[8]) + "_tag"
		 	)


	def klik(self):
		for t in range(9):
			self.igralna_plosca.tag_bind(
			"kvadrat" + str(t) + "_tag",
			"<Button-1>",
			 lambda event, t=t: self.kvadrat(event, t)
			)

		
	def odstrani_klik(self):
		for x in range(9):
			self.igralna_plosca.tag_unbind(
				"kvadrat" + str(x) + "_tag",
				'<Button-1>'
			)
		
		
okno = tk.Tk()
okno.resizable(0,0)
moj_program = Gui(okno)
okno.mainloop()