#####    C3.8  Python Crash Course 09/01/2022 	 #####
#                 Seeing the world                   #
######################################################

places_to_visit = ['Italy',
				   'China',
				   'Thailand',
				   'Turkey',
				   'Australia'	
				   ]

print("Here are the places I want to visit:")
print(places_to_visit)

# Sort list temporarily

print(f"\nHere are the temporary list, with places sorted alphabetically")
print(sorted(places_to_visit))

print("\nHere are the original list:")
print(places_to_visit)

print(f"\nHere are the temporary list, with places sorted in reverse order:")
print(sorted(places_to_visit, reverse=True))

print("\nHere are the original list:")
print(places_to_visit)

# Reverse list

places_to_visit.reverse()
print("\nList after using reverse:")
print(places_to_visit)

places_to_visit.reverse()
print(f"\nUsing reverse again, the list goes back to its original form:")
print(places_to_visit)

# Sort list permanently 

places_to_visit.sort()
print("\nList after using permanent sort:")
print(places_to_visit)

places_to_visit.sort(reverse=True)
print("\nList after using permanent  reverse sort:")
print(places_to_visit)
