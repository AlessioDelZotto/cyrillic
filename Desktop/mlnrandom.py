#Calculates how many random numbers are even or odd out of a million
#The result is always different!

import random
x = 0
pari = 0
dispari = 0
while x < 1000000: 
	n = (random.random() * 100000000000) // 1
	if n % 2 == 0:
		pari = pari + 1
		x = x + 1
	else:
		dispari = dispari + 1
		x = x + 1
print("Un milione di numeri a caso")
print("\nNumeri pari:")
print pari
print("\nNumeri dispari:")
print dispari
