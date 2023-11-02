def test_cal_if():
    print("Your command is ?")
    command = input()
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
