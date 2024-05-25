import time
t0= time.time()
def print_b(m):
    for fila in m:
        for e in fila:
            print(e, end=" ")
        print()

def kataminoi(L, A):
    return [["."]*A for _ in range(L)]

def contar_caracteres(matriz):
    for pieza in matriz:
        contador=0
        for i in range(len(pieza)):
            for j in range(len(pieza[0])):
                if pieza[i][j] != ".":
                    contador+=1
    return contador

def cropPieza(matriz):
    resultado = []
    for fila in matriz:
        if fila != ['.'] * len(fila):
            resultado.append(fila)
    return resultado

def transponer(pieza):
    transpuesta = []
    for i in range(len(pieza[0])):
        nueva_fila = []
        for j in range(len(pieza)):
            nueva_fila.append(pieza[j][i])
        transpuesta.append(nueva_fila)
    return transpuesta

def crop_pieza(pieza):
    pieza_sin_filas = cropPieza(pieza)
    pieza_transpuesta = transponer(pieza_sin_filas)
    pieza_sin_columnas = cropPieza(pieza_transpuesta)
    pieza_final = transponer(pieza_sin_columnas)
    return pieza_final

# Input
L,A,P=map(int,input("").split())
def generar_piezas(P):
    contador_piezas=int(P)
    listota=[]
    while contador_piezas>0:
        pieza=[]
        for _ in range(L):
            entrada=input()
            linea=[]
            for caracter in entrada:
                linea.append(caracter)
            pieza.append(linea)
        pieza_crop=crop_pieza(pieza)
        listota.append(pieza_crop)
        contador_piezas-=1
    return listota
matriz_piezas=generar_piezas(P)

def matriz_nula(filas, columnas):
    return [[0]*columnas for _ in range(filas)]

def rotar(pieza):
    n,m=len(pieza), len(pieza[0])
    res=matriz_nula(m, n)
    for i in range(n):
        for j in range(m):
            res[j][n-1-i]=pieza[i][j]
    return res

def todas_rotaciones(pieza):
    rotaciones=[pieza]
    for _ in range(3):
        rotaciones.append(rotar(rotaciones[-1]))
    return rotaciones

total_rotaciones=[todas_rotaciones(pieza) for pieza in matriz_piezas]
sadkataminito=kataminoi(L, A)
katamino=kataminoi(L, A)

def katamino_completo(katamino):
    for i in range(len(katamino)):
        for j in range(len(katamino[0])):
            if katamino[i][j]==".":
                return False
    return True

def es_valido(katamino, pieza, fila, columna):
    for i in range(len(pieza)):
        for j in range(len(pieza[0])):
            if pieza[i][j] != '.':
                if fila + i >= L or columna + j >= A or katamino[fila + i][columna + j] != '.':
                    return False
    return True

def colocar_pieza(katamino, pieza, fila_inicio, columna_inicio):
    for i in range(len(pieza)):
        for j in range(len(pieza[0])):      
            if pieza[i][j]!=".":
                katamino[fila_inicio+ i][columna_inicio + j] = pieza[i][j] 

def copiarKatamino(katamino):
    return [fila[:] for fila in katamino]

def copiar(visitados):
    return visitados[:]
    
def DFS(katamino, matriz_piezas):
    if len(matriz_piezas)==0 and katamino_completo(katamino):
        return katamino
    pieza_actual = matriz_piezas[0]
    piezas_restantes = matriz_piezas[1:]
    for rotacion in todas_rotaciones(pieza_actual):
        for i in range(L):
            for j in range(A):
                if es_valido(katamino, rotacion, i, j):
                    nuevo_katamino = copiarKatamino(katamino)
                    colocar_pieza(nuevo_katamino, rotacion, i, j)
                    resultado = DFS(nuevo_katamino, piezas_restantes)
                    if resultado:
                        return resultado
    return None

def armarKatamino(katamino, piezas):
    resultado = DFS(katamino, piezas)
    return resultado if resultado else False

katamino_resuelto=armarKatamino(katamino, matriz_piezas)
def result(matriz_piezas,L,A):
    if katamino_resuelto:
        return print_b(katamino_resuelto)
    if contar_caracteres(matriz_piezas) != L*A:
        print_b(sadkataminito)
    else:
        print_b(sadkataminito)
result(matriz_piezas,L,A)
t1=time.time()
print(t1-t0)
