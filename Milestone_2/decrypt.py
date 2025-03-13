def decrypt(message: str, key: int) -> str:

    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - key) % 26 + base)
        else:
            result += char
    return result


def main():
    message = input("Enter message:  ")
    key = int(input("Enter key: "))
    decrypted_message = decrypt(message, key)
    print("Result:  ", decrypted_message)


if __name__ == "__main__":
    main()
