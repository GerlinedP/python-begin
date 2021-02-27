namen = ["kees", "piet", "amalia", "pieter-jan"]

# Verander item op index 1 naar gerrie
namen[1] = "gerrie"

# Print origineel
for naam in namen:
	print("Hallo", naam)

print(namen)

print("-----------")

# Krijg de lengte van wat we in len() gooien
len(namen) # Hier komt 4 uit

# Maak een range
range(4)
# Hier komt uit: --> [0, 1, 2, 3]

# Verander naar hoofdletters
for index in range(len(namen)):
	namen[index] = namen[index].upper()

# Print opnieuw
for naam in namen:
	print("Hallo", naam)

print(namen)
