import inspect

def check_types(func):
    annotations = func.__annotations__

    def wrapper(*args, **kwargs):
        bound_args = inspect.signature(func).bind(*args, **kwargs)
        bound_args.apply_defaults()

        for arg_name, arg_value in bound_args.arguments.items():
            if arg_name in annotations:
                expected_type = annotations[arg_name]
                if not isinstance(arg_value, expected_type):
                    raise TypeError(f"Argument {arg_name} must be {expected_type.__name__}, not {type(arg_value).__name__}")

        result = func(*args, **kwargs)

        if "return" in annotations:
            expected_return_type = annotations["return"]
            if not isinstance(result, expected_return_type):
                raise TypeError(f"Return value must be {expected_return_type.__name__}, not {type(result).__name__}")

        return result

    return wrapper

@check_types
def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2))  # 3

try:
    print(add("1", "2"))  # Ошибка
except TypeError as e:
    print(f"Ошибка: {e}")