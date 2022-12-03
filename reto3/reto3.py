def funcion1(n,m): #n = sucursales m= pasientes
    while n<1 or m<1:
        print("ingrese nuevamente")
        n,m = map(int, input().split())

def funcion2(n):
    
    for i in range(n): # por cada sucursal una cantidad de medicamentos
        print(f"cantidad de medicamentos para {i+1} ips")
        cant_med = int(input())
        while cant_med < 1: # mientras cant_med sea menor que 1 musestre mensaje de error
            print(f"'Error' cantidad de medicamentos para {i+1} ips")
            cant_med = int(input())
        cant1.append(cant_med) # creo tres varibles 1. la que voy a realizar los procesos
        cant2.append(cant_med) # 2. donde voy a guardar las cantidades iniciales de medicamentos
        med_entr.append(0)     # 3. para que me cree los puestos donde van a ir las cantidades de medicamentos a entregar
    print(med_entr)                        
def funcion3(m):
    for a in range(m):      # a cada paciente se le va a pedir los datos de numero de susursal, ps, pd. 
        print(f"Ingrese datos pasiente numero {a+1}: 1. ns, 2. ps, 3. pd  ")
        ns,ps,pd = map(int, input().split())
        
        if ps <83 and pd <48:
            cant1[ns-1]-=15      # resto a cantidad de medicamentos segun la sucursal del pasiente
            med_entr[ns-1]+=15   # sumo los medicamentos entregados segun la sucursal del paciente
        elif 83<=ps<124 and 48<=pd<66:
            cant1[ns-1]-=0      # como en la tabla contiene 0
        elif 124<=ps<141 and 66<=pd<83:
            cant1[ns-1]-=0
        elif 141<=ps<158 and 83<=pd<97:
            cant1[ns-1]-=3
            med_entr[ns-1]+=3
        elif 158<=ps<186 and 97<=pd<112:
            cant1[ns-1]-=6
            med_entr[ns-1]+=6
        elif 186<=ps<197 and 112<=pd<128:
            cant1[ns-1]-=18
            med_entr[ns-1]+=18
        elif ps>=197 and pd>=128:
            cant1[ns-1]-=30
            med_entr[ns-1]+=30
        elif ps>=159 and pd<94:
            cant1[ns-1]-=24
            med_entr[ns-1]+=24
        else:
            print()

def funcion4(cant1):
    minimo = min(cant1)         # saco la cantidad minima de la variable que estoy utilizando
    s_min = cant1.index(minimo)  # saco el indice de esa cantidad minima de la variable que estoy utilizando
    maximo = max(cant1)         # saco la cantidad maxima de la variable que estoy utilizando
    s_max = cant1.index(maximo) # saco el indice de esa cantidad maxima de la variable que estoy utilizando
    print(s_min+1,minimo)       # como el indice lo toma por puestos le sumo 1 y queda y concateno la cantidad minima
    print(s_max+1,maximo)       # como el indice lo toma por puestos le sumo 1 y queda y concateno la cantidad maxima

def funcion5(n):
    for b in range(n):        # que por cada sucursal me ejecute esta formula
        porcentaje = (med_entr[b]/cant2[b])*100  # porcent = indice de medicamentos entregados / indice de cantidades iniciales * 100
        print(f"{b+1} {porcentaje:.2f}%")       # imprimo indice + 1 por las pociciones  y el porcentaje redondeado a dos decimales 

###########################################################################

cant1 = []
cant2 = []
med_entr = []
print("ingresa datos")
n,m = map(int, input().split())
funcion1(n, m)    # funcion para identificar si sucursal o pacientes es igual a 0
funcion2(n)       # funcion para dar cantidades de exixtencias a n sucursales
funcion3(m)       # funcion para pedir datos al paciente y segun su sucursal y su precion el sistema le recete cierta cantidad de medicamento 
funcion4(cant1)   # funcion para sacar la cantidad minima y maxima de las existencias de todas las sucursal
funcion5(n)       # funcion para sacar el porcentaje de cantidades entregadas de cada una de las sucursales  
