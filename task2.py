def is_palindrome_number(num):
    num_str = str(num)
    return num_str == num_str[::-1]

def is_palindrome_string(text):
    processed_text = text.lower().replace(" ", "")
    return processed_text == processed_text[::-1]

number = int(input("Enter a number: "))
if is_palindrome_number(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

text = input("Enter a string: ")
if is_palindrome_string(text):
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")
