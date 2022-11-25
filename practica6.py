import random
num1= random.randint(1,20)
nom=input('cual es tu nombre')
vidas=0
print(f'hola',nom,'estoy pensando en un numero')
print('te reto a adivinarlo?')

while vidas<6:
    num2=int(input('cual es tu numero:'))
    vidas=vidas+1
    if num1==num2:
        print('en hora buena felicitaciones acertaste')
        break
    elif num1>num2:
        print('vas muy bajo')
    elif num1<num2:
        print('vas muy alto')
    else:
       if vidas==6:
           print('el numero es:',num1)

