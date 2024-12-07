import csv

def return_string_list(data_folder, day, file_name=None, entry_type=str,
                       delimiter = " ", ignore_empty=False):
    if file_name is None:
        file_name = f"{day}.csv"
    
    with open(f"{data_folder}/{day}/{file_name}") as file:
        csv_file = []
        for line in csv.reader(file, delimiter=delimiter):
            csv_file.append([entry_type(entry) for entry in line if (len(entry) > 0 or ignore_empty)])
        return csv_file
    return None
