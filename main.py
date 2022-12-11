side_one = (input("Enter the first side: "))
side_two = (input("Enter the second side: "))
side_three = (input("Enter the third side: "))

if not side_one.isnumeric() or not side_two.isnumeric() or not side_three.isnumeric():
    print("Please input positive integer\n")

elif side_one == side_two == side_three:
    print("The triangle is equilateral.\n ")

elif side_one != "" or side_two != "" or side_three != "":
    print("The triangle is not equilateral.\n ")
