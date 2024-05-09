def count_potatoes(string):
    num = string.lower()
    count = num.count("potato")
    return count

num1 = input()
potato_count = count_potatoes(num1)
print(potato_count)
