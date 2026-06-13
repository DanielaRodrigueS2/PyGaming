import pygame

# pygame setup
pygame.init()

tamanho_tela = (800,800)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Jogo da Dani")

tamanho_bola = 30
bola = pygame.Rect(100, 500, tamanho_bola, tamanho_bola)


tamanho_jogador = 150
jogador = pygame.Rect(0,750, tamanho_jogador, 30)

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
movimento_bola = [1,-1]

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

def movimentar_jogador(evento):
    if evento[pygame.K_RIGHT]:
        if (jogador.x + tamanho_jogador) < tamanho_tela[0]:
            jogador.x = jogador.x + 5
    if evento[pygame.K_LEFT]:
        if (jogador.x > 0):
            jogador.x = jogador.x - 5

def movimentar_bola(bola):
    movimento = movimento_bola
    bola.x = bola.x + movimento[0]
    bola.y = bola.y + movimento[1]

    if bola.x <= 0:
        movimento[0] = -movimento[0]
    if bola.y <= 0:
        movimento[1] = -movimento[1]
    if (bola.x + tamanho_bola) >= tamanho_tela[0]:
        movimento[0] = -movimento[0]
    if (bola.y+ tamanho_bola) >= tamanho_tela[1]:
        movimento = None

    if jogador.collidepoint(bola.x, bola.y):
        movimento[1] = -movimento[1]

    for bloco in blocos:
        if bloco.collidepoint(bola.x, bola.y):
            blocos.remove(bloco)
            movimento[1] = -movimento[1]

    return movimento

def atualizar_pontuacao(pontuacao):
    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f"Pontuação: {pontuacao}", 1, cores["amarela"])
    tela.blit(texto, (0, 780))
    if pontuacao >= qtd_total_blocos:
        return True
    else:
        return False

blocos = criar_blocos(qtd_blocos_linha, qtd_linhas)

while not fim:
    desenhar_inicio()
    desenhar_blocos(blocos)
    fim = atualizar_pontuacao(qtd_total_blocos - len(blocos))
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim = True


    teclas = pygame.key.get_pressed()

    movimento_bola = movimentar_bola(bola)
    movimentar_jogador(teclas)

    if not movimento_bola:
        fim = True

    pygame.time.wait(1)
    pygame.display.flip()


pygame.quit()