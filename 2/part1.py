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
    sum = 0
    max_red = 12
    max_green = 13
    max_blue = 14

    for line in input:
        #1. get game numbers
        [lhs, rhs] =  line.split(":")
        game_number = lhs[5:] #assume 5 characters before game number
        #2. sort into sets by semi colon
        sets = rhs.split(";")
        #3. sort into colours by commas
        reds = []
        blues = []
        greens = []
        for set in sets:
            pairings = set.split(",")
            #4. sort into value, colour by space
            for pair in pairings:
                [value, colour] = pair.strip().split(" ")
                value = int(value)
                if(colour == "red"):
                    reds.append(value)
                elif(colour == "blue"):
                    blues.append(value)
                elif(colour == "green"):
                    greens.append(value)
                else:
                    assert colour != "green" and colour != "blue" and colour != "red"
        #5. check values and fail if too high, otherwise add game number to total
        if(np.max(reds) <= max_red):
            if(np.max(blues) <= max_blue):
                if(np.max(greens) <= max_green):
                    sum += int(game_number)

    print(sum)