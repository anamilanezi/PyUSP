import turtle
import pandas
import time

# Cria a tela, define imagem como fundo
tela = turtle.Screen()
tela.title("Estados do Brasil")
tela.setup(width=643, height=605)
img = "Brazil_Political_Map.gif"
tela.addshape(img)
turtle.shape(img)

# Cria um objeto Turtle para escrever na tela
escrita = turtle.Turtle()
escrita.hideturtle()


# Obtém as cordenadas x e y de um estado ou capital
def obter_xy(tipo, resposta_usuario):
    dados_linha = data[data[tipo] == resposta_usuario]
    x = int(dados_linha.x)
    y = int(dados_linha.y)
    coordenadas = (x, y)
    return coordenadas


# Escrever o nome do Estado ou Capital no mapa
def escrever_nome(tipo):
    escrita.penup()
    escrita.goto(obter_xy(tipo, resposta))
    escrita.write(resposta, align='center', font=('Consolas', 8, 'bold'))


# Inciando a contagem
exibe_acertos = ""
conta_acertos = 0


# Obter a lista de Estados e Capitais do arquivo CSV
data = pandas.read_csv("estados_capitais_br.csv")
lista_estados = data.estado.to_list()
lista_capitais = data.capital.to_list()

# Listas para testar o programa:
# lista_estados = ["Amazonas", "Bahia"]
# lista_capitais = ["Porto Alegre", "Rio de Janeiro", "São Luís"]


jogar_capitais = True

# Pede para usuário adivinhar um Estado enquanto a lista não estiver vazia
while lista_estados:

    # Entrada da resposta
    resposta = tela.textinput(title=f"Adivinhe os Estados {exibe_acertos}", prompt="Diga o nome de um Estado:           ").title()

    # Sair do modo de adivinhação de Estados
    if resposta == "Sair":
        continuar = tela.textinput(title="Adivinhe as Capitais",
                         prompt="Gostaria de tentar adivinhar as capitais? (S/N)").title()
        if continuar == "S":
            jogar_capitais = True
        else:
            jogar_capitais = False
        break

    # Verifica se a resposta do usuário está na lista de estados:
    if resposta in lista_estados:

        # Remove respostas corretas da lista original
        lista_estados.remove(resposta)

        # Escreve respostas corretas no mapa
        escrever_nome('estado')

        # Pausa momentaneamente para usuário poder ver o mapa
        time.sleep(1.5)

        # Atualiza a contagem de acertos:
        conta_acertos += 1
        exibe_acertos = f"{conta_acertos}/27"

# Pausa tela após acertar todos os nomes
time.sleep(1.5)

# Limpa a tela
escrita.clear()

# Reinicia contagem
exibe_acertos = ""
conta_acertos = 0

#
if jogar_capitais:
    while lista_capitais:

        # Ask the user for an answer
        resposta = tela.textinput(title=f"Adivinhe as Capitais {exibe_acertos}", prompt="Diga o nome de uma capital:          ").title()

        if resposta == "Sair":
            break

        if resposta in lista_capitais:
            lista_capitais.remove(resposta)
            escrever_nome('capital')
            time.sleep(1.5)
            conta_acertos += 1
            exibe_acertos = f"{conta_acertos}/27"

# Cria um arquivo CSV com lista de estados e capitais que usuário não acertou
if lista_estados:
    estados_dict = {
        'estados': lista_estados
    }
    data = pandas.DataFrame(estados_dict)
    data.to_csv("estados_para_aprender.csv")

if lista_capitais:
    capitais_dict = {
        'capitais': lista_capitais
    }
    data = pandas.DataFrame(capitais_dict)
    data.to_csv("capitais_para_aprender.csv")

tela.exitonclick()
