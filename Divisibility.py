def last_digits_by_ten(array):
    number = 0 
    last_digits = [n % 10 for n in array]
    for current_digit in last_digits:
        number = number*10 + current_digit
    return 'Yes' if number % 10 == 0 else 'No'

x = int(input())
arrayx = list(map(int, input().split()))

result = last_digits_by_ten(arrayx)
print(result)