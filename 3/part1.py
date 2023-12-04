import csv
import pathlib
import os
import numpy as np

def readFile():
    values_list = []
    filepath = pathlib.Path(__file__).parent.absolute()
    with open(os.path.join(filepath, 'input.csv')) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\r')
        line_count = 0
        for row in csv_reader:
            values_list.append(row[0])
            line_count += 1
        print(f'Processed {line_count} lines.')
    return values_list

def is_number(n):
    try:
        float(n)   # Type-casting the string to `float`.
                   # If string is not a valid `float`, 
                   # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True

'''
numbers are counted only if next to a symbol (not a .)
even diagonally
therefore, search for numbers, check left, right, above and below (+/-1)
'''
if __name__ == '__main__':
    input = readFile()
    numbers_list = []
    symbols_list = []
    for line in input:
        #get numbers
        numbers = {}
        symbols = {}
        digits = []
        for i, c in enumerate(line):
            if(is_number(c)):
                digits.append(c)
            else:
                if(len(digits) > 0): #concatenate digits into single number
                    number = ''.join(digits)
                    numbers[i-1] = number #number ended on previous char
                    digits = []
                # if(c != '.'):
                if(ord(c) != 46):
                    symbols[i] = c
        numbers_list.append(numbers)
        symbols_list.append(symbols)

    part_numbers = []
    #iterate and check symbols
    for i,numbers_dict in enumerate(numbers_list):
        #get prev, current, and next symbol dicts
        prev_line_symbols = {}
        current_line_symbols = symbols_list[i]
        next_line_symbols = {}
        if(i != 0):
            prev_line_symbols = symbols_list[i-1]
        if((i+1) < len(symbols_list)):
            next_line_symbols = symbols_list[i+1]

        #search for symbols
        for placement, number in numbers_dict.items():
            end_index = placement +1
            start_index = placement - (len(number) - 1)
            #check horizontally above, current, and below
            for j in range(start_index-1, end_index+1, 1):#indexing to either side of number
                if(j in prev_line_symbols.keys()):
                    part_numbers.append(int(number))
                    break
                elif(j in current_line_symbols.keys()):
                    part_numbers.append(int(number))
                    break
                elif(j in next_line_symbols.keys()):
                    part_numbers.append(int(number))
                    break
    print(np.sum(part_numbers))
    print(np.max(part_numbers))