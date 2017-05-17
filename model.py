
tablica = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def izpisi_tablico():
	print(tablica[1] + " | " + tablica[2] +  " | "  + tablica[3])
	print("----------")
	print(tablica[4] + " | " + tablica[5] +  " | "  + tablica[6])
	print("----------")
	print(tablica[7] + " | " + tablica[8] +  " | "  + tablica[9])

def vnesi(igralec):
	polje = int(input("Izberi prazno polje za " + igralec + ": "))
	# preveri, če je izbrano polje prazno
	if tablica[polje] == str(polje):
		tablica[polje] = igralec
	else:
		print("To polje je že zasedeno! Izberi drugo polje.")
		izpisi_tablico()
		vnesi(igralec)
	izpisi_tablico()
	print()


def zmagovalne_kombinacije(igralec):
	# preveri vrstice
	if tablica[1] == tablica[2] == tablica[3] == igralec or \
		tablica[4] == tablica[5] == tablica[6] == igralec or \
		tablica[7] == tablica[8] == tablica[9] == igralec:
			return True

	# preveri stolpce
	if tablica[1] == tablica[4] == tablica[7] == igralec or \
		tablica[2] == tablica[5] == tablica[8] == igralec or \
		tablica[3] == tablica[6] == tablica[9] == igralec:
			return True

	# preveri diagonale
	if tablica[1] == tablica[5] == tablica[9] == igralec or \
		tablica[3] == tablica[5] == tablica[7] == igralec:
			return True

def polna_tablica():
	prazna_mesta = 0
	for i in range(1, 10):
		if tablica[i] == str(i):
			prazna_mesta += 1
	return prazna_mesta
			



izpisi_tablico()
while True:

	vnesi("X")
	if zmagovalne_kombinacije("X"):
		izpisi_tablico()
		print("Igralec X je zmagovalec!")
		break

	if polna_tablica() == 0:
		print('Neodločeno!')
		break

	vnesi("O")
	if zmagovalne_kombinacije("O"):
		izpisi_tablico
		print("Igralec O je zmagovalec!")
		break
			
	if polna_tablica() == 0:
		print('Neodločeno!')
		break


# V datoteko zapisi trenutno stanje
# Graficni vmesnik


