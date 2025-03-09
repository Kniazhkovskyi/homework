from collections import Counter


def is_anagram(s1: str, s2: str) -> bool:

    return Counter(s1) == Counter(s2)


print(Counter("listen"))
print(Counter("silent"))
print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))
