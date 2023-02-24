def point_slope_form(x_1, y_1, m):
	"""Write the equation of a line in point-slope form"""
	x_1 = float(x_1)
	y_1 = float(y_1)
	m = float(m)
	equation = f"y - {y_1} = {m}(x - {x_1})."
	print(f"The equation of a line that has points ({x_1}, {y_1}) and slope {m} is {equation}")
	return equation

# Function call
while True:
	x_1 = input("Enter X1: ")
	if x_1 == 'q' or x_1 == 'Q':
		break
	y_1 = input("Enter Y1: ")
	if y_1 == 'q' or y_1 == 'Q':
		break
	m = input("Enter slope (m): ")
	if m == 'q' or m == 'Q':
		break
		
	try:
		point_slope_form(x_1, y_1, m)
	except ValueError:
		print("Invalid entry!")
		continue