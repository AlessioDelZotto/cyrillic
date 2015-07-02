#Here is an example for the calculation of transport costs.

print("Package transport costs")

weight = input("\nInsert the weight (g): ")
width = input("\nInsert the width (cm): ")
length = input("\nInsert the length (cm): ")
height = input("\nInsert the height (cm): ")

volume = width * length * height
if volume > 100000:
	packcost = 80
elif volume < 8000:
	packcost = 20
else:
	packcost = 45
	
shipfee = (volume * weight) / 5000000

total = packcost + shipfee

print("\nThe package cost is (USD):")
print packcost
print("\nThe shipping fee is (USD):")
print shipfee
print("--------------------")
print("\nTOTAL (USD):")
print total
