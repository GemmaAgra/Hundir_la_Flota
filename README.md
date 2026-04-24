# Juego Hundir_la_Flota
Proyecto de clase con python v.3.11 y librerias: numpy
Documentación Técnica: Juego Hundir la Flota



1. Descripción General
Este programa es una simulación del clásico juego Hundir la Flota, desarrollado en Python usando la librería NumPy para la gestión de matrices. El juego permite a un usuario enfrentarse contra la CPU en un tablero de 10x10, donde el objetivo es hundir los barcos del oponente antes de perder los propios. 
2. Arquitectura del Proyecto
El código se divide en dos bloques:
    • Lógica de Datos (utils): Funciones para la creación, validación y manipulación de tableros y barcos.
    • Controlador del Juego (main): Clase que gestiona el estado de la partida, los turnos y la interacción con el usuario. Se ejecutará este fichero para iniciar el juego.
      
3. Especificaciones de los Componentes
Clase JuegoHundirFlota (main.py):  Es el motor principal del programa. Desde aquí llama a las funciones de utils.py.
    • __init__: Inicializa las configuraciones (tablero 10x10 y flota de barcos: esloras 2, 2, 2, 3, 3, 4). Crea 4 tableros: 2 para las posiciones reales de barcos y 2 "radares" para visualizar los disparos efectuados.
    • preparar_juego: Orquestador q invoca las funciones de utils para posicionar aleatoriamente las flotas en ambos tableros.
    • jugar: Contiene el bucle principal (while). Gestiona:
        ◦ Turno Jugador: Entrada por teclado con manejo de excepciones para coordenadas inválidas.
        ◦ Turno Máquina: Lógica de disparo aleatorio con validación para no repetir coordenadas ya atacadas.
Funciones (utils.py)
    • crear_tablero(tamano): Genera una matriz de NumPy llena de caracteres "-".
    • colocar_barco(barco,tablero): Pinta en el tablero los barcos “O”.
    • crear_barco(eslora, tamano_tablero): Genera una lista de coordenadas aleatorias. Incluye una validación geográfica mediante all() para asegurar q ninguna parte del barco exceda los límites del índice (0-9).
    • colocar_barcos_aleatorios(tablero, barcos_config): Recorre la configuración de la flota. Valida la colisión, comprobando q todas las celdas propuestas estén vacías ("-") antes de llamar a colocar_barco.
    • disparar(casilla, tablero): Compara la coordenada recibida con el contenido del tablero: O (barco), X (Tocado), -, A (Agua).
          

4. Simbología del Tablero
Símbolo	Significado
-	Agua / Casilla no explorada
O	Posición de un barco (invisible para el oponente)
X	Impacto (Tocado)
A	Disparo fallido (Agua)

5. Requisitos del Sistema
    • Lenguaje: Python 3.11
    • Librerías: numpy (instalar mediante pip install numpy)
    • IDE: Visual Studio
