n1 = int(input("Write the number one : "))
n2 = int(input("Write the number two : "))

def add_num(n1, n2):
    result = n1 + n2 
    return result

def multiply_num(n1, n2):
    result = n1 * n2
    return result

add = add_num(n1, n2)
mult = multiply_num(n1, n2)

print("", "The sum of numbers : ", add,"\n","The multiply of numbers: ", mult)
