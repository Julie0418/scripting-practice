
paragragh = input("Enter the paragraph: ").lower()

words = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in paragragh).split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word Frequency:")

for word, frequency in word_count.items():
    print(f"{word}: {frequency}")

