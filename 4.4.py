import random

n = random.randrange(1,10)
guess = int(input('Anna kokonaisluku: '))
while n!= guess:
    if guess < n:
        print('Liian pieni')
        guess = int(input('Anna uusi kokonaisluku: '))
    elif guess > n:
        print('Liian suuri')
        guess = int(input('Anna uusi kokonaisluku: '))
    else:
        break
print('Arvasit oikein!')