# n verður fjölda talna sem fara í röðina
# Regla á röðinni verður að eftir töluna 3 verður næsta tala summa fyrri þriggja talna sem koma undan í röðinni
# Búið verður til 3 temp sem halda tölunum og þær færast síðan um eitt sæti þegar ný tala kemur inn

n = int(input("Enter the length of the sequence: "))

counter = 1
temp_1 = 1
temp_2 = 2
temp_3 = 3

while counter < n+1:
    if counter == 1:
        print(temp_1)
        counter += 1
    if counter == 2:
        print(temp_2)
        counter += 1
    if counter == 3:
        print(temp_3)
        counter += 1
    if counter >= 4:
        temp_4 = (temp_1 + temp_2 + temp_3)
        print(temp_4)
        temp_1 = temp_2
        temp_2 = temp_3
        temp_3 = temp_4
        counter += 1

