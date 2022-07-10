filo = input().lower()   # vertebrado
classe = input().lower() # mamifero
ordem = input().lower()  # onivoro

filos_dic = {
    'vertebrado': {
        'ave': {
            'carnivoro': 'aguia',
            'onivoro': 'pomba'
        },
        'mamifero': {
            'onivoro': 'homem',
            'herbivoro': 'vaca',
        }
    },
    'invertebrado': {
        'inseto': {
            'hematofago': 'pulga',
            'herbivoro': 'lagarta'
        },
        'anelideo': {
            'hematofago': 'sanguessuga',
            'onivoro': 'minhoca'
        }
    }
}

if filo in filos_dic:
    filos = filos_dic[filo]
   # print(filos)
    if classe in filos:
        classes_dic = filos[classe]
    #    print(classes_dic)
        if ordem in classes_dic:
            animal = classes_dic[ordem]
            print(animal)
