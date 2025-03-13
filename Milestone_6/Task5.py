import time

def rate_limiter(calls_per_minute):
    interval = 60.0 / calls_per_minute
    call_times = []
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_time = time.time()

            while call_times and call_times[0] < current_time - 60:
                call_times.pop(0)

            if len(call_times) >= calls_per_minute:
                print("Rate limit exceeded. Try again later.")
                return None

            call_times.append(current_time)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@rate_limiter(3)  # Максимум 3 вызова в минуту
def my_function():
    print("Function executed!")

my_function()  # Выполнится
my_function()  # Выполнится
my_function()  # Выполнится
my_function()  # Должно заблокироваться