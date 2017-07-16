import tkinter as tk
import model
import tkinter.messagebox
import pickle

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
				if j == "X":
					x = i % 3
					y = i // 3

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

					self.igra.clovek(i)

				elif j == "O":
					x = i % 3
					y = i // 3

					self.igralna_plosca.create_oval(
						2 * ODMIK + x * VELIKOST_TABLICE,
						2 * ODMIK + y * VELIKOST_TABLICE,
						VELIKOST_TABLICE - ODMIK + x * VELIKOST_TABLICE, 
						VELIKOST_TABLICE - ODMIK + y * VELIKOST_TABLICE,
						width=3
					)

					self.igra.tablica[i] = "O"

			if self.igra.zmagovalne_kombinacije_clovek() == True:
				tk.messagebox.showinfo(" ", "Zmagal si!")
				self.odstrani_klik()

			elif self.igra.polna_tablica() == True:
				tk.messagebox.showinfo(" ", "Neodločeno!")
				self.odstrani_klik()
			
			elif self.igra.zmagovalne_kombinacije_racunalnik() == True:
				tk.messagebox.showinfo(" ", "Izgubil si!")
				self.odstrani_klik()

		except IOError:
			tk.messagebox.showinfo(" ", "Igra ni shranjena!")


	
	
	def konec(self):
		if self.igra.zmagovalne_kombinacije_racunalnik() or \
		self.igra.zmagovalne_kombinacije_clovek() or \
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
		# Matrične koordinate
		x = n % 3
		y = n // 3

		if self.igra.clovek(n) == False:
			tk.messagebox.showinfo(" ", "To polje je že zasedeno!")
		else:
			self.igra.clovek(n)

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
		

			if self.igra.zmagovalne_kombinacije_clovek() == True:
				tk.messagebox.showinfo(" ", "Zmagal si!")
				self.odstrani_klik()

			elif self.igra.polna_tablica() == True:
				tk.messagebox.showinfo(" ", "Neodločeno!")
				self.odstrani_klik()
			else:
				self.krog()
				if self.igra.zmagovalne_kombinacije_racunalnik() == True:
					tk.messagebox.showinfo(" ", "Izgubil si!")
					self.odstrani_klik()

	def krog(self):
		m = self.igra.racunalnik()

		# Matrične koordinate
		x = m % 3
		y = m // 3

		self.igralna_plosca.create_oval(
			2 * ODMIK + x * VELIKOST_TABLICE,
			2 * ODMIK + y * VELIKOST_TABLICE,
			VELIKOST_TABLICE - ODMIK + x * VELIKOST_TABLICE, 
			VELIKOST_TABLICE - ODMIK + y * VELIKOST_TABLICE,
			width=3
		)

		
	def osvezi_prikaz(self):
		self.igralna_plosca.delete('all')

		# Tablica, prva vrsta
		self.igralna_plosca.create_rectangle(
			ODMIK,
			ODMIK, 
			VELIKOST_TABLICE,
			VELIKOST_TABLICE, 
			fill="FloralWhite", tags="kvadrat0_tag"
		)
		self.igralna_plosca.create_rectangle(
			VELIKOST_TABLICE + ODMIK,
			ODMIK, 
			2 * VELIKOST_TABLICE,
			VELIKOST_TABLICE,
			fill="FloralWhite", tags="kvadrat1_tag"
		)
		self.igralna_plosca.create_rectangle(
			2 * VELIKOST_TABLICE + ODMIK,
			ODMIK,
			3 * VELIKOST_TABLICE,
			VELIKOST_TABLICE,
		 	fill="FloralWhite", tags="kvadrat2_tag"
		)

		# Tablica, druga vrsta
		self.igralna_plosca.create_rectangle(
			ODMIK,
			2 * VELIKOST_TABLICE,
			VELIKOST_TABLICE,
			VELIKOST_TABLICE + ODMIK,
		 	fill="FloralWhite", tags="kvadrat3_tag"
		)
		self.igralna_plosca.create_rectangle(
			VELIKOST_TABLICE + ODMIK,
			2 * VELIKOST_TABLICE,
			2 * VELIKOST_TABLICE,
			VELIKOST_TABLICE + ODMIK,
			fill="FloralWhite", tags="kvadrat4_tag"
		)
		self.igralna_plosca.create_rectangle(
			2 * VELIKOST_TABLICE + ODMIK,
			2 * VELIKOST_TABLICE,
			3* VELIKOST_TABLICE,
			VELIKOST_TABLICE + ODMIK,
			fill="FloralWhite", tags="kvadrat5_tag"
		)

		# Tablica, tretja vrsta
		self.igralna_plosca.create_rectangle(
			ODMIK,
			3 * VELIKOST_TABLICE,
			VELIKOST_TABLICE,
			2 * VELIKOST_TABLICE + ODMIK,
			fill="FloralWhite", tags="kvadrat6_tag"
		)
		self.igralna_plosca.create_rectangle(
			VELIKOST_TABLICE + ODMIK,
			3 * VELIKOST_TABLICE,
			2 * VELIKOST_TABLICE,
			2 * VELIKOST_TABLICE + ODMIK,
			fill="FloralWhite", tags="kvadrat7_tag"
		)
		self.igralna_plosca.create_rectangle(
			2 * VELIKOST_TABLICE + ODMIK,
			3 * VELIKOST_TABLICE,
			3 * VELIKOST_TABLICE,
			2 * VELIKOST_TABLICE + ODMIK,
			fill="FloralWhite", tags="kvadrat8_tag"
		)

	def klik(self):
		self.igralna_plosca.tag_bind(
			"kvadrat0_tag","<Button-1>",
			 lambda event: self.kvadrat(event, 0)
		)
		self.igralna_plosca.tag_bind(
			"kvadrat1_tag","<Button-1>", 
			lambda event: self.kvadrat(event, 1)
		)
		self.igralna_plosca.tag_bind(
			"kvadrat2_tag","<Button-1>",
			lambda event: self.kvadrat(event, 2)
		)
		self.igralna_plosca.tag_bind(
			"kvadrat3_tag","<Button-1>",
			lambda event: self.kvadrat(event, 3)
		)
		self.igralna_plosca.tag_bind(
			"kvadrat4_tag","<Button-1>",
			lambda event: self.kvadrat(event, 4)
		)
		self.igralna_plosca.tag_bind(
			"kvadrat5_tag","<Button-1>",
			lambda event: self.kvadrat(event, 5)
		)
		self.igralna_plosca.tag_bind(
			"kvadrat6_tag","<Button-1>",
			lambda event: self.kvadrat(event, 6)
		)
		self.igralna_plosca.tag_bind(
			"kvadrat7_tag","<Button-1>",
			lambda event: self.kvadrat(event, 7)
		)
		self.igralna_plosca.tag_bind(
			"kvadrat8_tag","<Button-1>",
			lambda event: self.kvadrat(event, 8)
		)


	def odstrani_klik(self):
		self.igralna_plosca.tag_unbind("kvadrat0_tag",'<Button-1>')
		self.igralna_plosca.tag_unbind("kvadrat1_tag",'<Button-1>')
		self.igralna_plosca.tag_unbind("kvadrat2_tag",'<Button-1>')
		self.igralna_plosca.tag_unbind("kvadrat3_tag",'<Button-1>')
		self.igralna_plosca.tag_unbind("kvadrat4_tag",'<Button-1>')
		self.igralna_plosca.tag_unbind("kvadrat5_tag",'<Button-1>')
		self.igralna_plosca.tag_unbind("kvadrat6_tag",'<Button-1>')
		self.igralna_plosca.tag_unbind("kvadrat7_tag",'<Button-1>')
		self.igralna_plosca.tag_unbind("kvadrat8_tag",'<Button-1>')
		
		
		


okno = tk.Tk()
okno.resizable(0,0)
moj_program = Gui(okno)
okno.mainloop()