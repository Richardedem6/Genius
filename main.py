# ******simple calculator******
# 1. ADD
# 2. SUBTRACT
# 3. MULTIPLY
# 4. DIVIDE

print("Select an operation to perform: ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

# so using if else statement, a simple calculator program will be designed.
operation = input()
if operation == "1":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) + int(num2)))
    # if any integer entered under the operation 1, an addition is done
elif operation =="2":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The difference is " + str(int(num1) + int(num2)))
    # if any integer entered under the operation 2, a subtraction is done
elif operation == "3":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The product is " + str(int(num1) + int(num2)))
    # if any integer entered under the operation 3, a multiplication is done
elif operation == "4":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The result is " + str(int(num1) + int(num2)))
    # if integers entered under the operation 4, a division is done
else:
    print ("Invalid Entry")



