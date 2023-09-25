def laskee_summan(numbers):
    yht = sum(numbers)
    return yht

if __name__ == "__main__":
    kokonaisluvut_lista = [1,2,3,66,666]

    total_sum = laskee_summan(kokonaisluvut_lista)

    print("Kokonaislukujen summa on: ", total_sum)