sandwich_orders = ['BLT', 'reuben', 'chicken', 'ham and cheese']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()

    print(f"I made your {order} sandwich.")
    finished_sandwiches.append(order)

print("\nThese sandwich orders have been made:")

for sandwich in finished_sandwiches:
    print(f"\t{sandwich}")