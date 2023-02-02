import pygame 

ANCHO = 640
ALTO = 480

CBLANCO = (255, 255, 180)

ANCHO_PALETA = 10
ALTO_PALETA = 40
MARGEN_LATERAL = 40


class Jugador(pygame.Rect):
    def __init__(self,pos_x, pos_y):
       self.rectangulo = pygame.Rect(pos_x, pos_y, ANCHO_PALETA, ALTO_PALETA)



class Pong:

    def __init__(self):
        print("Construyendo un objeto de la clase Pong")
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pos_y = (ALTO-ALTO_PALETA)/2
        pos_x_2 = ANCHO-MARGEN_LATERAL-ANCHO_PALETA
        self.jugador1 = Jugador(MARGEN_LATERAL,y)
        self.jugador2 = Jugador(pos_x_2, pos_y)

    def bucle_principal(self):
        salir = False
        while not salir:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    salir = True
                #Dibujo rectángulo
            pygame.draw.rect(self.pantalla,CBLANCO, self.jugador1)
            pygame.draw.rect(self.pantalla,CBLANCO, self.jugador2)
            pygame.display.flip()


if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()


