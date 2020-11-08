#Utilizînd ciclul FOR elaboraţi un program care afişează toate numerele pare, pentru intervalul de la 1 la n

n = int(input("dati un numar "))
for n in range(0,n+1,+2):
    if n!=0:
     print(n) 