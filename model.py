import random

PRAZNO = " "
IGRALEC_CLOVEK = "X"
IGRALEC_RACUNALNIK = "O"

class Igra:
	def __init__(self):
		self.tablica = [
							 PRAZNO, PRAZNO, PRAZNO, 
							 PRAZNO, PRAZNO, PRAZNO,
							 PRAZNO, PRAZNO, PRAZNO
						]

	def clovek(self, polje):
		if self.tablica[polje] == PRAZNO:
			self.tablica[polje] = IGRALEC_CLOVEK
		else:
			return False

	def racunalnik(self):
		while True:
			polje = random.randint(0, 8)
			if self.tablica[polje] == PRAZNO:
				self.tablica[polje] = IGRALEC_RACUNALNIK
				return polje
				break

	def __repr__(self):
		return 'Igra({})'.format(self.tablica)

	def __str__(self):
		return(self.tablica[0] + " | " + self.tablica[1] +  " | "  + self.tablica[2] + "\n" +\
			"----------" + "\n" +\
			self.tablica[3] + " | " + self.tablica[4] +  " | "  + self.tablica[5] + "\n" +\
			"----------" +"\n" +\
			self.tablica[6] + " | " + self.tablica[7] +  " | "  + self.tablica[8] + "\n")

	def zmagovalne_kombinacije_clovek(self):
		# Preveri vrstice
		if self.tablica[0] == self.tablica[1] == self.tablica[2] == IGRALEC_CLOVEK or \
			self.tablica[3] == self.tablica[4] == self.tablica[5] == IGRALEC_CLOVEK or \
			self.tablica[6] == self.tablica[7] == self.tablica[8] == IGRALEC_CLOVEK:
				return True

		# Preveri stolpce 
		if self.tablica[0] == self.tablica[3] == self.tablica[6] == IGRALEC_CLOVEK or \
			self.tablica[1] == self.tablica[4] == self.tablica[7] == IGRALEC_CLOVEK or \
			self.tablica[2] == self.tablica[5] == self.tablica[8] == IGRALEC_CLOVEK:
				return True
	
		# Preveri diagonale
		if self.tablica[0] == self.tablica[4] == self.tablica[8] == IGRALEC_CLOVEK or \
			self.tablica[2] == self.tablica[4] == self.tablica[6] == IGRALEC_CLOVEK:
				return True

	def zmagovalne_kombinacije_racunalnik(self):
		# Preveri vrstice
		if self.tablica[0] == self.tablica[1] == self.tablica[2] == IGRALEC_RACUNALNIK or \
			self.tablica[3] == self.tablica[4] == self.tablica[5] == IGRALEC_RACUNALNIK or \
			self.tablica[6] == self.tablica[7] == self.tablica[8] == IGRALEC_RACUNALNIK:
				return True

		# Preveri vrstice
		if self.tablica[0] == self.tablica[3] == self.tablica[6] == IGRALEC_RACUNALNIK or \
			self.tablica[1] == self.tablica[4] == self.tablica[7] == IGRALEC_RACUNALNIK or \
			self.tablica[2] == self.tablica[5] == self.tablica[8] == IGRALEC_RACUNALNIK:
				return True
	
		# Preveri diagonale
		if self.tablica[0] == self.tablica[4] == self.tablica[8] == IGRALEC_RACUNALNIK or \
			self.tablica[2] == self.tablica[4] == self.tablica[6] == IGRALEC_RACUNALNIK:
				return True

	def polna_tablica(self):
		prazna_mesta = 0
		for i in range(9):
			if self.tablica[i] == PRAZNO:
				prazna_mesta += 1
		if prazna_mesta == 0:
			return True
