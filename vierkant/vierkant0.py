def rush(x, y):
	# Check getallen
	if x <= 0 or y <= 0:
		print("Kerel wtf")
		return
	# Omdat python
	x -= 1
	y -= 1
	# Loop over alle getallen van 0 tm y
	for row in range(y + 1):
		# Loop over alle getallen van 0 tm x
		for col in range(x + 1):
			# Top / bottom line
			if (row == 0 or row == y):
				# Hoekje
				if col == 0 or col == x:
					print("o", end="")
				# De rest
				else:
					print("-", end="")
			else:
				# Links / Rechts
				if col == 0 or col == x:
					print("|", end="")
				# Binnenkant
				else:
					print(" ", end="")
		# Nieuwe regel
		print()

rush(5, 5)
