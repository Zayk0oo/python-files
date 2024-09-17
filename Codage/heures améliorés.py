h=int(input("Choisissez les heures : "))
m=int(input("Choisissez les minutes : "))
s=int(input("Choisissez les secondes : "))
a=h*3600+m*60+s

if h<0 or m<0 or s<0:
    print("Merci de saisir des nombres positifs")
else:
    print("Votre nombre de secondes est : ", a)