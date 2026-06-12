import pygame

# pygame setup
pygame.init()

tamanho_tela = (800,800)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Jogo da Dani")

tamanho_bola = 15
bola = pygame.Rect(100, 500, tamanho_bola, tamanho_bola)


tamanho_jogador = 100
jogador = pygame.Rect(0,750, tamanho_jogador, 15)

qtd_blocos_linha = 6
qtd_linhas = 8

qtd_total_blocos = qtd_blocos_linha * qtd_linhas

cores = {
    "branca": (255, 255, 255),
    "preta": (0, 0, 0),
    "amarela": (255, 255, 0),
    "azul": (0, 0, 255),
    "verde": (0, 255, 0)
}

fim = False
pontuacao = 0
movimento_bola = [7,-7]

def criar_blocos(qtd_blocos_linha, qtd_linhas):
    larguraTela = tamanho_tela[0]
    alturaTela = tamanho_tela[1]
    distanciaBlocos = 5
    larguraBloco = larguraTela / qtd_blocos_linha - distanciaBlocos
    alturaBloco = 15
    distancia_entre_linhas = alturaBloco + 10
    blocos = []

    for j in range(qtd_blocos_linha):
        for i in range(qtd_linhas):
            bloco = pygame.Rect(i * (larguraBloco + distanciaBlocos), j * (alturaBloco + distancia_entre_linhas), larguraBloco, alturaBloco)
            blocos.append(bloco)

    return blocos

def desenhar_inicio():
    tela.fill(cores["preta"])
    pygame.draw.rect(tela, cores["azul"], jogador)
    pygame.draw.rect(tela, cores["branca"], bola)

def desenhar_blocos(blocos):
    for bloco in blocos:
        pygame.draw.rect(tela, cores["verde"], bloco)


blocos = criar_blocos(qtd_blocos_linha, qtd_linhas)

while not fim:
    desenhar_inicio()
    desenhar_blocos(blocos)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim = True

    pygame.time.wait(1)
    pygame.display.flip()


pygame.quit()