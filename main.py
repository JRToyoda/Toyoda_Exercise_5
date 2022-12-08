while True:

    side_one = (input("Enter the first side: "))
    side_two = (input("Enter the second side: "))
    side_three = (input("Enter the third side: "))

    if side_one == side_two == side_three:
        print("The triangle is equilateral.\n ")

    elif (side_one != "") & (side_two != "") & (side_three != ""):
        print("The triangle is not equilateral.\n ")

    else:
        print("Error\n")



