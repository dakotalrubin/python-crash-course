my_pizzas = ['pepperoni', 'pineapple', 'pesto']
friend_pizzas = my_pizzas[:]

my_pizzas.append('veggie')
friend_pizzas.append('sausage')

print("My favorite pizzas are:")

for pizza in my_pizzas:
  print(f"\t{pizza.title()}")
  
print("\nMy friend's favorite pizzas are:")

for pizza in friend_pizzas:
  print(f"\t{pizza.title()}")