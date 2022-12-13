def procesos():
 
     ps = int(input('ingresar presión sistólica: ' ))
     pd = int(input('Ingresar presión diastólica: ' ))

     cat=['Hipotencion','Ideal','Comun','Comun-alta','HTAG1','HTAG2','HTAG3','HTASA']
     colores = ['Amarilla','Verde','Naranja','Roja','Gris']

     if ps <89 and pd <53:
          print(format((cat[0]) ),"Alerta", format(colores[0]) )
     elif (89 <= ps <101) and (53<= pd <71):
          print(format((cat[1]) ),"Alerta", format(colores[1]))
     elif (101 <= ps <139) and (71<= pd <88):
          print(format((cat[2]) ),"Alerta", format(colores[1]))
     elif (139 <= ps <156) and (88<= pd <105):
          print(format((cat[3]) ),"Alerta", format(colores[0]))
     elif (156 <= ps <172) and (105<= pd <124):
          print(format((cat[4]) ),"Alerta", format(colores[2]))
     elif (172 <= ps <223) and (124<= pd <143):
          print(format((cat[5]) ),"Alerta", format(colores[2]))
     elif ps >= 223 and pd >= 143:
          print(format((cat[6]) ),"Alerta", format(colores[3]))
     elif ps>=142 and pd < 103:
          print(format((cat[7]) ),"Alerta", format(colores[3]))
     else:
          print("No se puede determinar la categoría alerta", format(colores[4])) 

print('**********************************************************************************')
print('\t Programa para calcular la presión del corazón ')
print('Bienvenido')


while True:
     continuar = input('\n¿Deseas calcular su presión arterial?: (S/N) ').upper()
     if continuar == 'N':
          print('Gracias por utilizar nuestra aplicación vuelva pronto \n')
          break
     elif continuar == 'S':
          try:
               procesos()
          except ValueError:
               print('las presiones van en números')
     else:     
          print("la opción ¿Deseas calcular su presión arterial? solo responde con la letra 'S' para decir si y la letra 'N' para decir no")
