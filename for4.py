#Utilizînd ciclul FOR elaboraţi un program care afişează toate numerele impare, pentru intervalul de la a la b

a = int(input("dati numarul a: "))
b = int(input("dati numarul b: "))
for a in range(a,b,+1):
    if a %2!=0:
       print(a) 