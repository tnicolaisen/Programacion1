import random
# #Funciones solicitadas:    
# FALTAN HACER LAS FUNCIONES DE DEBAJO
'''
Descripción: Calcula el promedio de notas de cada estudiante en una matriz
Retorno: Devuelve una matriz con encabezado, correspondiente a las notas promedio de todas las materias entre todos los alumnos.
Pre: Se solicita el promedio de notas por alumno
Pos: Se entrega una matriz con el promedio de notas por alumno (identificados con el N° de legajo), y el promedio de todas las notas.
'''
def calcular_promedio_estudiantes(matriz):
    # Genero el encabezado de la matriz
    promedios = [["Legajo N°", "Promedio"]]
    #Empezando siempre a partir de la columna y fila 1 (para no mezclar los encabezados y los legajos con la sumatoria), tomo el número de legajo del alumno, y voy calculando la sumatoria del promedio. Luego lo dividio por la cantidad de estudiantes (que es matriz[i] - 1 porque sino contendría también el N° de legajo comoe estudiante).
    for i in range(1, len(matriz)):
        legajo = matriz[i][0]
        sumatoria = 0
        for j in range(1, len(matriz[i])):
            sumatoria += matriz[i][j]
        promedio = sumatoria / len(matriz[i])-1
        promedio = round(promedio, 1)
        promedios.append([legajo,promedio])
    return promedios
    
'''
Descripción: Calcula el promedio de notas de cada materia en una matriz
Retorno: Devuelve una matriz con encabezado, correspondiente a las notas promedio de cada materia entre todos los alumnos.
Pre: Se solicita el promedio de notas por materia
Pos: Se entrega una matriz con el promedio de notas por materia entre todos los alumnos cursantes.
'''
def calcular_promedio_materias(matriz):
    promedios = [["Materia", "Promedio"]]
    for i in range(1,len(matriz)):
        materia = matriz[0][i]
        sumatoria = 0
        for j in range(1, len(matriz)):
            sumatoria += matriz[j][i]
        promedio = sumatoria / (len(matriz) - 1)
        promedio = round(promedio,1)
        promedios.append([materia,promedio])
    return promedios
    
#FUNCIONES PROPIAS:
'''
Descripción: Genera una lista de las materias que se asignan a la matriz (máximo 10 materias)
Retorno: Lista con las materias asignadas (list[])
Pre: Se solicita una cantidad de materias distintas.
Pos: Se devuelve una lista con la cantidad de materias distintas.
'''
def asignar_materias(cantidad_materias):
    #Verifico que no se pidan más materias de las posibles (ni menos).
    while cantidad_materias <1 or cantidad_materias > 10:
        cantidad_materias = int(input("Por favor. Ingrese una cantidad de materias válidas (mínimo 1, máximo 10): "))
    
    #Establezco la cantidad de materias psobiles
    materias_posibles = ["Matemática", "Física", "Química", "Historia", "Lengua", "Geografía", "Biología", "Filosofía", "Ed. Física", "Arte"]
    materias_asignadas = []
    
    #Genero una lista con las materias posibles, verificando que no se repitan.
    while len(materias_asignadas) < cantidad_materias:
        materia = random.choice(materias_posibles)
        if len(materias_asignadas) == 0:
            materias_asignadas.append(materia)
        else:
            repetida = False
            for i in range(len(materias_asignadas)):
                if materias_asignadas[i] == materia:
                    repetida = True
            if repetida == False:
                materias_asignadas.append(materia)
    return materias_asignadas


'''
Descripción: Genera una cantidad de legajos indicada (números enteros de cuatro cifras).
Retorno: Devuelve una lista con la cantidad de legajos solicitadas (números enteros de cuatro cifras).
Pre: Se solicita una cantidad de legajos determinada.
Pos: Se retorna una lista con la cantidad de legajos determinada (distintos entre sí).
'''
def generar_legajos(cantidad_legajos):
    legajos = []
    while len(legajos) < cantidad_legajos:
        # Verifica que los legajos no se repitan
        legajo = random.randint(1000,9999)
        if len(legajos) == 0:
            legajos.append(legajo)
        else:
            repetida = False
            for i in range(len(legajos)):
                if legajos[i] == legajo:
                    repetida == True
            if repetida == False:
                legajos.append(legajo)
    return legajos

'''
Descripción: Genera una matriz en base a una lista de materias y una lista de estudiantes dada.
Retorno: Devuelve una matriz ordenada, con la primer fila conteniendo "Legajo N°" más los nombres de las materias, y las filas posteriores, el legajo del alumno seguido a las notas correspondientes a cada materia.
Pre: Existen sólo las listas de los legajos de los estudiantes y las materias.
Pos: Genera una matriz con la cantidad de alumnos y materias ingresada, de manera ordenada, mostrando la nota de cada alumno en cada materia correspondiente (generada automáticamente).
'''
def generar_calificaciones(materias, estudiantes):
    #Reacomodo la primera fila para que quede la palabra "Estudiantes" delante
    materias.append("Legajo N°")
    a = materias[0]
    b = materias[len(materias) - 1]
    materias[0] = b
    materias[len(materias) - 1] = a
    
    #Genero la matriz a retornar con la primer fila
    calificaciones = [materias]
    
    #Añado alumno por alumno y le voy generando sus notas en base a la cantidad de materias
    for j in range(len(estudiantes)):
        calificaciones.append([estudiantes[j], *[random.randint(1,10) for i in range(len(materias)-1)]]) # NOTA: Preguntar cómo funciona el "*" acá. Recomendado por ChatGPT.
    return calificaciones

'''
Descripción: Muestra la tablilla otorgada de manera bien ordenada y centrada
Retorno: Nulo
'''
# NOTA PARA EL PROFESOR: Cambié un poco la función "mostrar_matriz" solicitada por la función "imprimir_matriz" para así podía utilizarla no sólamente para la matriz de calificaciones. Es por ello que tampoco tiene los parámetros solicitados, a excepción de la matriz objetivo.
def imprimir_matriz(matriz):
    #Establezco un ancho de columna (en la que entra cualquiera de las materias) para que quede prolija la tabla al imprimirse
    ancho = 12
    for fila in (matriz):
        for elemento in fila:
            print(f"{elemento:^{ancho}}", end = "|")
        print()