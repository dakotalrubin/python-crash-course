guest_list = ['albert einstein', 'alan turing', 'elon musk']

print(f"Hello, {guest_list[0].title()}. I'd like to invite you to dinner.")
print(f"Hello, {guest_list[1].title()}. I'd like to invite you to dinner.")
print(f"Hello, {guest_list[-1].title()}. I'd like to invite you to dinner.")

print(f"Unfortunately, it appears that {guest_list[0].title()} can't make it.")

guest_list[0] = 'sam altman'

print(f"Hello, {guest_list[0].title()}. I'd like to invite you to dinner.")
print(f"Hello, {guest_list[1].title()}. I'd like to invite you to dinner.")
print(f"Hello, {guest_list[-1].title()}. I'd like to invite you to dinner.")