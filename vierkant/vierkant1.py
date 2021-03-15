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
			if row == 0:
				if col == 0:
					print("/", end="")
				elif col == x:
					print("\\", end="")
				else:
					print("*", end="")
			elif row == y:
				if col == 0:
					print("\\", end="")
				elif col == x:
					print("/", end="")
				else:
					print("*", end="")
			else:
				if col == 0 or col == x:
					print("*", end="")
				else:
					print(" ", end="")
		# Nieuwe regel
		print()

rush(5, 3)
