def task_2() -> None:

    n = int(input(("Input your number: ")))
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(factorial)


task_2()
