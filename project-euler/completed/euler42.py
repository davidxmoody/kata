letter_values = {letter: index+1 for index, letter in 
                 enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}

triangle_numbers = [int(n*(n+1)/2) for n in range(100)]

def word_value(word):
    return sum(letter_values[letter] for letter in word)

with open("euler42-words.txt") as words_file:
    words = (word.strip('"') for word in words_file.readline().split(','))

count = 0
for word in words:
    if word_value(word) in triangle_numbers:
        count += 1

print(count)
