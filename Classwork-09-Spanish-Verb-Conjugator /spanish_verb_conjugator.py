# INPUT
verbo = input("Ingrese verbo: ")

# PROCESS
pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']
terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

# Obtener la raíz (todo menos las últimas 2 letras) y la terminación (últimas 2 letras)
raiz = verbo[:-2]
terminacion = verbo[-2:]

# Buscar la lista de terminaciones correspondiente en el diccionario
terminaciones_correspondientes = terminaciones[terminacion]

# OUTPUT
# Ciclo sobre los pronombres usando el mismo índice para ambas listas
for i in range(len(pronombres)):
    print(pronombres[i] + " " + raiz + terminaciones_correspondientes[i])
