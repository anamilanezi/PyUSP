cities = {
    'criciúma': {
        'país': 'Brasil',
        'população': 210000,
        'curiosidade': 'Ganhou a Copa do Brasil de 1992',
    },
    'salvador': {
        'país': 'Brasil',
        'população': 2900000,
        'curiosidade': 'Primeira capital do Brasil',
    },
    'rotterdam': {
        'país': 'Holanda',
        'população': 624000,
        'curiosidade': 'Possui o maior porto da Europa'
    }
}

for city in cities:
    print(f"Algumas informações sobre a cidade de {city.title()}:")
    for info in cities[city]:
        print(f"{info.title()}: {cities[city][info]}")
    print()