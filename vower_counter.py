
user_input = input("Enter any string: ").lower()

vowel_count = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for char in user_input:
    if char in vowel_count:
        vowel_count[char] += 1
                
for vowel, count in vowel_count.items():
    print(f"{vowel}: {count}")
    