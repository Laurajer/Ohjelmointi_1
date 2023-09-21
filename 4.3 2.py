import math

def main():

    pienin : float = math.inf
    suurin : float = -math.inf
    while True:
        userInput : str = input('Anna luku: ')
        if userInput == "":
            if pienin == math.inf and suurin == -math.inf:
                print('Anna luku: ')
                break
            print(f'Pienin luku on {pienin} ja suurin luku on {suurin}.')
            break
        pienin = min(pienin, float(userInput))
        suurin = max(suurin, float(userInput))


main()