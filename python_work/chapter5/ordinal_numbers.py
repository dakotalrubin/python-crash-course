digits = [value for value in range(1, 10)]

for digit in digits:
    if digit == 1:
        suffix = 'st'
    elif digit == 2:
        suffix = 'nd'
    elif digit == 3:
        suffix = 'rd'
    else:
        suffix = 'th'

    print(str(digit) + suffix)