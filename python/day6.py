
from file_utils import return_string_list 
from collections import defaultdict
from enum import Enum

import numpy as np

class Direction(Enum):
    NORTH = (-1, 0)
    EAST = (0, 1)
    SOUTH = (1, 0)
    WEST = (0, -1)

def get_next_direction(current_direction):
    current_direction_idx = list(Direction).index(current_direction)
    next_direction_idx = (current_direction_idx + 1) % len(Direction)
    next_direction = list(Direction)[next_direction_idx]
    return next_direction


def rotate_direction(map_list, current_direction, current_coords, call_depth = 0):
    if call_depth > 4:
        return -1
    try:
        next_x = current_coords[0]+current_direction.value[0]
        next_y = current_coords[1]+current_direction.value[1]

        if next_x <0 or next_x >= len(map_list[0]) or next_y <0 or next_y >= len(map_list):
            return None
        next_square = map_list[next_x][next_y]
        
        if next_square == '#':
            next_direction = get_next_direction(current_direction)
            return rotate_direction(map_list, next_direction, current_coords, call_depth+1)
        else:
            return current_direction
    except Exception as e:
       print(e)
       print(f"ENDED AT {current_coords}")
       return None

def move_once(map_list, prev_coords, prev_direction):
    new_dir = rotate_direction(map_list, prev_direction, prev_coords)

    if new_dir is None:
        return None, None
    elif new_dir == -1:
        return -1, -1
    else:
        new_coords = [new_dir.value[0] + prev_coords[0],
                      new_dir.value[1] + prev_coords[1]]
        return new_coords, new_dir

def part_one(csv_file):
    map_list = []
    for line in csv_file:
        map_list.append([char for char in line[0]])
    visted = set([])
    print(map_list)
    start_search = np.where(np.array(map_list) == '^')

    coord = [int(start_search[0]), int(start_search[1])]
    visted.add(f"{coord[0]}, {coord[1]}")
    
    orientation = Direction.NORTH

    while True:
        coord, orientation = move_once(map_list, coord, orientation)
        print(coord, orientation)
        if coord is None:
            break
        else:
            visted.add(f"{coord[0]}, {coord[1]}")
    print(len(visted))

def part_two(csv_file):
    map_list = []
    for line in csv_file:
        map_list.append([char for char in line[0]])
    visted_and_dir = set([])
    print(map_list)
    start_search = np.where(np.array(map_list) == '^')

    coord = [int(start_search[0]), int(start_search[1])]

    orientation = Direction.NORTH
    
    visted_and_dir.add(f"{coord[0]}, {coord[1]}, {orientation}")

    while True:
        test_orientation = orientation
        test_coord = coord.copy()
        while True:
            
            coord, orientation = move_once(map_list, coord, orientation)
        coord, orientation = move_once(map_list, coord, orientation)
        print(coord, orientation)
        if coord is None:
            break
        else:

            visted_and_dir.add(f"{coord[0]}, {coord[1]}")
    print(len(visted))

data_folder = "AdventofCode2024/data"
csv_file = return_string_list(data_folder, "day6", entry_type=str)
part_one(csv_file)
#part_two(csv_file)
