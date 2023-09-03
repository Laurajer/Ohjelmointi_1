#Kysy käyttäjältä hyttiluokka. tulostaa Sanallisen kuvauksen. if else elif

hyttiluokka = input("Mikä hyttiluokka? ")
if hyttiluokka == 'LUX':
    print('LUX on parvekkeellinen hytti yläkannella.')
elif hyttiluokka == 'A':
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif hyttiluokka == 'B':
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif hyttiluokka == 'C':
    print('C on ikkunaton hytti autokannen alaåuolella.')
else:
    print('Virheellinen hyttiluokka.')