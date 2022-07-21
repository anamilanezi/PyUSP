# # 6.3 Glossary
#
# glossary = {
#     'list': 'Lists are used to store multiple items in a single variable.',
#     'tuple': 'A tuple is a collection which is ordered and unchangeable.',
#     'dictionary': 'Dictionaries are used to store data values in key:value'
#                   ' pairs.',
#     'if_elif_else': 'Allows to perform actions based on conditions.',
#     'for_loop': 'A for loop is used for iterating over a sequence (that is eit'
#                 'her a list, a tuple, a dictionary, a set, or a string).',
#     'string': 'A series of characters.',
#     'comment': 'A note in a program that the Python interpreter ignores.',
# }
#
# # Sugestão de resolução do livro
#
# word = 'string'
# print(f"\n{word.title()}: {glossary[word]}")
#
# word = 'comment'
# print(f"\n{word.title()}: {glossary[word]}")
#
# # Minha resolução
#
# meaning = glossary['list']
# print(f"List: {meaning}")
#
# meaning = glossary['tuple']
# print(f"Tuple: {meaning}")
#
# meaning = glossary['dictionary']
# print(f"Dictionary: {meaning}")
#
# meaning = glossary['if_elif_else']
# print(f"If-elif-else: {meaning}")
#
# meaning = glossary['for_loop']
# print(f"For loop: {meaning}")

# 6.4

glossary = {
    'list': 'Lists are used to store multiple items in a single variable.',
    'tuple': 'A tuple is a collection which is ordered and unchangeable.',
    'dictionary': 'Dictionaries are used to store data values in key:value'
                  ' pairs.',
    'if_elif_else': 'Allows to perform actions based on conditions.',
    'for_loop': 'A for loop is used for iterating over a sequence (that is eit'
                'her a list, a tuple, a dictionary, a set, or a string).',
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'set': 'is a collection which is unordered, unchangeable, and unindexed.'
           ' No duplicate members.',
    'boolean': 'Booleans represent one of two values: True or False.',
    'variable': 'Variables are containers for storing data values.',
    'operators': 'Operators are used to perform operations on variables and v'
                 'alues.'
}

print("Here is the python glossary I've made so far:")

for word, meaning in sorted(glossary.items()):
    print(f"\n{word.title()}:")
    print(meaning)
