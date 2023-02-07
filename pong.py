import pygame 
import pygame.key

pygame.display.set_caption("Juego Pong")
ANCHO = 640
ALTO = 480

CBLANCO = (255, 255, 180)
#### Ejercicio 2, añadir color
GRAY = (41, 81, 41)
#####
ANCHO_PALETA = 10
ALTO_PALETA = 40
MARGEN_LATERAL = 40

TAM_PELOTA = 5

class Jugador(pygame.Rect):
    def __init__(self,pos_x, pos_y):
       self.rectangulo = pygame.Rect(pos_x, pos_y, ANCHO_PALETA, ALTO_PALETA)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, CBLANCO, self.rectangulo)

class Pelota(pygame.Rect):
    def __init__(self, x, y):
        self.rectangulo = pygame.Rect(x, y, TAM_PELOTA, TAM_PELOTA)
    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, CBLANCO, self.rectangulo)

class Pong:
    

    def __init__(self):
        print("Construyendo un objeto de la clase Pong")
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
    ################## AÑADIMOS EL COLOR TRAS DEFINIR EL TAMAÑO
        pygame.Surface.fill(self.pantalla, GRAY)
    ##################
        
        pos_y = (ALTO-ALTO_PALETA)/2
        pos_x_2 = ANCHO-MARGEN_LATERAL-ANCHO_PALETA

       
    ##  PARA HACER LINEAS CONTIGUAS
 
      ##ESTA ESTA BIEN##  pygame.draw.aaline(self.pantalla, (0,0,255), [(ANCHO/2)-1, 0], [(ANCHO/2)-1, ALTO])
    ##    pygame.draw.lines(self.pantalla, (0.200,0), True, [(ANCHO/2)-1, 0], [(ANCHO/2)-1, ALTO])
    ##linea de separación
        pygame.draw.lines(self.pantalla, (220,0,0), True, [((ANCHO/2)-1,ALTO), ((ANCHO/2)-1,0)], 4)
    ##LINEAS DE CAMPO
            ##CENTRAL SUPERIOR
        pygame.draw.lines(self.pantalla, (180,0,0), True, [(ANCHO,40),(-ANCHO,40)], 2)   
            ##CENTRAL INFERIOR
        pygame.draw.lines(self.pantalla, (180,0,0), True, [(ANCHO,ALTO-40),(-ANCHO,ALTO-40)], 2)  

       # pygame.draw.lines(self.pantalla, (180,0,0), True, [(ANCHO,20),(-ANCHO,40)], 2)  


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


                    
                
            


        
                #Dibujo rectángulo
            pygame.draw.rect(self.pantalla,CBLANCO, self.jugador1)
            pygame.draw.rect(self.pantalla,CBLANCO, self.jugador2)
            
            self.jugador1.pintame(self.pantalla)
            self.jugador2.pintame(self.pantalla)
            self.pelota.pintame(self.pantalla)
            pygame.display.flip()


if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()


