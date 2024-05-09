def odd_numbers(start, end):
    if start > end:
        return
    if start % 2 != 0:
        print(start, end=" ")
    odd_numbers(start + 1, end)

num1 = int(input())
num2 = int(input())
odd_numbers(num1, num2)
