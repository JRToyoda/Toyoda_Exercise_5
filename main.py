side_one = (input("Enter the first side: "))
side_two = (input("Enter the second side: "))
side_three = (input("Enter the third side: "))

while (side_one != "") & (side_two != "") & (side_three != ""):

    if side_one == side_two == side_three:
        print("The triangle is equilateral.\n ")

    else:
        print("The triangle is not equilateral.\n ")

    side_one = (input("Enter the first side: "))
    side_two = (input("Enter the second side: "))
    side_three = (input("Enter the third side: "))

print("Error")
