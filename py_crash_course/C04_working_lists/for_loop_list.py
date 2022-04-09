##############################################################
#####    CHAPTER 04  Python Crash Course 09/01/2022 	 #####
#####                Working with lists	                 #####
##############################################################

magicians = ['alice', 'david', 'carolina']
for magician in magicians:						# For every magician in the list of magicians,
	print(magician.title())						# print the magician's name

print()
for magician in magicians:
	print(f"Hey, {magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}!\n")

print("Thank you everyone. That was a great magic show!")

