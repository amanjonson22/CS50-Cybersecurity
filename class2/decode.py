from string import ascii_lowercase

number = 21

word = input("Word: ")
key = number

letter = []

letter_ascii_position = []

letter_decoded_position = []

letter_decoded = []

for i in word:
    letter.append(i)

print(letter)

for i in word:
    for j in ascii_lowercase:
        if i == j:
            letter_ascii_position.append(ascii_lowercase.index(j))

print(letter_ascii_position)

for i in range(len(letter_ascii_position)):
    letter_decoded_position.append(letter_ascii_position[i] - key)

print(letter_decoded_position)

for i in range(len(letter_decoded_position)):
    letter_decoded.append(ascii_lowercase[letter_decoded_position[i]])

print(letter_decoded)

for i in range(len(letter_decoded)):
    print(letter_decoded[i], end='')
