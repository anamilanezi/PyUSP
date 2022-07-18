#####    C3.4  Python Crash Course 09/01/2022 	 #####
# I'm still learning Python but this list obviously  #
# can be optimized using functions and loops so as a #
# a reminder for the future that I shoul improve the #
# code!												 #
######################################################

#####            CREATES GUEST LIST            ##### 

guest_list = ['sufjan stevens',          	# 0 
			  'alanis morissette', 			# 1
			  'beyonce', 					# 2
			  'gilberto gil']				# 3

message = ", you're invited to dinner!"

print(f"Initial list: {guest_list}")

print()
print(f"{guest_list[0].title()}{message}")  # Print message to index 
print(f"{guest_list[1].title()}{message}")
print(f"{guest_list[2].title()}{message}")
print(f"{guest_list[3].title()}{message}")

##### UPDATE LIST BY CHANGING A VALUE ######

not_going = 'beyonce'

print("\nUPDATE LIST:")
print(f"{not_going.title()} can't attend to the dinner")

guest_list[2] = 'dua lipa'
print(f"{guest_list[2].title()} will be joining us. Updated list: {guest_list}")

##### ADDING NEW GUESTS ####

print("\nGood news! We've found a bigger table!\n")

guest_list.insert(0, 'Xandy')						# Insert a new element to specified index
guest_list.insert(2, 'Juliette')					# Insert a new element to specified index 
guest_list.append('lula')							# Insert new element to end of list

	 
print(f"{guest_list[0].title()}{message}")          # Print message to all new guests
print(f"{guest_list[1].title()}{message}")
print(f"{guest_list[2].title()}{message}")
print(f"{guest_list[3].title()}{message}")
print(f"{guest_list[4].title()}{message}")
print(f"{guest_list[5].title()}{message}")
print(f"{guest_list[6].title()}{message}")
print(f"\nThis is the new guest list: {guest_list}")

#### SHRINKING GUEST LIST USING .POP

print("\nWe are sorry to announce that for safety reasons, we can now invite only two guests.\n")

pop_message = ", sorry I can't invite you to dinner anymore."

pop_guest = guest_list.pop(0)						# Pop first element of list (Xandy)
print(f"{pop_guest.title()}{pop_message}")  		# Message to first element of list

# Elements new order: 0 - Sufjan, 1 - Juliette, 2 - Alanis, 3 - Dua, 4 - Gilberto, 5 - Lula

pop_guest = guest_list.pop(1)						# Pop second element of updated list (Juliette)
print(f"{pop_guest.title()}{pop_message}")			# Message to popped element

# Elements new order: 0 - Sufjan, 1 - Alanis, 2 - Dua Lipa, 3 - Gilberto, 4 - Lula

pop_guest = guest_list.pop(1)						# Pop second element of updated list (Alanis)
print(f"{pop_guest.title()}{pop_message}")			# Message to popped element

# Elements new order: 0 - Sufjan, 1 - Dua Lipa, 2 - Gilberto, 3 - Lula

pop_guest = guest_list.pop(1)						# Pop second element of updated list (Dua Lipa)
print(f"{pop_guest.title()}{pop_message}")			# Message to popped element

# Elements new order: 0 - Sufjan, 1 - Gilberto, 2 - Lula

pop_guest = guest_list.pop(1)						# Pop second element of updated list (Gilberto)
print(f"{pop_guest.title()}{pop_message}\n")		# Message to popped element

# Remaining elements: 0 - Sufjan, 1 - Lula
message = ", congratulations! You're still invited to dinner! :)"

print(f"{guest_list[0].title()}{message}") 
print(f"{guest_list[1].title()}{message}") 

print(f"\nSorry, the dinner was canceled.") 

del guest_list[0]				# Delete item index 0
del guest_list[0]				# Delete item index 0

print(f"Final list: {guest_list}")

