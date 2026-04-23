import numpy as np, utils, random, os

class JuegoHundirFlota:

    def __init__(self):
        self.tamano = 10
        self.config_barcos = [2, 2, 2, 3, 3, 4]
        # Tableros
        self.tablero_maquina = utils.crear_tablero(self.tamano)   # donde pinto los barcos
        self.tablero_jugador = utils.crear_tablero(self.tamano)   # donde pinto los barcos
        self.radar_jugador   = utils.crear_tablero(self.tamano)   # Visibilidad para el jugador (donde dispara)
        self.radar_rival     = utils.crear_tablero(self.tamano)   # Visibilidad para el rival (donde dispara)

    def preparar_juego(self):                                     # pinto los barcos del jugador y máquina en el tablero
        self.tablero_maquina = utils.colocar_barcos_aleatorios(self.tablero_maquina, self.config_barcos)
        self.tablero_jugador = utils.colocar_barcos_aleatorios(self.tablero_jugador, self.config_barcos)
        print("\n Barcos máquina: \n", self.tablero_maquina)
        print("\n Barcos jugador: \n", self.tablero_jugador)


    def jugar(self):
        self.preparar_juego()
        print("\n ¡Bienvenido a Hundir la Flota!")
        
        while "O" in self.tablero_maquina and "O" in self.tablero_jugador:   # "O"= barcos

            os.system('cls' if os.name == 'nt' else 'clear')       # limpio pantalla

             # pinto SIEMPRE los 2 tableros de los barcos y el de la maquina F5
            print("\n Barcos máquina: \n", self.tablero_maquina)
            print("\n Barcos jugador: \n", self.tablero_jugador)
            print("\n Barcos máquina: \n", self.radar_rival)

            # TURNO JUGADOR
            print("\n--- TU TURNO --- \n", self.radar_jugador)         
            try:
                f = int(input("Fila (0-4): "))
                c = int(input("Columna (0-4): "))
                rdo = utils.disparar((f, c), self.tablero_maquina)
                print(rdo)
                self.radar_jugador[f, c] = self.tablero_maquina[f, c]   # F5 mi tablero para ver el rdo de mi disparo
            except:  
                print("Error: Coordenada inválida, pierdes el turno") # controlar error si meto 10, 11.. fuera del tablero

            # TURNO MÁQUINA      
            # Antes de q la máquina dispare, VF si a la casilla elegida le quedan barcos 'O'
            # para evitar q dispare si yo acabo de hundir su último barco en el turno ant.

            if "O" in self.tablero_maquina:
                ataco = False
                while not ataco:  # La máquina se queda "pensando" hasta q encuentra una coord q no haya disparado antes
                    # La máquina genera 2 nºs aleatorios entre 0 y 4 (f_m =la fila del disparoy y c_m es la col)
                    f_m, c_m = random.randint(0, 4), random.randint(0, 4)                    
                    # VF q no haya disparado antes en esa casilla, Solo dispara si tiene agua ' ' o un barco 'O'                    
                    # Si hay una 'X' o una 'A', la máquina genera otra coord.
                    if self.tablero_jugador[f_m, c_m] in ["-", "O"]:
                        utils.disparar((f_m, c_m), self.tablero_jugador)  # Si la máquina acierta, en mi tablero veo una "X" y si falla una "A"
                        print(f"\nLa máquina disparó a ({f_m}, {c_m})")
                        print("\n--- TURNO MAQUINA --- \n", self.radar_rival)                        
                        rdo_m = utils.disparar((f_m, c_m), self.tablero_maquina)
                        print(rdo_m)
                        self.radar_rival[f_m, c_m] = self.tablero_maquina[f_m, c_m]
                        ataco = True # sale bucle pq el disparo es VL

        if "O" not in self.tablero_maquina:
            print("¡HAS GANADO! barco hundido! ")   # si hundes un barco considero q has ganado
        else: print("La máquina ha ganado...")

if __name__ == "__main__":          # ejecuta el if si el archivo main se abre (ejecuto en terminal "python main.py")
    partida = JuegoHundirFlota()    # arrancar prog. creando un objeto de mi clase
    partida.jugar()                 # empiezo el juego


# Si importo la clase JuegoHundirFlota desde otro archivo, el juego no se lanzará solo, hay q ejecutarlo con el main.py
