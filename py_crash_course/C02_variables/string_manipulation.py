 # Tabulação, nova linha e eliminar espaços branco extra

print("\tPython")                                                    ##Insere tabulação no início da frase
print("Languages:\nPython,\nJavaScript,\nC++")                       ##Começa nova linha
print("Languages:\n\tPython,\n\tJavaScript,\n\tC++")                 ##Combinação dos dois

favorite_language = 'Python   '                                          ##String com espaços em branco no final
print(f"01: Minha linguagem favorita é {favorite_language}.")            ##Output sem uso de .rtrip()
print(f"02: Minha linguagem favorita é {favorite_language.rstrip()}.")   ##Output com .rstrip() elimina os espaços extra


favorite_language = favorite_language.rstrip()                       ##Armazena o valor na variável sem os espaços extra de forma permanente
print(f"03: Minha linguagem favorita é {favorite_language}.")

whitespace = "  espaços  "
print(f"Aqui podemos ver os {whitespace} extra.")

print(f"Aqui podemos ver somente o .lstrip em ação: {whitespace.lstrip()}, mantendo espaços à direita")
print(f"Aqui podemos ver .strip em ação: {whitespace.strip()}, espaços removidos")
