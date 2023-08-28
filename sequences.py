def remove_duplicates(sequence):
    result_list = []
    for item in sequence:
        if item not in result_list:
            result_list.append(item)
    return result_list

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  
