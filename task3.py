def sum_of_digit(n):
    if n < 10:
        return n
    else:
        return n + sum_of_digit(n // 10)

number = float(input("Enter number: "))
num = sum_of_digit(number)
print(num, "OM")









