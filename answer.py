
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
    for i in range(len(lines)):
        lines[i] = lines[i].split(" ")
    return lines


def main():
    data = open_file()
    items = parse_items(data)
    print(items)
    #total_items = items[0][0]
    #capacity = items[0][1]
    #find_optimal_subset(items)

if __name__ == "__main__":
    main()