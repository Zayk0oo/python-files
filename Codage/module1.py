operande=int(input("Votre table de muntiplication"))
for n in range(1,21):
    somme=0
    for i in range(140):
        if i % 3 == 0:
            somme+= i
    print(somme)
    print(operande,"*",n,"=",n*operande)
