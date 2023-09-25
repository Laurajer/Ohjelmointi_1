# Funktio: poistaa listasta parittomat
def poistaa_parittomat(z):
    parilliset = [num for num in z if num % 2 == 0]
    return parilliset


kokonaisluvut = [1,22,31,23,24,122]

korjattu = poistaa_parittomat(kokonaisluvut)

print("Alkuperäinen lista ", kokonaisluvut ,"Korjattu lista ", korjattu)