def gal_lit(x):
    return x * 3.785

while True:
    gallona = float(input("Anna gallonoiden määrä: "))
    result = gal_lit(gallona)
    print("Gallonat litroina: ", result)

    if gallona <= 0:
        print("ERROR!!!")
        break