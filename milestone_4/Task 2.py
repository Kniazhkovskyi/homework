def word_frequency(text: str) -> dict:

    import re
    words = re.findall(r'\b\w+\b', text)
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


print(word_frequency("This is a sample text. This text is a good example."))
# Временная сложность: O(n)
