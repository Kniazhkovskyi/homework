def task_1() -> None:

    number = input("Input your number: ")
    result = sum(int(digit) for digit in number)
    print(result)


task_1()
