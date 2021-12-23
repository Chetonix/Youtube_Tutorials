def calculator():
    cont = "c"
    num1 = input("Enter a number: ")
    sign = input("Enter the operator: ")
    num2 = input("Enter another number: ")

    if sign == "+":
        return float(num1) + float(num2)
    
    if sign == "-":
        return float(num1) - float(num2)
    
    if sign == "/":
        r = input("Please tell if you want remainder by saying y/n: ")
        if r == "y":
            return "%f: remainder and %f: division" %(float(num1) % float(num2), float(num1) / float(num2))
        else:
            return "%f: division" %(float(num1) / float(num2))

    if sign == "*":
        return float(num1) * float(num2)

cont = "c"

while (cont == "c"):
    print(calculator())
    cont = input("Type c to continue or any other key to exit: ")
    
        
            

