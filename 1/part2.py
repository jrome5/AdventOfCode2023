import csv
import pathlib
import os
import collections

def check_for_numbers(line):
    values = {}
    numbers = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    #check for word numbers
    for i,n in enumerate(numbers):
        try:
            occurances = [k for k in range(len(line)) if line.startswith(n, k)]
            for o in occurances:
                values[o] = i
        except ValueError:
            continue
    #check for char numbers
    for i,c in enumerate(line):
        if(is_number(c)):
            values[i] = int(c)
    #sort list
    try:
        # sorted_dict = {k: v for k, v in sorted(values.items(), key=lambda item: item[1])}
        od = collections.OrderedDict(sorted(values.items()))
        return list(od.values())
    except ValueError:
        return [0,0]
    
def is_number(n):
    try:
        float(n)   # Type-casting the string to `float`.
                   # If string is not a valid `float`, 
                   # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True

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


if __name__ == '__main__':
    input = readFile()
    sum = 0
    for line in input:
        digits = check_for_numbers(line)
        value = int(str(digits[0]) + str(digits[-1]))
        sum += value
    print(sum)
