while True:
	x_from, x_to = 1, 1000
	x = input ("Vvedit znachennya vid 1 do 1000:")
	x = int(x)

	if x_from <= x <= x_to:
		break
	else:
		print("Sprobuyte sche raz")
while True:
	# ввід
	y = input ("Znachennya 2 =")

	# умова
	# 1. int(y) - 10 == x
	if x == int(y):
		print("Hureyyyyy!!!!! You got me!!!")
		break
	elif x > int(y):
		print("Bilshe!")
	elif x < int(y):
		print("Menshe")
