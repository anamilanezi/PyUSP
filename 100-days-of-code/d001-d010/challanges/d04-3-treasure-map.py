# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# row1[0] = ["0","1","2"]
# row2[1] = ["0","1","1"]
# row3[2] = ["0","1","2"]
# CL
# row1 = ["11","21","31"]
# row2 = ["12","22","32"]
# row3 = ["13","23","33"]
# Exemplo: 32 => map[1][2] (2-1) (3-1)

# selected_row = int(position[1]) -> vertical
# selected_col = int(position[0]) -> horizontal

selected_row = int(position) % 10    
selected_col = int(position) // 10  

map[selected_row - 1][selected_col-1] = 'X'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
