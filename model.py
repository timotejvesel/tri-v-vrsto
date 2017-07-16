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
		if self.tablica[4] == PRAZNO:
			self.tablica[4] = IGRALEC_RACUNALNIK
			polje = 4
			return polje
		elif self.tablica[0] == self.tablica[1] != PRAZNO and \
		   self.tablica[2] == PRAZNO:
			self.tablica[2] = IGRALEC_RACUNALNIK
			polje = 2
			return polje
		elif self.tablica[0] == self.tablica[2] != PRAZNO and \
		   self.tablica[1] == PRAZNO:
			self.tablica[1] = IGRALEC_RACUNALNIK
			polje = 1
			return polje
		elif self.tablica[1] == self.tablica[2] != PRAZNO and \
		   self.tablica[0] == PRAZNO:
			self.tablica[0] = IGRALEC_RACUNALNIK
			polje = 0
			return polje
		elif self.tablica[3] == self.tablica[4] != PRAZNO and \
		   self.tablica[5] == PRAZNO:
			self.tablica[5] = IGRALEC_RACUNALNIK
			polje = 5
			return polje
		elif self.tablica[4] == self.tablica[5] != PRAZNO and \
		   self.tablica[3] == PRAZNO:
			self.tablica[3] = IGRALEC_RACUNALNIK
			polje = 3
			return polje
		elif self.tablica[3] == self.tablica[5] != PRAZNO and \
		   self.tablica[4] == PRAZNO:
			self.tablica[4] = IGRALEC_RACUNALNIK
			polje = 4
			return polje
		elif self.tablica[6] == self.tablica[7] != PRAZNO and \
		   self.tablica[8] == PRAZNO:
			self.tablica[8] = IGRALEC_RACUNALNIK
			polje = 8
			return polje
		elif self.tablica[7] == self.tablica[8] != PRAZNO and \
		   self.tablica[6] == PRAZNO:
			self.tablica[6] = IGRALEC_RACUNALNIK
			polje = 6
			return polje
		elif self.tablica[6] == self.tablica[8] != PRAZNO and \
		   self.tablica[7] == PRAZNO:
			self.tablica[7] = IGRALEC_RACUNALNIK
			polje = 7
			return polje
		elif self.tablica[0] == self.tablica[3] != PRAZNO and \
		   self.tablica[6] == PRAZNO:
			self.tablica[6] = IGRALEC_RACUNALNIK
			polje = 6
			return polje
		elif self.tablica[3] == self.tablica[6] != PRAZNO and \
		   self.tablica[0] == PRAZNO:
			self.tablica[0] = IGRALEC_RACUNALNIK
			polje = 0
			return polje
		elif self.tablica[0] == self.tablica[6] != PRAZNO and \
		   self.tablica[3] == PRAZNO:
			self.tablica[3] = IGRALEC_RACUNALNIK
			polje = 3
			return polje
		elif self.tablica[1] == self.tablica[4] != PRAZNO and \
		   self.tablica[7] == PRAZNO:
			self.tablica[7] = IGRALEC_RACUNALNIK
			polje = 7
			return polje
		elif self.tablica[4] == self.tablica[7] != PRAZNO and \
		   self.tablica[1] == PRAZNO:
			self.tablica[1] = IGRALEC_RACUNALNIK
			polje = 1
			return polje
		elif self.tablica[1] == self.tablica[7] != PRAZNO and \
		   self.tablica[4] == PRAZNO:
			self.tablica[4] = IGRALEC_RACUNALNIK
			polje = 4
			return polje
		elif self.tablica[2] == self.tablica[5] != PRAZNO and \
		   self.tablica[8] == PRAZNO:
			self.tablica[8] = IGRALEC_RACUNALNIK
			polje = 8
			return polje
		elif self.tablica[5] == self.tablica[8] != PRAZNO and \
		   self.tablica[2] == PRAZNO:
			self.tablica[2] = IGRALEC_RACUNALNIK
			polje = 2
			return polje
		elif self.tablica[2] == self.tablica[8] != PRAZNO and \
		   self.tablica[5] == PRAZNO:
			self.tablica[5] = IGRALEC_RACUNALNIK
			polje = 5
			return polje
		elif self.tablica[0] == self.tablica[4] != PRAZNO and \
		   self.tablica[8] == PRAZNO:
			self.tablica[8] = IGRALEC_RACUNALNIK
			polje = 8
			return polje
		elif self.tablica[4] == self.tablica[8] != PRAZNO and \
		   self.tablica[0] == PRAZNO:
			self.tablica[0] = IGRALEC_RACUNALNIK
			polje = 0
			return polje
		elif self.tablica[0] == self.tablica[8] != PRAZNO and \
		   self.tablica[4] == PRAZNO:
			self.tablica[4] = IGRALEC_RACUNALNIK
			polje = 4
			return polje
		elif self.tablica[2] == self.tablica[4] != PRAZNO and \
		   self.tablica[6] == PRAZNO:
			self.tablica[6] = IGRALEC_RACUNALNIK
			polje = 6
			return polje
		elif self.tablica[4] == self.tablica[6] != PRAZNO and \
		   self.tablica[2] == PRAZNO:
			 self.tablica[2] = IGRALEC_RACUNALNIK
			 polje = 2
			 return polje
		elif self.tablica[2] == self.tablica[6] != PRAZNO and \
		   self.tablica[4] == PRAZNO:
			self.tablica[4] = IGRALEC_RACUNALNIK
			polje = 4
			return polje
		else:
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

	def nova_igra(self):
		for i in range(9):
			self.tablica[i] = PRAZNO





