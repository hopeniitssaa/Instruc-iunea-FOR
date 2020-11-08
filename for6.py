n=int(input("Dati un numar: "))
s1=0
s2=0
s5=0
s6=0
for num in range(1, n):
    s1 +=num
    s2 +=((num - 1) * num)
    s5 +=(num / (num + 1))
    s6 +=(20 + num)
s3=1
factorial =1
for num in range(2, n):
    factorial *= num
    s3 += factorial
s4 = 0
for num in range(1, ((n * 10) + 1)):
    if (num % 10 == 0):
        s4 += (num + 2)

print("s1 =", s1, "  s2 =", s2, "  s3 =", s3, "  s4 =", s4, "  s5 =", s5, "  s6 =", s6) 