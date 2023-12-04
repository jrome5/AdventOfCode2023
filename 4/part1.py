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


if __name__ == '__main__':
    input = readFile()
    #get data into sets
    total_score = 0.0
    for line in input:
        [lhs, rhs] =  line.split(":")
        [winning_numbers_string, number_set_string] = rhs.split("|")
        winning_numbers_list = winning_numbers_string.split(" ")
        number_set_list = number_set_string.split(" ")
        matching_numbers = 0
        for number in number_set_list:
            if number != '':#discard empties
                if number in winning_numbers_list:
                    matching_numbers += 1
        score = np.floor(2 ** (matching_numbers-1))
        total_score += score
    print(total_score)