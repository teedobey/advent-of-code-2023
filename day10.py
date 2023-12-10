import fileinput
import parse

north_connections = {"|": ["|", "F", "7"], 
                     "F": [],
                     "7": [],
                     "J": ["|", "F", "7"],
                     "." : [],
                     "-": [],
                     "L": ["|", "F", "7"],
                     "S": ["|", "F", "7"]}

south_connections = {"|": ["|", "L", "J"],
                     "F": ["|", "L", "J"],
                     "7": ["|", "L", "J"],
                     "S": ["|", "L", "J"],
                     "J": [],
                     "L": [],
                     ".": [],
                     "-": []}

east_connections = {"|": [],
                    "F": ["-", "7", "J"],
                    "S": ["-", "7", "J"],
                    "7": [],
                    "L": ["-", "7", "J"],
                    "-": ["-", "7", "J"],
                    "J": [],
                    ".": []}

west_connections = {"|": [],
                    "F": [],
                    "L": [],
                    "7": ["-", "F", "L"],
                    "J": ["-", "F", "L"],
                    "S": ["-", "F", "L"],
                    ".": [],
                    "-": ["-", "F", "L"]}

def main():
    sum = 0
    lines = iter(fileinput.input())
    map = []
    edges = {}
    start = (-1, -1)
    for line in lines:
        map.append([ch for ch in line[:-1]])
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if map[i][j] == "S":
                start = (i, j)
    visited = set()
    queue = [(start, 0)]
    max_distance = 0
    while len(queue) > 0:
        node = queue.pop(0)
        if node[0] in visited:
            continue
        visited.add(node[0])
        if node[1] > max_distance:
            max_distance = node[1]
        pipe_type = map[node[0][0]][node[0][1]]
        distance = node[1]
        if node[0][0] > 0:
            north = map[node[0][0]-1][node[0][1]]
            if north in north_connections[pipe_type]:
                queue.append(((node[0][0]-1, node[0][1]), distance + 1))
        if node[0][0] < len(map) - 1:
            south = map[node[0][0]+1][node[0][1]]
            if south in south_connections[pipe_type]:
                queue.append(((node[0][0]+1, node[0][1]), distance + 1))
        if node[0][1] > 0:
            west = map[node[0][0]][node[0][1]-1]
            if west in west_connections[pipe_type]:
                queue.append(((node[0][0], node[0][1] - 1), distance + 1))
        if node[0][1] < len(map[node[0][0]]) - 1:
            east = map[node[0][0]][node[0][1]+1]
            if east in east_connections[pipe_type]:
                queue.append(((node[0][0], node[0][1] + 1), distance + 1))
    print(max_distance)

if __name__ == "__main__":
    main()

