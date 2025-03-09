def encrypt(message: str, key: int) -> str:

    result = ""
    for char in message:
        if char.isalpha():

            base = ord('A') if char.isupper() else ord('a')

            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char
    return result


def main():
    message = input("Enter message: ")
    key = int(input("Enter key: "))
    encrypted_message = encrypt(message, key)
    print("Result:", encrypted_message)


if __name__ == "__main__":
    main()
