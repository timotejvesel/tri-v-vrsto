import tkinter as tk
import model

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
        
		self.klik()
		self.osvezi_prikaz()
		

	def klik(self):
		self.igralna_plosca.tag_bind("kvadrat0",'<Button-1>', self.test)
		self.igralna_plosca.tag_bind("kvadrat1",'<Button-1>', self.test)



	def test(self, event):
		self.igralna_plosca.create_rectangle(50, 25, 150, 75, fill="blue")
		self.igra.clovek(0)
		print(self.igra)



	
	def osvezi_prikaz(self):
		self.igralna_plosca.delete('all')

		# Tablica, prva vrsta
		self.igralna_plosca.create_rectangle(
			ODMIK,
			ODMIK, 
			VELIKOST_TABLICE,
			VELIKOST_TABLICE, 
			fill="FloralWhite", tags="kvadrat0"
		)
		self.igralna_plosca.create_rectangle(
			VELIKOST_TABLICE + ODMIK,
			ODMIK, 
			2 * VELIKOST_TABLICE,
			VELIKOST_TABLICE,
			fill="FloralWhite", tags="kvadrat1"
		)
		self.igralna_plosca.create_rectangle(
			2 * VELIKOST_TABLICE + ODMIK,
			ODMIK,
			3 * VELIKOST_TABLICE,
			VELIKOST_TABLICE,
		 	fill="FloralWhite", tags="kvadrat2"
		)

		# Tablica, druga vrsta
		self.igralna_plosca.create_rectangle(
			ODMIK,
			2 * VELIKOST_TABLICE,
			VELIKOST_TABLICE,
			VELIKOST_TABLICE + ODMIK,
		 	fill="FloralWhite", tags="kvadrat3"
		)
		self.igralna_plosca.create_rectangle(
			VELIKOST_TABLICE + ODMIK,
			2 * VELIKOST_TABLICE,
			2 * VELIKOST_TABLICE,
			VELIKOST_TABLICE + ODMIK,
			fill="FloralWhite", tags="kvadrat4"
		)
		self.igralna_plosca.create_rectangle(
			2 * VELIKOST_TABLICE + ODMIK,
			2 * VELIKOST_TABLICE,
			3* VELIKOST_TABLICE,
			VELIKOST_TABLICE + ODMIK,
			fill="FloralWhite", tags="kvadrat5"
		)

		# Tablica, tretja vrsta
		self.igralna_plosca.create_rectangle(
			ODMIK,
			3 * VELIKOST_TABLICE,
			VELIKOST_TABLICE,
			2 * VELIKOST_TABLICE + ODMIK,
			fill="FloralWhite", tags="kvadrat6"
		)
		self.igralna_plosca.create_rectangle(
			VELIKOST_TABLICE + ODMIK,
			3 * VELIKOST_TABLICE,
			2 * VELIKOST_TABLICE,
			2 * VELIKOST_TABLICE + ODMIK,
			fill="FloralWhite", tags="kvadrat7"
		)
		self.igralna_plosca.create_rectangle(
			2 * VELIKOST_TABLICE + ODMIK,
			3 * VELIKOST_TABLICE,
			3 * VELIKOST_TABLICE,
			2 * VELIKOST_TABLICE + ODMIK,
			fill="FloralWhite", tags="kvadrat8"
		)

		
		
		

		
		
		






okno = tk.Tk()
moj_program = Gui(okno)
okno.mainloop()