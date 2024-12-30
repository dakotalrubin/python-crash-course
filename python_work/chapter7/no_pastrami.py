sandwich_orders = ['pastrami', 'BLT', 'reuben', 'pastrami', 'chicken', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami!\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    order = sandwich_orders.pop()

    print(f"I made your {order} sandwich.")
    finished_sandwiches.append(order)

print("\nThese sandwich orders have been made:")

for sandwich in finished_sandwiches:
    print(f"\t{sandwich}")