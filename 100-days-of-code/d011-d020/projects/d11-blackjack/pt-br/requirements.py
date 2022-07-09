from random import choice
from art import *
import os

deck = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, }  

def sorteia_carta():
    '''Escolhe uma carta aleatória do dicionário de cartas'''
    return choice(list(deck.keys()))

def distribui_cartas():
    '''Distribui as duas primeiras cartas do jogo'''
    cartas_mao = []
    while len(cartas_mao) < 2:
        carta_aleatoria = sorteia_carta()
        cartas_mao.append(carta_aleatoria)
    return cartas_mao

def calcula_pontos(lista_de_cartas):
    pontos = 0
    for carta in lista_de_cartas:
        pontos += deck[carta]

    if 'A' in lista_de_cartas and pontos > 21:
        pontos -= 10

    return pontos

def adiciona_carta(lista_de_cartas):
    lista_de_cartas.append(sorteia_carta())
    return lista_de_cartas

def compara_pontos(pontos_jogador, pontos_pc):

    resultado = ""
    if pontos_jogador > 21:
        imprimir_linhas()
        decoracao_texto("Você ultrapassou o limite.")
        resultado = perdeu
    elif pontos_jogador <= 21 and pontos_pc > 21:
        imprimir_linhas()
        decoracao_texto("O seu oponente ultrapassou o limite")
        resultado = venceu
    elif pontos_jogador > pontos_pc:
        resultado = venceu
    elif pontos_jogador == pontos_pc:
        resultado = empate
    else:
        resultado = perdeu 
    decoracao_texto(resultado, True)



def quer_continuar(resposta_usuario):
    if (resposta_usuario.lower() == 's'):
        return True
    elif (resposta_usuario.lower() == 'n'):
        return False

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def formatar_lista(qualquer_lista):
    lista_str = ' ][ '.join(qualquer_lista)
    return lista_str

def imprimir_linhas():
    print(f"{'-':-^70}")

def decoracao_texto(qualquer_texto, com_linha=False):
    if com_linha:
        imprimir_linhas()
        print(f"{qualquer_texto:^70}")
        imprimir_linhas()
    else:
        print(f"{qualquer_texto:^70}")

def status_jogo(cartas_jogador, pontos_jogador, primeira_carta_pc):

    texto_lista = [
        f"Suas Cartas: [ {formatar_lista(cartas_jogador)} ]", 
        f"Pontuação atual: {pontos_jogador}", 
        f"Primeira carta do oponente: {primeira_carta_pc}"
        ]

    imprimir_linhas()
    
    for linha in texto_lista:
        decoracao_texto(linha)

    imprimir_linhas()

def texto_final(cartas_jogador, pontos_jogador, cartas_pc, pontos_pc):

    texto_lista = [
        f"Sua cartas: [ {formatar_lista(cartas_jogador)} ]", 
        f"Sua pontuação final é: {pontos_jogador}", 
        f"{'-':-^70}",
        f"Cartas do computador: [ {formatar_lista(cartas_pc)} ]", 
        f"A pontuação final do computador é: {pontos_pc}"
        ]
    
    for linha in texto_lista:
        decoracao_texto(linha)

    compara_pontos(pontos_jogador, pontos_pc)