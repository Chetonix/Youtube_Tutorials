def calculator():
    num1 = input("Enter a number ")
    num2 = input("Enter another number ")
    sign = input("Enter the operator ")

    if sign == "+":
        return float(num1) + float(num2)
    
    if sign == "-":
        return float(num1) - float(num2)
    
    if sign == "/":
        return float(num1) / float(num2)

    if sign == "*":
        return float(num1) * float(num2)


print(calculator())