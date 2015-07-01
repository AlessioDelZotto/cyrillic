iterate = 0
while iterate == 0:
	gender = input("Calcolo del peso forma \nScrivi 1 se sei un uomo, 2 se sei una donna: ")
	weight = input("Inserisci il tuo peso in kilogrammi: ")
	height = input("Inserisci la tua altezza in centimetri: ")
	if gender == 1:
		delta = 100
	else:
		delta = 104
	idealweight = 0.95 * (height - delta)
	idwe = (idealweight // 1)
	if idwe >= weight:
		print("Complimenti sei in forma!")
		iterate = 1
	else:
		print("Sei in sovrappeso!")
