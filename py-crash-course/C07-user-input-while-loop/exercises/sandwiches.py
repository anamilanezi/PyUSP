sandwich_orders = ['tuna', 'chesse', 'pastrami', 'bacon', 'pastrami', 'chicken', 'meatball', 'pastrami']
finished_sandwiches = []

print(sandwich_orders)
print("Sorry, the deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"\t- I'm making a {current_order} sandwich.")
    finished_sandwiches.append(current_order)

print(f"Here are all the finished sandwiches: ")
for sandwich in finished_sandwiches:
    print(sandwich.title())