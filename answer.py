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


def approx_tsp_cheap(matrix):
    path = []

    cost = 0
    n = len(matrix[0])
    farthest = find_farthest_vert(matrix)
    visited = [farthest]
    for i in range(n):
        next_visit = find_cheapest_vert(matrix[visited[-1]], visited)
        cost += matrix[visited[-1]][next_visit]
        visited.append(next_visit)
    cost += matrix[farthest][visited[-1]]
    path.extend(visited)
    result = path
    result.append(cost)
    return result


def approx_tsp_cheap_and_far(matrix):
    paths = []
    costs = []
    n = len(matrix[0])
    for j in range(n):
        cost = 0
        visited = [j]

        for i in range(int(n/2)):
            next_visit = find_cheapest_vert(matrix[visited[-1]], visited)
            cost += matrix[visited[-1]][next_visit]
            visited.append(next_visit)
            next_visit = find_farthest_vert(matrix, visited)
            if next_visit == None:
                continue
            cost += matrix[visited[-1]][next_visit]
            visited.append(next_visit)
        cost += matrix[j][visited[-1]]
        paths.append(visited)
        costs.append(cost)
    min_cost = min(costs)
    min_path = paths[costs.index(min_cost)]
    result = min_path
    result.append(min_cost)
    return result


def find_cheapest_vert(vertex: list, ignore):
    cost = max(vertex)
    index = vertex.index(0)
    for i in range(len(vertex)):
        if i in ignore:
            continue
        if vertex[i] != 0 and vertex[i] <= cost:
            cost = vertex[i]
            index = i
    return index


def find_farthest_vert(matrix, ignore=[]):
    farthest = None
    for i in range(len(matrix)):
        if i in ignore:
            continue
        if farthest is None:
            farthest = i
        if sum(matrix[i]) > sum(matrix[farthest]):
            farthest = i
    return farthest


def main():
    data = open_file()
    matrix = parse_items(data)
    cheap = approx_tsp_cheap(matrix)
    cheap_and_far = approx_tsp_cheap_and_far(matrix)
    if cheap[-1] < cheap_and_far[-1]:
        [print(vert) for vert in cheap]
    else:
        [print(vert) for vert in cheap_and_far]


if __name__ == "__main__":
    main()
