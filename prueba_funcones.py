import random
import funciones

materias = funciones.asignar_materias(int(input("¿Cuántas materias quieres asignar?: ")))
print(materias)

legajos = funciones.generar_legajos(int(input("¿Cuántos legajos quiere generar?: ")))
print(legajos)