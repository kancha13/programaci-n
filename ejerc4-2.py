numero1=input("dame un numero")
numero2=input("dame otro numero")
for i in range(numero1,numero2+2):
    if i %2==0:
        print i,"si es par"
    else:
        print i,"si es impar"
