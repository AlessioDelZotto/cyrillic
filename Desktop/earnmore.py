iterate = 0
while iterate == 0:
	hrinc = input("Calcolo del reddito \tIncome calculator \n \nScrivi quanto guadagni mediamente ogni ora \nHow much do you earn per hour? ")
	wkhrs = input("\nIndica quante ore alla settimana lavori mediamente. \nHow many hours do you work per week? ")
	wkayr = input("\nQuante settimane lavori in un anno? \nHow many weeks do you work per year? ")
	incrs = input("\nQuanto vorresti guadagnare in un anno? \nHow much would you like to earn each year? ")
	delta = (hrinc * wkhrs * wkayr) - incrs
	if delta >= 0:
		print("\nComplimenti per il tuo successo! \nCongratulations for your success!")
		iterate = 1
	else:
		print("\nDevi ancora lavorare per raggiungere il tuo obiettivo. \nYou still have to work in order to reach your goal. \n")
