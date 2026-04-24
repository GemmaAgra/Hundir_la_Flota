import numpy as np, random

def crear_tablero(tamano=10):
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


def crear_barco(eslora, tamano_tablero=10):      # crea un barco dentro del tablero   
    while True:                                  # bucle infinito de intentos hasta q el barco encuentre un lugar VL 
        orientacion = random.choice(['H', 'V'])           # genera orient. y coords aleatorias. de 0 a 9 (tamaño 10)
        fila = random.randint(0, tamano_tablero - 1)  
        col  = random.randint(0, tamano_tablero - 1)
        
        casillas = []
        for i in range(eslora):
            if orientacion == 'H': casillas.append((fila, col + i))
            else:                  casillas.append((fila + i, col))
        
        # VL q el barco no se salga del tablero, sino volvería a intentarlo hasta q el diseño sea VL
        if all(0 <= r < tamano_tablero and 0 <= c < tamano_tablero for r, c in casillas):
            return casillas  
        """
        for r, c in casillas: Recorre cada coord de la lista casillas del barco. r =fila (row) y c = col
        0 <= r < tamano_tablero: Comprueba q la fila no sea negativa y q sea < al tamaño del tablero 
        (si el tablero es de 10, la fila máx es 9)
        0 <= c < tamano_tablero: Hace lo mismo para la col
        all(...): función de Python q devuelve True si todas las condiciones del bucle son true 
                  Si 1 casilla se sale (por ej. fila 10 en un tablero de 10), all devuelve False
        """


def colocar_barcos_aleatorios(tablero, barcos_config):   
    tablero_temp = tablero.copy()
    for eslora in barcos_config:    # Recorre lista de barcos a colocar
        colocado = False
        while not colocado:                  
            propuestaCasillas = crear_barco(eslora)     # genera coord aleatorias y VF q el barco no se sale del tablero        
            if all(tablero_temp[c] == "-" for c in propuestaCasillas): # VL q no haya otro barco superpuesto en c (f-col)
                colocar_barco(propuestaCasillas, tablero_temp)  # Si hueco libre pongo "O" y sale del while para pasar al
                colocado = True                     #  sgte barco. Si hay otro barco (O) rechaza la propuesta y pide otra
    return tablero_temp           
""" 
all(...): es el "detector de colisiones", VF q todas las casillas q necesita el nuevo barco tengan agua (-)
Si 1 tiene una "O" hay colisión y el if falla


for c in propuestaCasillas: Recorre 1 a 1 las coords de c (fila y col) propuestas
tablero_temp[c] == "-":     Mira en el tablero q hay en la coord c y comprueba si es agua ("-")
all(...):                   devuelve True si todas las casillas de la lista cumplen la condición
                            True = agua y se coloca el barco con "O". False= si 1 casilla ya ocupada por otro barco "O", 
                            el programa rechaza la propuesta y busca otra ubicación aleatoria


característica	crear_barco	                                    colocar_barcos_aleatorios
Misión	        Crear coords de un barco                    	Gestionar la colocación de toda la flota
VL      	    Q no se salga del tablero                   	Q no choque con otros barcos
Rdo     	    Devuelve 1 lista de tuplas [(0,1), (0,2)]   	Devuelve el tablero terminado

"""