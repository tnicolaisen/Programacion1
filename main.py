"Implementar una matriz que almacene las calificaciones iniciales de los estudiantes en distintas materias. Este ejercicio ayudará a familiarizarse con el manejo de matrices en Python, que será fundamental para el desarrollo del proyecto."
import random
import funciones

n = int(input("¿Cuántas materias desea en su matriz?: "))
m = int(input("¿Cuántos estudiantes desea en su matriz?: "))
print()

# Defino una lista de materias y otra de estudiantes, genero la matriz de calificaciones, y la muestro debidamente (usando las funciones creadas en 'funciones.py')
materias = funciones.asignar_materias(n)
estudiantes = funciones.generar_legajos(m)
calificaciones = funciones.generar_calificaciones(materias, estudiantes)
print("\033[1mCalificaciones de los estudiantes:\033[0m") #Texto en negrita
funciones.imprimir_matriz(calificaciones)
# NOTA PARA EL PROFESOR: Ver línea 121 del archivo 'funciones.py'
print()

# Calculo el promedio de notas de los estudiantes utilizando la función correspondiente de "funciones.py"
promedioEstudiantes = funciones.calcular_promedio_estudiantes(calificaciones)
print("\033[1mPromedio de notas de los estudiantes:\033[0m")
funciones.imprimir_matriz(promedioEstudiantes)
print()

#Calculo el promedio de notas de las materias usando también la función correspondiente de "funciones.py"
promedioMaterias = funciones.calcular_promedio_materias(calificaciones)
print("\033[1mPromedio de notas de las materias:\033[0m")
funciones.imprimir_matriz(promedioMaterias)