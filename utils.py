import numpy as np, random

def crear_tablero(tamano=5):
    return np.full((tamano, tamano), "-")

def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero

def disparar(casilla, tablero):
    if tablero[casilla] == "O":
        tablero[casilla] = "X"
        return "¡Tocado!"
    elif tablero[casilla] =="-":
        tablero[casilla] = "A"        
        return "Agua"
    return "Ya disparaste aquí"

def crear_barco(eslora, tamano_tablero=5):    # diseña un barco q exista dentro de los límites del mapa
    while True:
        orientacion = random.choice(['H', 'V'])
        fila = random.randint(0, tamano_tablero - 1)
        col  = random.randint(0, tamano_tablero - 1)
        
        casillas = []
        for i in range(eslora):
            if orientacion == 'H': casillas.append((fila, col + i))
            else:                  casillas.append((fila + i, col))
        
        # VL q no se salga del tablero el barco, volvería a intentarlo hasta q el diseño sea VL
        if all(0 <= r < tamano_tablero and 0 <= c < tamano_tablero for r, c in casillas):
            return casillas        
        """
        for r, c in casillas: Recorre cada coord de la lista de casillas del barco. r =fila (row) y c = col.
        0 <= r < tamano_tablero: Comprueba que la fila no sea negativa y que no sea >= al tamaño del tablero 
        (si el tablero es de 5, la fila máx es 4).
        0 <= c < tamano_tablero: Hace lo mismo para la columna.
        all(...): función de Python q devuelve True solo si todas las condiciones dentro del bucle son true. 
                  Si una sola casilla se sale (por ej, fila 5 en un tablero de 5), all devuelve False.
        """

def colocar_barcos_aleatorios(tablero, barcos_config):   # gestiona toda la flota usando crear_barco, propuesta barco y mira tablero
    tablero_temp = tablero.copy()
    for eslora in barcos_config:    # Recorre lista de barcos ptes
        colocado = False
        while not colocado:                  
            propuesta = crear_barco(eslora)          # genera coord aleatorias (VF que el barco no se sale del tablero)        
            if all(tablero_temp[c] == "-" for c in propuesta):   # VL q no haya otro barco superpuesto. c coord (fila, col)
                colocar_barco(propuesta, tablero_temp)      # Si hueco libre pongo "O" y sale del while para pasar al
                colocado = True                             #  sgte barco. Si hay otro barco (O) rechaza la propuesta
    return tablero_temp                                     # y pide otra

"""
bucle infinito de intentos. para cuando el barco encuentre un lugar VL
 
 
 
all(...): Comprueba q todas las casillas q necesita el nuevo barco tengan agua (_), Si 1 tiene una "O" hay colisión 
y el if falla


característica	crear_barco	                       colocar_barcos_aleatorios
Misión	     Crear coordenadas de un barco.     	Gestionar la colocación de toda la flota.
Validación	Que no se salga del tablero (Bordes).    	Que no choque con otros barcos (Colisiones).
Rdo     	Devuelve una lista de tuplas [(0,1), (0,2)].	Devuelve el tablero de NumPy terminado.

"""