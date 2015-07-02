iter = 0
print("Scopri la combinazione giusta ed esci dal labirinto")
while iter == 0:
	n1 = input("\nScrivi la prima cifra: ")
	n2 = input("\nScrivi la seconda cifra: ")
	n3 = input("\nScrivi la terza cifra: ")
	n4 = input("\nScrivi la quarta cifra: ")
	n5 = input("\nScrivi la quinta cifra: ")
	if n1 == 4:
		print("\nClic")
		if n2 == 5:
			print("\nClic")
			if n3 == 2:
				print("\nClic")
				if n4 == 7:
						print("\nClic")
						if n5 == 6:
							print("\nClic")
							print("\nComplimenti! Sei uscito dal labirinto!")
							iter = 1 
	else:
		print("\nErrore! Ritenta")
		
