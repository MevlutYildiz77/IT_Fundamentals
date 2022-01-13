string = input("Provide a string to search vowels: ")
# Iterate the string
found = []
for letter in string:
    if letter in vowels:
        if letter not in found:
            found.append(letter)






























