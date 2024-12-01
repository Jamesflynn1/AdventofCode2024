
import csv 
from collections import defaultdict
def part_one(csv_file):
    first_list = []
    second_list = []

    for line in csv_file:
        line = line[0].split("   ")
        first_list.append(int(line[0]))
        second_list.append(int(line[1]))
    
    first_list.sort()
    second_list.sort()

    cum_diff = 0
    for x, y in zip(first_list, second_list):
        cum_diff += abs(x-y)

    print(cum_diff)

def part_two(csv_file):
    first_list = []
    second_freqs = defaultdict(int)
    for line in csv_file:
        line = line[0].split("   ")
        second_freqs[int(line[1])] += 1
        
        first_list.append(int(line[0]))
    
    similarity_score = 0
    for x in first_list:
        similarity_score += second_freqs[x]*x

    print(similarity_score)
    
with open("AdventofCode2024/data/day1/day1.csv") as file:
    csv_file = [line for line in csv.reader(file, delimiter=",")]
    part_one(csv_file)
    part_two(csv_file)
