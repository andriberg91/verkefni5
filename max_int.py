# Finna og prenta stærstu innsettu töluna. 
# Ef innsett tala er stærri en -1 þá setja hana sem max_int
# Ef næsta tala sem er sett inn er stærri en sú fyrri þá yfirskrifa hana sem max_int
# Framkvæma þetta þangað til tala minni en 0 er innsett.
# Prenta max_int (Hæðsta tala sem hefur verið slegið inn)

num_int = int(input("Input a number: "))

max_int= 0

while num_int >= 0:
	if num_int > max_int:
		max_int = num_int
	num_int = int(input("Input a number: "))
print("The maximum is", max_int)
