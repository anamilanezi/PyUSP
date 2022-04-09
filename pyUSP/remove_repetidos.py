def remove_repetidos(lista):
    lista.sort()
    nova_lista = []
    for i in lista:
        if i not in nova_lista:
            nova_lista.append(i)
    return nova_lista
