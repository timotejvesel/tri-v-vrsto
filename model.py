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
		trojice = {
			(0, 1, 2), (0, 2, 1), (1, 2, 0), (3, 4, 5),
		 	(4, 5, 3), (3, 5, 4), (6, 7, 8), (7, 8, 6), 
		 	(6, 8, 7), (0, 3, 6), (3, 6, 0), (0, 6, 3), 
		 	(1, 4, 7), (4, 7, 1), (1, 7, 4), (2, 5, 8), 
		 	(5, 8, 2), (2, 8, 5), (0, 4, 8), (4, 8, 0), 
		 	(0, 8, 4), (2, 4, 6), (4, 6, 2), (2, 6, 4)
		}

		if self.tablica[4] == PRAZNO:
			self.tablica[4] = IGRALEC_RACUNALNIK
			polje = 4
			return polje

		elif any(self.tablica[x[0]] == self.tablica[x[1]] != PRAZNO and \
				self.tablica[x[2]] == PRAZNO for x in trojice):
					a = next(x[2] for x in trojice if self.tablica[x[0]] == self.tablica[x[1]] != PRAZNO and \
						self.tablica[x[2]] == PRAZNO)

					self.tablica[a] = IGRALEC_RACUNALNIK
					polje = a
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

	def zmagovalne_kombinacije(self, igralec):
		kombinacije = {
			(0, 1, 2), (3, 4, 5), (6, 7, 8),
			(0, 3, 6), (1, 4, 7), (2, 5, 8),
			(0, 4, 8), (2, 4, 6),
		}

		return any(
			self.tablica[x[0]] == self.tablica[x[1]] == self.tablica[x[2]] == igralec
		 	for x in kombinacije)

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
