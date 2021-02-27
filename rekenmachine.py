# getal opvragen
getal1 = input("Getal 1: ")
getal1 = int(getal1)

# operator opvragen
# + - / *
operator = input("Operator: ")

# getal opvragen
getal2 = input("Getal 2: ")
getal2 = int(getal2)

# uitvoeren
if (operator == "+"):
	uitkomst = getal1 + getal2
elif (operator == "-"):
	uitkomst = getal1 - getal2
elif (operator == "/"):
	uitkomst = getal1 / getal2
elif (operator == "*"):
	uitkomst = getal1 * getal2
else:
	print("Dat is balen pik")
	exit()

print(uitkomst)
