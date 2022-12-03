def funcion1(n,k,m ): #n = sucursales m= pasientes
    
    while n<1 or k<1 or m<1:
        print("ingrese nuevamente")
        n,k,m = map(int, input().split())
    

def funcion2(n):    
    for i in range(n): 
        print(f"cantidad de medicamentos para {i+1} ips")
        cant_med = list(map(int,input().split())) # por cada sucursal diferentes tipos de medicamentos 
        cant1.append(cant_med) 
        cant2.append(cant_med) 
        
def suma(m1,m2):
    if len(m1)==len(m2) and len(m1[0]) == len(m2[0]):
        med_entr = []
        for i in range(len(m1)):
            med_entr.append([])
            for j in range(len(m1[0])):
                med_entr[i].append(m1[i][j] - m2[i][j])
        return med_entr
    else:
        return None


def funcion3(m):
    for a in range(m):      # a cada paciente se le va a pedir los datos de numero de susursal, ps, pd. 
        print(f"Ingrese datos pasiente numero {a+1}: 1. ns, 2. ps, 3. pd  ")
        ns,k,n_existen,ps,pd = map(int, input().split())
        ns = ns-1
        k = k-1
        
        if 0 < ns <= n  and n_existen > 0:

            if ps <83 and pd <48:
                cant1[ns][k]=cant1[ns][k]-n_existen
                med_entr[ns][k]=med_entr[ns][k]+n_existen
                x[ns][k] += 1
                conPac.append(x)        
            elif 83<=ps<124 and 48<=pd<66:
                cant1[ns][k]=cant1[ns][k]-n_existen
                x[ns][k] += 1
                conPac.append(x)
            elif 124<=ps<141 and 66<=pd<83:
                cant1[ns][k]=cant1[ns][k]-n_existen
                x[ns][k] += 1
                conPac.append(x)
            elif 141<=ps<158 and 83<=pd<97:
                cant1[ns][k]=cant1[ns][k]-n_existen
                med_entr[ns][k]=med_entr[ns][k]+n_existen
                x[ns][k] += 1
                conPac.append(x)
            elif 158<=ps<186 and 97<=pd<112:
                cant1[ns][k]=cant1[ns][k]-n_existen
                med_entr[ns][k]=med_entr[ns][k]+n_existen
                x[ns][k] += 1
                conPac.append(x)
            elif 186<=ps<197 and 112<=pd<128:
                cant1[ns][k]=cant1[ns][k]-n_existen
                med_entr[ns][k]=med_entr[ns][k]+n_existen
                x[ns][k] += 1
                conPac.append(x)
            elif ps>=197 and pd>=128:
                cant1[ns][k]=cant1[ns][k]-n_existen
                med_entr[ns][k]=med_entr[ns][k]+n_existen
                x[ns][k] += 1
                conPac.append(x)
            elif ps>=159 and pd<94:
                cant1[ns][k]=cant1[ns][k]-n_existen
                med_entr[ns][k]=med_entr[ns][k]+n_existen
                x[ns][k] += 1
                conPac.append(x)
            else:
                cant1[ns][k]-n_existen
                x[ns][k] += 1
                conPac.append(x)


def funcion4(m1,m2):

    if len(m1)==len(m2) and len(m1[0]) == len(m2[0]):
        tipoM = []
        for i in range(len(m1)):
            tipoM.append([])
            for j in range(len(m1[0])):
                tipoM[i].append(m1[j][i])
        return tipoM
    else:
        return None
                

def sumar_valores(m):
    if m == []:
        suma = 0
    else:
        suma = m[0] + sumar_valores(m[1:])     
    return suma
    
    

###########################################################################

cant1 = []
cant2 = []
med_entr = []
conPac = []
entrega = []  
x = []
tipoM = []
tipom2 = []
maximos =[]
minimos =[]
y = 0
########################################################################################
print("ingresa datos")
n,k,m = map(int, input().split())

funcion1(n, k, m)
    # funcion para identificar si sucursal o tipo medicamento o pacientes  es igual a 0
funcion2(n)
med_entr = suma(cant1, cant2)
x = suma(cant1, cant2)
########################################################################################

funcion3(m)

for i in range(n):
    print(i+1)
    filaMin = min(cant1[i])
    s_min = cant1[i].index(filaMin)
    print(s_min+1,filaMin)
    filaMax = max(cant1[i])
    s_max = cant1[i].index(filaMax)
    print(s_max+1,filaMax)
################################################################
    filaMin = min(med_entr[i])
    l = sumar_valores(med_entr[i])
    y = l / len(med_entr[i])
    filaMax = max(med_entr[i])
    print(f"{filaMin:.2f} {y:.2f} {filaMax:.2f}")
################################################################
    g = sumar_valores(med_entr[i])
    print("vlor de g",g)
    d = sumar_valores(x[i])
    print("vlor de d", d)
    if g == 0:
        print(f"{g:.2f}")
    else:
        s = g / d
        print(f"{s:.2f}")
#################################################################

filaMin = min(med_entr)
s_min = med_entr.index(filaMin)
filaMax = max(med_entr)
s_max = med_entr.index(filaMax)

print(s_min+1,filaMin[0])
print(s_max+1,filaMax[0])


# print("cantidad despues de ", cant1)
print("medicamentos entregados", med_entr)
print("x ", x)
# print("maximos" , maximos)
# print("minimos", minimos)
