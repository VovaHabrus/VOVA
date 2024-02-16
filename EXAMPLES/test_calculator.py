def test_cal_if():
    command = input("Your command is ? ")
    if command == "*":
        num_1 = int(input("Num 1 = "))
        num_2 = int(input("Num 2 = "))
        res = num_1 * num_2
        print("Result is : ", res)
    elif command == "/":
        num_1 = int(input("Num 1 = "))
        num_2 = int(input("Num 2 = "))
        res = num_1 / num_2
        print("Result is : ", res)
    elif command == "+":
        num_1 = int(input("Num 1 = "))
        num_2 = int(input("Num 2 = "))
        res = num_1 + num_2
        print("Result is : ", res)
    elif command == "-":
        num_1 = int(input("Num 1 = "))
        num_2 = int(input("Num 2 = "))
        res = num_1 - num_2
        print("Result is : ", res)
    else:
        command != "*" or "+" or "-" or "/", print("Pls check yor command ! ")
