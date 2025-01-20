def make_pizza(size, *toppings):
    """Summarize the pizza we're about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")

    for topping in toppings:
        print(f"\t{topping}")

make_pizza(16, 'pepperoni')
make_pizza(10, 'mushrooms', 'green peppers', 'extra cheese')