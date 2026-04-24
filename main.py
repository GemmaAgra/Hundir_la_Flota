import numpy as np, utils, random, os, time

class JuegoHundirFlota:

    def __init__(self):
        self.tamano = 10
        self.config_barcos = [2, 2, 2, 3, 3, 4]
        # Tableros
        self.tablero_maquina = utils.crear_tablero(self.tamano)   # donde pinto los barcos 'O'
        self.tablero_jugador = utils.crear_tablero(self.tamano)   # donde pinto los barcos 'O'
        self.radar_jugador   = utils.crear_tablero(self.tamano)   # Visibilidad para el jugador (tablero donde dispara)
        self.radar_rival     = utils.crear_tablero(self.tamano)   # Visibilidad para el rival (tablero donde dispara)
      
    def preparar_juego(self):                                     # creo los barcos del jugador y máquina en el tablero
        self.tablero_maquina = utils.colocar_barcos_aleatorios(self.tablero_maquina, self.config_barcos)
        self.tablero_jugador = utils.colocar_barcos_aleatorios(self.tablero_jugador, self.config_barcos)
       
    def jugar(self):
        self.preparar_juego()
        print("\n ¡Bienvenido a Hundir la Flota!")

        # El Jugador dispare a tablero_maquina y F5 su radar_jugador
        # La Máquina dispare a tablero_jugador y F5 su radar_rival

        while "O" in self.tablero_maquina and "O" in self.tablero_jugador:   # "O"= barcos

            # pinto SIEMPRE los 2 tableros de los barcos y el de la maquina F5
            print("\n Barcos máquina: \n", self.tablero_maquina)
            print("\n Barcos jugador: \n", self.tablero_jugador)
            print("\n Turno máquina: \n", self.radar_rival)
            print("\n Turno jugador: \n", self.radar_jugador)

            # TURNO JUGADOR
            print("\n--- TU TURNO --- \n")         
            try:
                f = int(input(f"Fila (0-{self.tamano-1}): "))        #f = int(input("Fila (0-9): "))
                c = int(input(f"Columna (0-{self.tamano-1}): "))     #c = int(input("Col (0-9): "))
                rdo = utils.disparar((f, c), self.tablero_maquina)
                print(rdo)
                self.radar_jugador[f, c] = self.tablero_maquina[f, c] # F5 mi tablero radar para ver el rdo de mi disparo
            except Exception as e:  
                print("Error: Coordenada inválida, pierdes el turno") # controlar error si meto 10, 11.. fuera del tablero

            # TURNO MÁQUINA      
            # Antes de q la máquina dispare, VF si a la casilla elegida le quedan barcos 'O' para q no dispare si he ganado
            # pq lo compruebo abajo con el if
            if "O" in self.tablero_maquina:   
                print("\n--- TURNO DE LA MÁQUINA --- \n")
                ataco = False
                while not ataco:  
                    # La máquina genera 2 nºs aleatorios entre 0 y 9 (f_m = fila disparo y c_m = col disparo)
                    f_m, c_m = random.randint(0, self.tamano-1), random.randint(0, self.tamano-1)     
                    # la maquina VF q esa coord no haya disparado antes en la casilla. Solo dispara si tiene agua ' ' o 
                    # barco 'O'. Si hay 'X' o 'A' la máquina genera otra coord

                    # La máquina comprueba en su radar para no repetir disparo
                    if self.radar_rival[f_m, c_m] == "-":                      
                        rdo_m= utils.disparar((f_m, c_m), self.tablero_jugador)# Si la máquina acierta en mi tablero veo "X" y si falla "A"
                        print(f"La máquina disparó a ({f_m}, {c_m})\n {rdo_m}")
                        self.radar_rival[f_m, c_m] = self.tablero_jugador[f_m, c_m]    # F5 su tablero radar con el rdo
                        ataco = True  # sale bucle pq el disparo es VL              

                print("\n Limpiando pantalla en 5 seg...")         
                time.sleep(5)                                      # Pausa de 5" para ver el disparo de la máquina              
                os.system('cls' if os.name == 'nt' else 'clear')   # limpio pantalla

        if "O" not in self.tablero_maquina:
            print("¡HAS GANADO! Todos los barcos hundidos !!!!!! \n")   
        elif "O" not in self.tablero_jugador:
            print("OHHH... La máquina ha ganado... \n")

if __name__ == "__main__":          # ejecuta el if si el archivo main se abre (ejecuto en terminal "python main.py")
    partida = JuegoHundirFlota()    # arrancar prog. creando un objeto de mi clase
    partida.jugar()                 # empiezo el juego


# NOTA: Si importo la clase JuegoHundirFlota desde otro archivo, el juego no se lanzará solo, hay q ejecutarlo con el main.py       