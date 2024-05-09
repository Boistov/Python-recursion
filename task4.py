def sum_of_subsequence(sequence):
    if not sequence:
        return 0
    else:
        head, *tail = sequence
        if head % 2 == 0:
            return head + sum_of_subsequence(tail)
        else:
            return sum_of_subsequence(tail)

input_sequence = [12, 45, 57, 3, 75, 40, 25, 4, 0]
result = sum_of_subsequence(input_sequence)
print(result)

