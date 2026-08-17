print("Welcome to the Greater Than comparison Game!")

number = float(input("\nPlease enter the number you want to check: "))

value = float(input("\nPlease enter the value you want to compare it to: "))

if number > value:
    print("\nThe number", number, "is greater than", value, ".")
    print("\nI am in the if statement")
else:
    print("\nThe number", number, "is not greater than", value, ".")
    print("\nI am in the else statement")

print("\nI am neither in the if statement nor the else statement")

print("\nThank you for using the Greater Than comparison Game!")