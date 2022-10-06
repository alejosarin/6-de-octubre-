n = int(input("\ndigite un numero entero positivo : "))
calculo =n
suma=0
while n<0:
    print("ES un digito negativo")
    n = int(input("\ndigite un numero entero positivo : "))

calculo =n
suma=0

while calculo != 0:
    digito=(calculo%10)
    calculo=(calculo-digito)//10
    suma=suma+digito
print("\n\nEl resultado de la suma es : "+str(suma)+ "  Del numero : "+str(n))
    
    
    



