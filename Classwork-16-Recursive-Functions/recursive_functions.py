# recursive_functions.py

def recursiva(n):
    try:
        # Manejo de errores: tipos de dato inválidos y números negativos
        if not isinstance(n, int):
            raise TypeError("El valor debe ser un número entero.")
        if n < 0:
            raise ValueError("El valor no puede ser negativo.")
            
        # CASO BASE[cite: 3]
        if n == 0:
            return "Done!"
        else:
            print(n)
            return recursiva(n - 1)
    except (TypeError, ValueError) as e:
        return f"Error en recursiva: {e}"


def fibonacci(n):
    try:
        # Manejo de errores: números negativos y tipos de dato inválidos[cite: 3]
        if not isinstance(n, int):
            raise TypeError("El valor debe ser un número entero.")
        if n < 0:
            raise ValueError("El valor no puede ser negativo.")
            
        if (n == 0) or (n == 1):
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    except (TypeError, ValueError) as e:
        return f"Error en fibonacci: {e}"


def factorial(n):
    try:
        # Manejo de errores: decimales y números negativos[cite: 3]
        if not isinstance(n, int):
            raise TypeError("El valor debe ser un número entero.")
        if n < 0:
            raise ValueError("El valor no puede ser negativo.")
            
        if (n == 0) or (n == 1):
            return 1
        else:
            return factorial(n - 1) * n
    except (TypeError, ValueError) as e:
        return f"Error en factorial: {e}"


def multiplicacion_recursiva(n, m):
    try:
        # Manejo de errores: el multiplicador no puede ser negativo[cite: 3]
        if not isinstance(m, int):
            raise TypeError("El multiplicador (m) debe ser un entero.")
        if m < 0:
            raise ValueError("El multiplicador (m) no puede ser negativo.")
            
        if m == 0:
            return 0
        else:
            return multiplicacion_recursiva(n, m - 1) + n
    except (TypeError, ValueError) as e:
        return f"Error en multiplicacion_recursiva: {e}"


def division_entera_recursiva(dividendo, divisor):
    try:
        # Manejo de errores: división entre cero y soporte para negativos[cite: 3]
        if divisor == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        if not isinstance(dividendo, int) or not isinstance(divisor, int):
            raise TypeError("Ambos valores deben ser enteros.")
        if dividendo < 0 or divisor < 0:
            raise ValueError("Esta versión básica no soporta números negativos.")

        if dividendo - divisor < 0:
            return 0
        else:
            return division_entera_recursiva(dividendo - divisor, divisor) + 1
    except (ZeroDivisionError, TypeError, ValueError) as e:
        return f"Error en division_entera_recursiva: {e}"


def potencia_recursiva(base, exponente):
    try:
        # Manejo de errores: exponentes negativos (espera 0 o positivos)[cite: 3]
        if not isinstance(exponente, int):
            raise TypeError("El exponente debe ser un número entero.")
        if exponente < 0:
            raise ValueError("El exponente no puede ser negativo para esta función.")
            
        if exponente == 0:
            return 1
        else:
            return potencia_recursiva(base, exponente - 1) * base
    except (TypeError, ValueError) as e:
        return f"Error en potencia_recursiva: {e}"


def serie_collatz(n):
    try:
        # Manejo de errores: n debe ser mayor a 0 y ser entero[cite: 3]
        if not isinstance(n, int):
            raise TypeError("El valor debe ser un número entero.")
        if n <= 0:
            raise ValueError("El valor debe ser estrictamente mayor a 0.")
            
        if n == 1:
            print("END!")
            return 0
        else:
            if n % 2 == 0:
                print(n // 2)
                return serie_collatz(n // 2)
            else:
                print(3 * n + 1)
                return serie_collatz(3 * n + 1)
    except (TypeError, ValueError) as e:
        return f"Error en serie_collatz: {e}"


def aplanar_json(diccionario, clave_padre='', separador='.'):
    elementos = []
    try:
        # Manejo de errores: si el input principal es una lista, .items() lanzará un AttributeError[cite: 3]
        for key, value in diccionario.items():
            nueva_llave = f"{clave_padre}{separador}{key}" if clave_padre else key
            
            if isinstance(value, dict):
                # Desempaqueta diccionarios anidados[cite: 3]
                resultado_anidado = aplanar_json(value, nueva_llave, separador)
                if isinstance(resultado_anidado, dict):
                    elementos.extend(resultado_anidado.items())
                    
            elif isinstance(value, list):
                # Manejo de error: procesa las listas para que no queden como valores planos (ej. "tags": [1, 2, 3])[cite: 3]
                for i, item in enumerate(value):
                    llave_lista = f"{nueva_llave}{separador}{i}"
                    if isinstance(item, dict):
                        res_lista = aplanar_json(item, llave_lista, separador)
                        if isinstance(res_lista, dict):
                            elementos.extend(res_lista.items())
                    else:
                        elementos.append((llave_lista, item))
            else:
                elementos.append((nueva_llave, value))
                
        return dict(elementos)
    
    except AttributeError:
        # Captura específicamente cuando se intenta usar .items() en una lista[cite: 3]
        return "Error: El parámetro ingresado debe ser un diccionario, no una lista u otro tipo de dato."
    except Exception as e:
        return f"Error inesperado en aplanar_json: {e}"


# ==========================================
# SECCIÓN DE PRUEBAS
# ==========================================
if __name__ == "__main__":
    # Datos extraídos del archivo JSON de prueba[cite: 4]
    json_prueba = {
        "a": 1,
        "b": {
            "c": 2,
            "d": {
                "e": 3
            }
        },
        "f": [1, 2, 3],
        "g": [
            {"h": 4},
            {"i": 5}
        ],
        "j": {
            "k": [6, 7, {"l": 8}]
        },
        "m": None,
        "n": True,
        "o": []
    }
    
    print("--- PRUEBA APLANAR JSON ---")
    resultado = aplanar_json(json_prueba)
    import pprint
    pprint.pprint(resultado)
    
    print("\n--- PRUEBA DE ERRORES (no debe crashear) ---")
    print("recursiva(-3):", recursiva(-3)) # Falla controlada[cite: 3]
    print("aplanar_json(['a', 'b', 'c']):", aplanar_json(["a", "b", "c"])) # Falla controlada[cite: 3]
    print("division_entera_recursiva(10, 0):", division_entera_recursiva(10, 0)) # Falla controlada[cite: 3]
