#Calculates the rest of the division by 9 
#Out of a million random numbers
#Probability is 1 divided by 9 equals 0,11.

import random
x = 0
mod1 = 0
mod2 = 0
mod3 = 0
mod4 = 0
mod5 = 0
mod6 = 0
mod7 = 0
mod8 = 0
mod9 = 0
while x < 1000000: 
	n = (random.random() * 100000000000) // 1
	if n % 9 == 1:
		mod1 = mod1 + 1
		x = x + 1
	elif n % 9 == 2:
		mod2 = mod2 + 1
		x = x + 1
	elif n % 9 == 3:
		mod3 = mod3 + 1
		x = x + 1
	elif n % 9 == 4:
		mod4 = mod4 + 1
		x = x + 1
	elif n % 9 == 5:
		mod5 = mod5 + 1
		x = x + 1
	elif n % 9 == 6:
		mod6 = mod6 + 1
		x = x + 1
	elif n % 9 == 7:
		mod7 = mod7 + 1
		x = x + 1
	elif n % 9 == 8:
		mod8 = mod8 + 1
		x = x + 1					
	else:
		mod9 = mod9 + 1
		x = x + 1
print("Un milione di numeri a caso")
print("Radice numerica 1: ")
print mod1
print("Radice numerica 2:")
print mod2
print("Radice numerica 3:")
print mod3
print("Radice numerica 4:")
print mod4
print("Radice numerica 5:")
print mod5
print("Radice numerica 6:")
print mod6
print("Radice numerica 7:")
print mod7
print("Radice numerica 8:")
print mod8
print("Radice numerica 9:")
print mod9
