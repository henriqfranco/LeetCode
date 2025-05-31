def mergeAlternately(word1: str, word2: str) -> str:

    merged = []
    current = 1
    A, B = len(word1), len(word2)
    a, b = 0, 0

    while a < A and b < B:
        if current == 1:
            merged.append(word1[a])
            a += 1
            current = 2
        else:
            merged.append(word2[b])
            b += 1
            current = 1

    while a < A:
        merged.append(word1[a])
        a += 1

    while b < B:
        merged.append(word2[b])
        b += 1

    return ''.join(merged)


print(mergeAlternately("abc", "xyz"))