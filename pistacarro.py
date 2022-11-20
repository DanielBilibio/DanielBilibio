jogador = input("\nInsira seu nome e email: ")

import pygame
import random
import time
pygame.init()
pygameDisplay = pygame.display
pygameDisplay.set_caption("Pista carro")
altura = 800
largura = 1000
tamanho = (largura, altura)
gameDisplay = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
gameEvents = pygame.event
branco = (255,255,255)
fundo = pygame.image.load("assets/pista.jpg")
carro = pygame.image.load("assets/carro.png")
ambulancia = pygame.image.load("assets/ambulancia.png")


def escreverTexto (texto):
    fonte  = pygame.font.Font("freesansbold.ttf",25)
    textoDisplay = fonte.render(texto,True,branco)
    gameDisplay.blit(textoDisplay, (10,10))
    pygameDisplay.update()

def bateu():
    fonte  = pygame.font.Font("freesansbold.ttf",95)
    fonte2  = pygame.font.Font("freesansbold.ttf",45)
    textoDisplay = fonte.render("BATEU!!!!",True,branco)
    textoDisplay2 = fonte2.render("press enter para continuar!!!!",True,branco)
    gameDisplay.blit(textoDisplay, (150,150))
    gameDisplay.blit(textoDisplay2, (150,350))
    pygameDisplay.update()

def jogar():
    jogando = True
    carrox = 550
    carroy = 30
    movimentocarrox = 0
    larguracarro = 150
    alturacarro = 210
    alturaambulancia = 210
    larguraambulancia = 150
    posicaoambulanciax = 500
    posicaoambulanciay = 850
    velocidadeambulancia = 3
    pontos = 0
    pygame.mixer.music.load("assets/somrodovia.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(-1)


    batidaSound = pygame.mixer.Sound("assets/sombatida.mp3")
    batidaSound.set_volume(1)
    while True:
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentocarrox = -15
                elif event.key == pygame.K_RIGHT:
                    movimentocarrox = 15
                elif event.key == pygame.K_RETURN:
                    jogar()
            elif event.type == pygame.KEYUP:
                movimentocarrox = 0
            
        if jogando:
            if (posicaoambulanciay <= -200):
                posicaoambulanciay = 900
                posicaoambulanciax = random.randint(200,800)
                velocidadeambulancia = velocidadeambulancia +1
                
                pontos = pontos + 1

            else:
                posicaoambulanciay = posicaoambulanciay - velocidadeambulancia

            if carrox + movimentocarrox >0 and carrox + movimentocarrox < largura-larguracarro-50:
                carrox = carrox + movimentocarrox
            gameDisplay.fill(branco)
            gameDisplay.blit(fundo,(0,0))
            gameDisplay.blit(carro, (carrox, carroy))
            
            gameDisplay.blit(ambulancia, (posicaoambulanciax,posicaoambulanciay))
            escreverTexto("Pontos: "+str(pontos))

            pixelsXcarro = list(range(carrox, carrox+larguracarro))
            pixelsYcarro = list(range(carroy, carroy+alturacarro))

            pixelXambulancia = list(range(posicaoambulanciax, posicaoambulanciax+larguraambulancia))
            pixelYambulancia = list(range(posicaoambulanciay, posicaoambulanciay+alturaambulancia))

            colisaoY = len(list(set(pixelYambulancia) & set(pixelsYcarro) ))
            if colisaoY > 0:
                colisaoX = len(list(set(pixelXambulancia) & set(pixelsXcarro) ))
                print(colisaoX)
                if colisaoX > 45:
                    bateu()
                    jogando=False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(batidaSound)
            
            with open('jogador.txt','w') as arquivos:
                for dados in jogador:
                    arquivos.write (jogador) 

        pygameDisplay.update()
        clock.tick(60)

jogar()
