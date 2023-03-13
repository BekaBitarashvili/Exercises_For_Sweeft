# Exercise N1
words = {}
unique_words = 0

print("please select any five words...")
first = input("first word: ")
second = input("second word: ")
third = input("third word: ")
fourth = input("fourth word: ")
fifth = input("fifth word: ")

for word in [first, second, third, fourth, fifth]:
    if word not in words:
        words[word] = 1
        unique_words += 1
    else:
        words[word] += 1

print("different words:", unique_words)

print("words:")
for word, count in words.items():
    print(word, count)

# Exercise N2