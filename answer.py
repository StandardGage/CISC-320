def open_file():
    """Open file from input and return the contents of the file"""
    file_name = input()
    try:
        file = open(file_name, "r")
        return file.read()
    except FileNotFoundError:
        print("File not found")
        return None


def parse_items(data):
    """Parse the data from the file and return the items in a manageable format"""
    lines = data.split("\n")
    lines = [[int(i) for i in line.split()] for line in lines]
    return lines


def approx_tsp(matrix):
    cost = 0
    n = len(matrix[0])
    farthest = find_farthest_vert(matrix)
    visited = [farthest]
    for i in range(n):
        next_visit = find_cheapest_vert(matrix[visited[-1]], visited)
        print(visited[-1])
        cost += matrix[visited[-1]][next_visit]
        visited.append(next_visit)
    print(cost)


def find_cheapest_vert(vertex: list, ignore=[]):
    cost = max(vertex)
    for i in range(len(vertex)):
        if i in ignore:
            continue
        if vertex[i] != 0 and vertex[i] < cost:
            cost = vertex[i]
    return vertex.index(cost)


def find_farthest_vert(matrix):
    farthest = 0
    for i in range(len(matrix)):
        if sum(matrix[i]) > sum(matrix[farthest]):
            farthest = i
    return farthest


def main():
    data = open_file()
    matrix = parse_items(data)
    approx_tsp(matrix)


if __name__ == "__main__":
    main()
