guest_list = ['albert einstein', 'alan turing', 'elon musk']

print(f"Hello, {guest_list[0].title()}. I'd like to invite you to dinner.")
print(f"Hello, {guest_list[1].title()}. I'd like to invite you to dinner.")
print(f"Hello, {guest_list[-1].title()}. I'd like to invite you to dinner.")

print(f"Unfortunately, it appears that {guest_list[0].title()} can't make it.")

guest_list[0] = 'sam altman'

print(f"Hello, {guest_list[0].title()}. I'd like to invite you to dinner.")
print(f"Hello, {guest_list[1].title()}. I'd like to invite you to dinner.")
print(f"Hello, {guest_list[-1].title()}. I'd like to invite you to dinner.")

print("I found a bigger table. We can invite three more people!")

guest_list.insert(0, 'steve wozniak')
guest_list.insert(2, 'richard stallman')
guest_list.append('carl sagan')

print(f"Hello, {guest_list[0].title()}. I'd like to invite you to dinner.")
print(f"Hello, {guest_list[1].title()}. I'd like to invite you to dinner.")
print(f"Hello, {guest_list[2].title()}. I'd like to invite you to dinner.")
print(f"Hello, {guest_list[3].title()}. I'd like to invite you to dinner.")
print(f"Hello, {guest_list[4].title()}. I'd like to invite you to dinner.")
print(f"Hello, {guest_list[5].title()}. I'd like to invite you to dinner.")