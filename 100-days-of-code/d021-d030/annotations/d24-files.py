# This approach doesn't close the file automatically after manipulation, so we have to use .close() at the end
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# Using the with keyword, the file is automatically closed after manipulation
# The default mode is "r" -> reading, that doesn't allow to write on the file. We must specify if we want to write.
# mode="w" create new file/overwrite the contents and mode="a" appends to the end of file
# with open("new_file.txt", mode="w") as file:
#     file.write("Hello new file.")

# Absolute file path:
with open("/Usuarios/Usuario/Desktop/my_file.txt") as file:
    content = file.read()
    print(content)

# Relative file path:
# Working directory:
# D:\Usuarios\Usuario\Desktop\Estudos\GitHub\py-practices\100-days-of-code\d021-d030\annotations
with open("../../../../../../my_file.txt") as file:
    content = file.read()
    print(content)