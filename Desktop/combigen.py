print("Scegli cinque cifre e scopri la combinazione generata")
n1 = input("\nScegli la prima cifra: ")
n2 = input("\nScegli la seconda cifra: ")
n3 = input("\nScegli la terza cifra: ")
n4 = input("\nScegli la quarta cifra: ")
n5 = input("\nScegli la quinta cifra: ")

iter = 0

while iter == 0:
	m1 = input("\nPrima cifra della combinazione: ")
	m2 = input("\nSeconda cifra della combinazione: ")
	m3 = input("\nTerza cifra della combinazione: ")
	m4 = input("\nQuarta cifra della combinazione: ")
	m5 = input("\nQuinta cifra della combinazione: ")
	if m1 == (2**n1 % 9):
		print("\nClic")
		if m2 == (2**n2 % 9):
			print("\nClic")
			if m3 == (2**n3 % 9):
				print("\nClic")
				if m4 == (2**n4 % 9):
						print("\nClic")
						if m5 == (2**n5 % 9):
							print("\nClic")
							print("\nComplimenti! Sei uscito dal labirinto!")
							iter = 1 
	else:
		print("\nErrore! Ritenta")
