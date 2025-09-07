i = 0

while i < 5:
    tunnus = input("Enter username: ")
    salasana = input("Enter password: ")

    if tunnus == "python" and salasana == "rules":
        print("Welcome")
        break
    else:
        i += 1
        if i == 5:
            print("Access denied")
            break
        else:
            print("Incorrect username or password. Please try again.")