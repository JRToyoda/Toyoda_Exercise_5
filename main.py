def triangle():
    i = 0
    while i < 2:
        i += 1
        side_one = int(input("Enter the first side: "))
        side_two = int(input("Enter the second side: "))
        side_three = int(input("Enter the third side: "))

        if side_one == side_two == side_three:
            print("The triangle is equilateral.\n ")

        else:
            print("The triangle is not equilateral.\n ")

triangle()