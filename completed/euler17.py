#!/usr/bin/env python3

numbers = {  1 : 'one',
             2 : 'two',
             3 : 'three',
             4 : 'four',
             5 : 'five',
             6 : 'six',
             7 : 'seven',
             8 : 'eight',
             9 : 'nine',
            10 : 'ten', 
            11 : 'eleven',
            12 : 'twelve',
            13 : 'thirteen',
            14 : 'fourteen',
            15 : 'fifteen',
            16 : 'sixteen',
            17 : 'seventeen',
            18 : 'eighteen',
            19 : 'nineteen',
            20 : 'twenty',
            30 : 'thirty',
            40 : 'forty',
            50 : 'fifty',
            60 : 'sixty',
            70 : 'seventy',
            80 : 'eighty',
            90 : 'ninety'
          }

def in_words(n):
    if n==1000: return 'one thousand'

    words = ''
    hundreds = n//100
    tens = n%100

    if hundreds in numbers:
        words += numbers[hundreds] + ' hundred'

    if len(words)>0 and tens>0:
        words += ' and '

    if tens in numbers:
        words += numbers[tens]
    elif (tens//10)*10 in numbers:
        words += numbers[(tens//10)*10] + ' ' + numbers[tens%10]
    
    return words


print(sum( len(in_words(i).replace(' ', '')) for i in range(1, 1001) ))
