# Question: Given a two integer numbers return their product and  if the product is greater than 1000, then return their sum

def sum_nums(n1, n2):
    prod = n1 * n2
    if prod > 1000:
        return n1 + n2
    else:
        return prod


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = sum_nums(num1, num2)
print("The result is: {}".format(result))
