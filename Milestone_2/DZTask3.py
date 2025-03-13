def task_prime() -> None:

    n = int(input("Введите число: "))

    if n < 2:
        print("false")
        return

    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("true")
    else:
        print("false")


task_prime()
