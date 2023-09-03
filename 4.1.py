#while-toistorakennetta käyttävä ohjelma,
# joka tulostaa kolmella jaolliset luvut väliltä 1..1000.
maximum = 1000
number = 1
while number <= maximum:
    if(number % 3== 0):
        print("{0}".format(number))
    number = number +1