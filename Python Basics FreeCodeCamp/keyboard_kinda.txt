key  = [0, 0, 0, 0, 0]
cont = "c"
while cont == "c":
    for i in range(0, 5):
        key[i] = input("Enter your words here → ")
    cont = input("Enter c  there to see your stuff → ")
    if cont == "c":
        print(key)
    else:
        break

