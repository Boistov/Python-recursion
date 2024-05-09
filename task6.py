def find_index(input_list, target_string):
    for i, item in enumerate(input_list):
        if item == target_string:
            return i
    return -1

my_list = ["apple", "banana", "cherry", "date"]
search_string = "banana"
result = find_index(my_list, search_string)
if result != -1:
    print(search_string,result)
else:
    print(search_string)
