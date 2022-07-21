# 6.6

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

coders = ['maria', 'giovana', 'phil', 'jen']

for coder in sorted(coders):
    if coder not in favorite_languages.keys():
        print(f"{coder.title()}, please take our poll!")
    else:
        print(f"{coder.title()}, thank you for taking our poll!")