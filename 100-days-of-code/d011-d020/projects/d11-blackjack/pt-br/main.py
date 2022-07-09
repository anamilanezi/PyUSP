############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import *
from requirements import *
from random import choice
import os

def inicia_jogo():
    jogar = input("Você gostaria de jogar uma partida de Blackjack? Digite 's' ou 'n': ")

    if quer_continuar(jogar):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        cartas_jogador = distribui_cartas()
        pontos_jogador = calcula_pontos(cartas_jogador)
        cartas_pc = distribui_cartas()
        pontos_pc = calcula_pontos(cartas_pc)
        primeira_carta_pc = cartas_pc[0]

        status_jogo(cartas_jogador, pontos_jogador, primeira_carta_pc)

        if pontos_jogador == 21:
            decoracao_texto("BLACKJACK!")
            decoracao_texto(venceu, True)
            inicia_jogo()

        while pontos_jogador < 21:
            add_carta = input("\tDigite 's' para comprar uma carta, 'n' para passar a vez: ")

            if quer_continuar(add_carta):
                imprimir_linhas()
                cartas_jogador = adiciona_carta(cartas_jogador)
                pontos_jogador = calcula_pontos(cartas_jogador)
                status_jogo(cartas_jogador, pontos_jogador, primeira_carta_pc)

            if not quer_continuar(add_carta):
                imprimir_linhas()
                break

        while pontos_pc < 17: 
            cartas_pc = adiciona_carta(cartas_pc) 
            pontos_pc = calcula_pontos(cartas_pc)   

        
        texto_final(cartas_jogador, pontos_jogador, cartas_pc, pontos_pc)
        inicia_jogo()

    else: 
        quit()

limpar()
decoracao_texto(logo, True)
inicia_jogo()