# Qn: Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string

def remove_chars(str_input, num):
    new_string = ""

    for i in range(num, len(str_input)):
        new_string += str_input[i]
    
    return new_string

print(remove_chars("pynative", 4))