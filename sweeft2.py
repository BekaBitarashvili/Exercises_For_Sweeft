def bigger_is_greater(w):
    n = len(w)
    i = n - 2
    while i >= 0 and w[i] >= w[i+1]:
        i -= 1
    if i < 0:
        return "no answer"

    j = n - 1
    while j > i and w[j] <= w[i]:
        j -= 1

    w = list(w)
    w[i], w[j] = w[j], w[i]

    w[i+1:] = sorted(w[i+1:])
    return "".join(w)

print(bigger_is_greater("beka"))
print(bigger_is_greater("ana"))
print(bigger_is_greater("sweeft"))
print(bigger_is_greater("python"))
print(bigger_is_greater("abcdefghijklmn"))
print(bigger_is_greater("wxzy"))
print(bigger_is_greater("aaa"))
print(bigger_is_greater("xxx"))
print(bigger_is_greater("123"))