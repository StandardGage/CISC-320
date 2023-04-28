
"""Open file from input and return the contents of the file"""
def open_file():
    file_name = input("Enter file name: ")
    try:
        file = open(file_name, "r")
        return file.read()
    except FileNotFoundError:
        print("File not found")
        return None

"""Parse the data from the file and return the items in a manageable format"""
def parse_items(data):
    lines = data.split("\n")
    lines = [line.split() for line in lines]
    
    total_items = int(lines[0][0])
    capacity = int(lines[1][0])
    
    items = []
    for line in lines[2:]:
        if len(line) == 3:
            items.append([line[0], int(line[1]), int(line[2])])

    return total_items, capacity, items

"""Find the optimal subset of items to take"""
def find_optimal_subset(items, total_items, capacity):
    dp_table = [[0] * (capacity + 1) for _ in range(total_items + 1)]

    for item_index in range(1, total_items + 1):
        item_name, item_weight, item_value = items[item_index - 1]
        for current_capacity in range(1, capacity + 1):
            if item_weight <= current_capacity:
                dp_table[item_index][current_capacity] = max(
                    dp_table[item_index - 1][current_capacity],
                    dp_table[item_index - 1][current_capacity - item_weight] + item_value,
                )
            else:
                dp_table[item_index][current_capacity] = dp_table[item_index - 1][current_capacity]

    optimal_items = []
    item_index, current_capacity = total_items, capacity
    while item_index > 0 and current_capacity > 0:
        if dp_table[item_index][current_capacity] != dp_table[item_index - 1][current_capacity]:
            optimal_items.append(items[item_index - 1])
            current_capacity -= items[item_index - 1][1]
        item_index -= 1
    total_value = sum([item[2] for item in optimal_items])
    return optimal_items[::-1], total_value


def main():
    data = open_file()
    total_items, capacity, items = parse_items(data)
    optimal_items, total_value = find_optimal_subset(items, total_items, capacity)
    [print(item[0]) for item in optimal_items]
    print(total_value)

if __name__ == "__main__":
    main()