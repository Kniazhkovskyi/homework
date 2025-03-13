def is_admin(func):
    def wrapper(*args, **kwargs):
        if 'user_type' not in kwargs or not isinstance(kwargs['user_type'], str):
            raise ValueError("user_type is required and must be a string")
        
        if kwargs['user_type'] != 'admin':
            raise ValueError("Permission denied")

        return func(*args, **kwargs)

    return wrapper

@is_admin
def show_customer_receipt(user_type: str):
    print("Showing customer receipt...")

# Проверка
show_customer_receipt(user_type='user')  # Ошибка: Permission denied
show_customer_receipt(user_type='admin')  # Выведет: Showing customer receipt...