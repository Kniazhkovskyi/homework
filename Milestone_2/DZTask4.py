def task_4() -> None:

    number = int(input("Input your number: "))

    a, b = 0, 1
    fib_seq = []

    for _ in range(number):
        fib_seq.append(a)
        a, b = b, a + b

    print(", ".join(map(str, fib_seq)))


task_4()
