import pygame 
import pygame.key

pygame.display.set_caption("Juego Pong")
ANCHO = 640
ALTO = 480

CBLANCO = (255, 255, 180)
AZUL = (10, 100, 100)
VERDE = (100, 250, 200)


ANCHO_PALETA = 10
ALTO_PALETA = 40
MARGEN_LATERAL = 30
MARGEN = 7

TAM_PELOTA = 10

class Jugador(pygame.Rect):
    ARRIBA = True
    ABAJO = False
    def __init__(self,pos_x, pos_y):
       self.rectangulo = pygame.Rect(pos_x, pos_y, ANCHO_PALETA, ALTO_PALETA)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, CBLANCO, self.rectangulo)

    def muevete(self, direccion):
        if direccion == self.ARRIBA:
            print("MUEVETE ARRIBA")
        else:
            print("MUEVETE HACIA ABAJO")


class Pelota(pygame.Rect):
    def __init__(self, x, y):
        self.rectangulo = pygame.Rect(x, y, TAM_PELOTA, TAM_PELOTA)
    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, (250, 250, 0), self.rectangulo)

class Pong:
    def __init__(self):
        print("Construyendo un objeto de la clase Pong")
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        
        
        pos_y = (ALTO-ALTO_PALETA)/2
        pos_x_2 = ANCHO-MARGEN_LATERAL-ANCHO_PALETA
    

        self.jugador1 = Jugador(MARGEN_LATERAL,pos_y)
        self.jugador2 = Jugador(pos_x_2, pos_y)

        pelota_x = (ANCHO-TAM_PELOTA)/2
        pelota_y = (ALTO-TAM_PELOTA)/2
        self.pelota = Pelota(pelota_x,pelota_y)

    def bucle_principal(self):

        salir = False
        while not salir:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    salir = True
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        salir = True
                    elif evento.key == pygame.K_a:
                        self.jugador1.muevete(Jugador.ARRIBA)
                    elif evento.key == pygame.K_z:
                        self.jugador1.muevete(Jugador.ABAJO)
                    elif evento.key == pygame.K_k:
                        self.jugador2.muevete(Jugador.ARRIBA)
                    elif evento.key == pygame.K_m:
                        self.jugador2.muevete(Jugador.ABAJO)
                #Dibujo rectángulo palas    
            pygame.draw.rect(self.pantalla,CBLANCO, self.jugador1)
            pygame.draw.rect(self.pantalla,CBLANCO, self.jugador2)
                ##fondo
            pygame.Surface.fill(self.pantalla, AZUL)
                ##LINEAS DE CAMPO
                            ##CENTRAL SUPERIOR
            pygame.draw.lines(self.pantalla, (VERDE), True, [(ANCHO,MARGEN_LATERAL),(-ANCHO,MARGEN_LATERAL)], 2)   
                            ##CENTRAL INFERIOR
            pygame.draw.lines(self.pantalla, (VERDE), True, [(ANCHO,ALTO-MARGEN_LATERAL),(-ANCHO,ALTO-MARGEN_LATERAL)], 2)  

            self.jugador1.pintame(self.pantalla)
            self.jugador2.pintame(self.pantalla)

            self.pinta_red()

            self.pelota.pintame(self.pantalla)
            pygame.display.flip()
             
    def pinta_red(self):
        tramo_pintado = 15
        tramo_vacio = 15
        ancho_red = 4
        pos_x= ANCHO/2+1 - ancho_red/2
        for y in range(MARGEN, ALTO-MARGEN, tramo_pintado+tramo_vacio):
                pygame.draw.line(self.pantalla, VERDE, (pos_x, y), (pos_x, y+tramo_pintado), ancho_red)


if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()


