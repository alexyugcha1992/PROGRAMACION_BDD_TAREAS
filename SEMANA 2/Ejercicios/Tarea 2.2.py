"""numero par"""
# n1 = int (input("ingresa un numero:"))
# if n1%2==0:
#     print ("el numero es par")
# else :
#     print ("el numero es impar")


# """numero mayor"""
# n1= int(input ("ingrese primer numero"))
# n2= int(input ("ingrese segundo numero"))
# n3= int(input ("ingrese tercer numero"))
# if n2 < n1 > n3:
#     print("el numero mayor es el primer numero:",n1)
# elif n1 < n2 > n3:
#     print("el numero mayor es el segundo numero:",n2)
# elif n1 < n3 > n2:    
#     print("el numero mayor es el tercer numero:",n3)
# else :
#     print("los numeros son iguales")      

# """ordenacion de tres numeros"""

# n1= int(input ("Ingrese el primer numero:"))
# n2= int(input ("Ingrese el segundo numero:"))
# n3= int(input ("Ingrese el tercer numero:"))
# if n1 > n2 and n2 > n3:
#     print("El numero mayor es: ",n1, "  El numero medio es: ",n2, "  El numero menor es: ",n3)
# elif n2 > n1 and n1 > n3:
#     print("El numero mayor es: ",n2, "  El numero medio es: ",n1, "  El numero menor es: ",n3)
# elif n3 > n1 and n1 > n2:
#     print("El numero mayor es: ",n3, "  El numero medio es: ",n1, "  El numero menor es: ",n2)
# elif n3 > n2 and n2 > n1:
#     print("El numero mayor es: ",n3, "  El numero medio es: ",n2, "  El numero menor es: ",n1)
# elif n1 > n3 and n3 > n2:
#   print("El numero mayor es: ",n1, "  El numero medio es: ",n3, "  El numero menor es: ",n2)
# elif n2 > n3 and n3 > n1:
#   print("El numero mayor es: ",n2, "  El numero medio es: ",n3, "  El numero menor es: ",n1)
# else:
#      print("ingrese numeros diferentes")

# """numero multiplo de otro"""

# n1= int(input ("Ingrese el primer numero:"))
# n2= int(input ("Ingrese el segundo numero:"))
# if n1 % n2 == 0:
#   print ("El numero ", n2, "es multiplo de ", n1)
# else:
#   print ("El numero ", n2, "no es multiplo de ", n1) 
 
 
    
"""año bisiesto"""
año = int(input('Introduce un año: '))

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print('El año es bisiesto')
        else:
            print('El año no es bisiesto')
    else:
        print('El año es bisiesto.')
else:
    print('El año no es bisiesto.')