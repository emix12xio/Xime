control=0
while control<1:
    print('')    
    print('bienvenidos')
    print('')
    print('1. numeros del 0 a 10')
    print('2. numeros romanos')
    print('3. dias de la semana')
    print('4. numeros primos')
    print('5. salir')
    print('')
    option=int(input('elige una opcion: '))

    if option==1:
       for x in range(0,11):
           print(x)
    if option==2:
      for x in ['I','II','III','IV','V']:
          print(x)
      
    if  option==3:
        for x in ['lunes','martes', 'miercoles','jueves','viernes']:
           print(x)
       
    if  option==4:
        for x in[1,3,7]:
           print(x)
    if  option==5:
         control=2 
