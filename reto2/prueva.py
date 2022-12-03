# 1. necesito que al cometer errores no se reinicie como tal  las cantidades
# 2. que solo al precionar la letra n se cancelan todos los procesos y que en caso de
# presionar alguna otra letra se continue normal

def medicamentos():

    print('Digite las dos cantidades de medicamentos separadas por un espacio ej: 50 80 ')
    m1,m2 = map(int,input().split())
    return m1,m2

def presion (m1,m2):

    cont_m1, cont_m2, pasiente = 0, 0, 0
    while m1 > 0 and m2 > 0:
        print( f'\nexistencias medicamento #1: {m1}, existencias medicamento #2: {m2}')
        print('por favor ingrese su presion diastólica y sistolica separadas por un espacio ej; 180 50')
        ps,pd = map(int,input().split())
        pasiente = pasiente + 1
        
        if ps <89 and pd <53:
            m2 = m2 -9
            cont_m2 = cont_m2 + 1 
        elif (89 <= ps <101) and (53<= pd <71):
            continue
        elif (101 <= ps <139) and (71<= pd <88):
            continue
        elif (139 <= ps <156) and (88<= pd <105):
            m1 = m1 - 2
            cont_m1 = cont_m1 + 1
            
        elif (156 <= ps <172) and (105<= pd <124):
            m1 = m1 - 7
            cont_m1 = cont_m1 + 1
            
        elif (172 <= ps <223) and (124<= pd <143):
            m1 = m1 - 13
            cont_m1 = cont_m1 + 1
            
        elif ps >= 223 and pd >= 143:
            m1 = m1 - 25
            cont_m1 = cont_m1 + 1
            
        elif ps>=142 and pd < 103:
            m1 = m1 - 16
            cont_m1 = cont_m1 + 1        
        else:
            print()

    if pasiente > 0:  
        porcentagem1 = cont_m1 * 100 / pasiente
        porcentagem2 = cont_m2 * 100 / pasiente
        print('')
        print(pasiente)
        print( f"{cont_m1} {porcentagem1:.2f}%" )
        print(f"{cont_m2} {porcentagem2:.2f}%")
    elif pasiente == 0:
        print('')
        print(pasiente)
        print("0 0.00%")
        print("0 0.00%")


print('************************************************************************************************')
print('\t Programa para la entrega de medicamentos segun  las cantidades existentes ')
print('\t\t\t\t\tBienvenido\n')

pregunta2 = True;
pregunta1 = True;

textSalida = 'gracias por utilizar nuestra aplicación vuelva pronto...\n'
textError = "(!!! la aplicacion solo acepta '2' cantidades de tipo numerico ¡¡¡)\n"
textentrada = 'desea realizar nuevo proceso (S/N): '
textContinuar = 'desea continuar  proceso (S/N): '

pregunta = input(textentrada).upper()
if pregunta == 'N':
    print(textSalida)
    pregunta1 = False;
else:
    while pregunta1 == True and pregunta2 == True:
        try:
            salida = medicamentos()
            if pregunta2 == True:
                while pregunta2 == True :
                    try:
                        presion(salida[0], salida[1])
                        pregunta = input(textentrada).upper()
                        if pregunta == 'N':
                            pregunta2 = False
                            print(textSalida)
                        
                            
                    except ValueError:
                        print(textError)
                        pregunt = input(textContinuar).upper()
                        if pregunt == 'N':
                            pregunta2 = False
                            print(textSalida)            
            else:
                print(textSalida)               
        except ValueError:
            print(textError)
            pregunta = input(textContinuar).upper()
            print(textSalida)

