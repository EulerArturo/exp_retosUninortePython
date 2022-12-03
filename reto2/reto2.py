m1 = int(input())
m2 = int(input())
cont_m1 = 0
cont_m2 = 0
pasiente = 0

while m1 > 0 and m2 > 0:
    ps = int(input())
    pd = int(input())
    pasiente = pasiente + 1
    
    if ps <89 and pd <53:
        m2 = m2 -9
        cont_m2 = cont_m2 + 1 
    elif (89 <= ps <101) and (53<= pd <71):
        print()
    elif (101 <= ps <139) and (71<= pd <88):
        print()
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
    print(pasiente)
    print( f"{cont_m1} {porcentagem1:.2f}%" )
    print(f"{cont_m2} {porcentagem2:.2f}%")
else:
    print("0")
    print("0 0.00%")
    print("0 0.00%")

