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


def find_matching(input):
    card_count_dict = {}
    no_matching_numbers_dict = {}
    for i in range(len(input)):
        line = input[i]
        [lhs, rhs] =  line.split(":")
        [winning_numbers_string, number_set_string] = rhs.split("|")
        winning_numbers_list = winning_numbers_string.split(" ")
        number_set_list = number_set_string.split(" ")
        matching_numbers = 0
        for number in number_set_list:
            if number != '':#discard empties
                if number in winning_numbers_list:
                    matching_numbers += 1
        card_no = i + 1
        card_count_dict[card_no] = 1
        no_matching_numbers_dict[card_no] = matching_numbers
    print(card_count_dict)
    print(no_matching_numbers_dict)
    for card, no_matching in no_matching_numbers_dict.items():
        for i in range(no_matching):
            card_count_dict[card+i+1] += card_count_dict[card]
    
    total = 0
    for card, count in card_count_dict.items():
        total += count
    return total


if __name__ == '__main__':
    input = readFile()
    #get data into sets
    scratch_cards = find_matching(input)
    print(scratch_cards)