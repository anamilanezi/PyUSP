# 6.5

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'parana': 'brazil',
    'paraguai': 'paraguai',
    'seine': 'france',
    'mississipi': 'united states',
    'river plate': 'argentina',
}

for name, country in sorted(rivers.items()):
    print(f"The {name.title()} runs through {country.title()}.")

print("\n\tHere are all the rivers recorded:")
for name in sorted(rivers):
    print(name.title())

print("\n\tHere are all the countries recorded:")
for country in set(sorted(rivers.values())):
    print(country.title())