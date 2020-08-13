#Qn: Given a string, display only those characters which are present at an even index number.

def print_even_chars(str_input):
    for i in range(0, len(str_input), 2):
        print(str_input[i])

text = "pynative"
print("Original string is " + text)
print("Printing only even index chars")
print_even_chars(text)