import pygame
from random import randint

pygame.display.set_caption("Gokupong")

ANCHO = 640
ALTO = 480
FPS = 60

CBLANCO = (255, 255, 180)
AZUL = (10, 100, 100)
VERDE = (100, 250, 200)


ANCHO_PALETA = 10
ALTO_PALETA = 40
MARGEN_LATERAL = 30
MARGEN = 7
VEL_JUGADOR = 5

TAM_PELOTA = 10
VEL_MAX_PELOTA = 5

PUNTOS_PARTIDA = 3


class Jugador(pygame.Rect):
    ARRIBA = True
    ABAJO = False
    VELOCIDAD = VEL_JUGADOR

    def __init__(self, pos_x, pos_y):
        super(Jugador, self).__init__(pos_x, pos_y, ANCHO_PALETA, ALTO_PALETA)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, CBLANCO, self)

    def muevete(self, direccion):
        if direccion == self.ARRIBA:
            self.y = self.y - self.VELOCIDAD
            if self.y < 0:
                self.y = 0

        else:
            self.y = self.y + self.VELOCIDAD
            if self.y > ALTO-ALTO_PALETA:
                self.y = ALTO-ALTO_PALETA


class Pelota(pygame.Rect):

    # velocidad_x = randint(-5, 5)
    # velocidad_y = randint(-5, 5)

    def __init__(self, x, y):
        super(Pelota, self).__init__(x, y, TAM_PELOTA, TAM_PELOTA)
        self.velocidad_y = randint(-VEL_MAX_PELOTA, VEL_MAX_PELOTA)
        self.velocidad_x = 0
        while self.velocidad_x == 0:
            self.velocidad_x = randint(-VEL_MAX_PELOTA, VEL_MAX_PELOTA)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, (250, 250, 0), self)

    def mover(self):
        self.x = self.x + self.velocidad_x
        self.y = self.y - self.velocidad_y

        if self.y <= 0:
            self.y = 0
            self.velocidad_y = -self.velocidad_y
        if self.y >= ALTO-TAM_PELOTA:
            self.y = ALTO-TAM_PELOTA
            self.velocidad_y = -self.velocidad_y

    # def colisionar(self, jugador):
        # jugador.colliderect(self)
        # if self.colliderect(jugador):
            # self.velocidad_x = -self.velocidad_x

    def comprobar_punto(self):
        """
        Devuelve 0 si no hay punto,
        1 si hay punto para el jugador 1 y
        2 si hay punto para el jugador 2
        """
        resultado = 0

        if self.x < 0:
            self.x = (ANCHO - TAM_PELOTA)/2
            self.y = (ALTO - TAM_PELOTA)/2
            self.velocidad_y = randint(-VEL_MAX_PELOTA, VEL_MAX_PELOTA)
            self.velocidad_x = randint(-VEL_MAX_PELOTA, -1)
            print("Punto para el jugador 2")
            resultado = 2
        elif self.x > ANCHO:
            self.x = (ANCHO - TAM_PELOTA)/2
            self.y = (ALTO - TAM_PELOTA)/2
            self.velocidad_y = randint(-VEL_MAX_PELOTA, VEL_MAX_PELOTA)
            self.velocidad_x = randint(1, VEL_MAX_PELOTA)
            print("Punto para el jugador 1")
            resultado = 1

        return resultado


class Marcador:

    ganador = 0

    def __init__(self):
        self.tipo_letra = pygame.font.SysFont('Tahoma', 35, True)
        self.reset()
        self.mostrar()

    def reset(self):
        self.puntuacion = [0, 0]
        self.ganador = 0

    def sumar_punto(self, jugador):
        self.puntuacion[jugador-1] += 1
        self.mostrar()

    def comprobar_ganador(self):
        if self.puntuacion[0] == PUNTOS_PARTIDA:
            self.reset()
            self.ganador = 1
        if self.puntuacion[1] == PUNTOS_PARTIDA:
            print("Gana el jugador 2")
            self.reset()
            self.ganador = 2
        return self.ganador > 0

    def pintar_ganador(self, pantalla):
        msg_texto = f"El ganador es el jugador {self.ganador}"
        texto = pygame.font.Font.render(
            self.tipo_letra, msg_texto, True, C_BLANCO)
        pos_x = ANCHO/2 - texto.get_width()/2
        pos_y = (ALTO - texto.get_height())/2
        pygame.Surface.blit(pantalla, texto, (pos_x, pos_y))

    def mostrar(self):
        print(
            f"El marcador ahora es: ({self.puntuacion[0]}, {self.puntuacion[1]})")


class Pong:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        self.reloj = pygame.time.Clock()

        pos_y = (ALTO-ALTO_PALETA)/2
        pos_x_2 = ANCHO-MARGEN_LATERAL-ANCHO_PALETA

        self.jugador1 = Jugador(MARGEN_LATERAL, pos_y)
        self.jugador2 = Jugador(pos_x_2, pos_y)

        pelota_x = (ANCHO-TAM_PELOTA)/2
        pelota_y = (ALTO-TAM_PELOTA)/2
        self.pelota = Pelota(pelota_x, pelota_y)

        self.marcador = Marcador()

        pygame.font.init()

    def bucle_principal(self):
        salir = False
        empezar = False

        if empezar == False:
            print("Pulsa Espacio para empezar")

        while not salir:

            pygame.key.get_pressed()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    salir = True

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        salir = True
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        empezar = True

            estado_teclas = pygame.key.get_pressed()

            if estado_teclas[pygame.K_a]:
                self.jugador1.muevete(Jugador.ARRIBA)
            if estado_teclas[pygame.K_z]:
                self.jugador1.muevete(Jugador.ABAJO)
            if estado_teclas[pygame.K_k]:
                self.jugador2.muevete(Jugador.ARRIBA)
            if estado_teclas[pygame.K_m]:
                self.jugador2.muevete(Jugador.ABAJO)
                # Dibujo rect??ngulo palas
            pygame.draw.rect(self.pantalla, CBLANCO, self.jugador1)
            pygame.draw.rect(self.pantalla, CBLANCO, self.jugador2)
            # fondo
            pygame.Surface.fill(self.pantalla, AZUL)
            # LINEAS DE CAMPO
            # CENTRAL SUPERIOR
            pygame.draw.lines(self.pantalla, (VERDE), True, [
                              (ANCHO, MARGEN_LATERAL), (-ANCHO, MARGEN_LATERAL)], 2)
            # CENTRAL INFERIOR
            pygame.draw.lines(self.pantalla, (VERDE), True, [
                              (ANCHO, ALTO-MARGEN_LATERAL), (-ANCHO, ALTO-MARGEN_LATERAL)], 2)

            self.jugador1.pintame(self.pantalla)
            self.jugador2.pintame(self.pantalla)
            self.pinta_red()

            if empezar == True:
                self.pelota.mover()

            pygame.display.flip()
            self.reloj.tick(FPS)

    def pinta_pelota(self):
        self.pelota.mover()
        if self.pelota.colliderect(self.jugador1) or self.pelota.colliderect(self.jugador2):
            self.pelota.velocidad_x = -self.pelota.velocidad_x + randint(-2, 2)
            self.pelota.velocidad_y = randint(-VEL_MAX_PELOTA, VEL_MAX_PELOTA)

        self.pelota.pintame(self.pantalla)

    def pinta_red(self):
        tramo_pintado = 15
        tramo_vacio = 15
        ancho_red = 4
        pos_x = ANCHO/2+1 - ancho_red/2
        for y in range(MARGEN, ALTO-MARGEN, tramo_pintado+tramo_vacio):
            pygame.draw.line(self.pantalla, VERDE, (pos_x, y),
                             (pos_x, y+tramo_pintado), ancho_red)


if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()
