def count_vowels(message):
    vowels = "aeiouAEIOU"
    count = 0
    for char in message:
        if char in vowels:
            count += 1
    return count
print(count_vowels("Hello, World!"))