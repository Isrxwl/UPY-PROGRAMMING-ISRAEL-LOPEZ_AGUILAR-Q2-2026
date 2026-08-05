import stddraw
import color

# ==========================================
# 1. BUBBLE SORT (Estándar)
# ==========================================
def bubble_sort(arr):
    # INPUT: arr (Una lista de números desordenada)
    n = len(arr)
    
    # PROCESS: Compara elementos adyacentes y los intercambia si están en el orden incorrecto
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                
    # OUTPUT: La lista ordenada
    return arr

# ==========================================
# 2. SELECTION SORT (Estándar)
# ==========================================
def selection_sort(arr):
    # INPUT: arr (Una lista de números desordenada)
    n = len(arr)
    
    # PROCESS: Encuentra el elemento mínimo de la parte no ordenada y lo pone al principio
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
        
    # OUTPUT: La lista ordenada
    return arr

# ==========================================
# 3. INSERTION SORT (Estándar)
# ==========================================
def insertion_sort(arr):
    # INPUT: arr (Una lista de números desordenada)
    n = len(arr)
    
    # PROCESS: Toma un elemento y lo inserta en su posición correcta en la parte ya ordenada
    for i in range(1, n):
        current_value = arr[i]
        pos = i
        
        while pos > 0 and arr[pos - 1] > current_value:
            arr[pos] = arr[pos - 1]
            pos -= 1
            
        arr[pos] = current_value
        
    # OUTPUT: La lista ordenada
    return arr

# ==========================================
# 4. DRAW BARS (Función de visualización)
# ==========================================
def draw_bars(arr):
    # INPUT: arr (La lista en su estado actual)
    
    # PROCESS: Limpia la pantalla y dibuja un rectángulo por cada elemento del arreglo
    stddraw.clear(stddraw.WHITE)
    n = len(arr)
    
    for i in range(n):
        # stddraw.filledRectangle(x, y, half_width, half_height)
        x_center = i + 0.5
        y_center = arr[i] / 2.0
        half_width = 0.4
        half_height = arr[i] / 2.0
        
        stddraw.setPenColor(stddraw.BLUE)
        stddraw.filledRectangle(x_center, y_center, half_width, half_height)
        
    # OUTPUT: Muestra la imagen en pantalla por una fracción de segundo (50 milisegundos)
    stddraw.show(50)

# ==========================================
# 5. BUBBLE SORT ANIMATED
# ==========================================
def bubble_sort_animated(arr):
    # INPUT: arr (Una lista de números desordenada)
    n = len(arr)
    
    # PROCESS: Ejecuta Bubble Sort y actualiza el dibujo en cada intercambio
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                draw_bars(arr) # <-- Aquí ocurre la animación
                
    # OUTPUT: La lista ordenada visualmente
    return arr

# ==========================================
# 6. SELECTION SORT ANIMATED
# ==========================================
def selection_sort_animated(arr):
    # INPUT: arr (Una lista de números desordenada)
    n = len(arr)
    
    # PROCESS: Ejecuta Selection Sort y actualiza el dibujo en cada intercambio
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
        draw_bars(arr) # <-- Aquí ocurre la animación
        
    # OUTPUT: La lista ordenada visualmente
    return arr

# ==========================================
# 7. INSERTION SORT ANIMATED
# ==========================================
def insertion_sort_animated(arr):
    # INPUT: arr (Una lista de números desordenada)
    n = len(arr)
    
    # PROCESS: Ejecuta Insertion Sort y actualiza el dibujo en cada inserción
    for i in range(1, n):
        current_value = arr[i]
        pos = i
        
        while pos > 0 and arr[pos - 1] > current_value:
            arr[pos] = arr[pos - 1]
            pos -= 1
            draw_bars(arr) # <-- Animación en el movimiento
            
        arr[pos] = current_value
        draw_bars(arr) # <-- Animación al colocar el elemento final
        
    # OUTPUT: La lista ordenada visualmente
    return arr

# ==========================================
# CÓDIGO DE PRUEBA PARA VER LA ANIMACIÓN
# ==========================================
if __name__ == '__main__':
    # 1. Creamos una lista desordenada de prueba
    test_array = [8, 3, 5, 2, 9, 1, 6, 4, 7]
    
    # 2. Configuramos la escala de la ventana para que las barras quepan bien
    stddraw.setXscale(0, len(test_array))
    stddraw.setYscale(0, max(test_array) + 1)
    
    # 3. Llamamos a UNA de las funciones animadas (puedes cambiarla para probar las otras)
    bubble_sort_animated(test_array)
    
    # 4. Mantenemos la ventana abierta unos segundos al terminar
    stddraw.show(3000)
