#Utilizînd ciclul FOR elaboraţi un program care să calculeze suma numerelor de la 1 la n, care se împart la 3 şi 5 pentru oricare n întrodus de la tastatură

s=0
i=0
n=int(input("dati numarul n: "))
for i in range(1,n):
    if(i%3==0) and (i%5==0):
        s+=i
print(s) 