import argparse
import fileinput
import parse
import copy

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
    args = parser.parse_args()
    sum = 0
    lines = iter(fileinput.input(files=(args.input)))
    map = []
    edges = {}
    start = (-1, -1)
    for line in lines:
        map.append([ch for ch in line[:-1]])
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if map[i][j] == "S":
                start = (i, j)
                map[i][j] = replace_s(map, i, j)

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
    print(F"Max distance = {max_distance}")
    print(F"Pipes visited: {len(visited)}")

    loop_x_counts = copy.deepcopy(map)
    loop_y_counts = copy.deepcopy(map)
    # populate loop_x_counts
    first_turn = ""
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            loop_x_counts[i][j] = 0 if j == 0 else loop_x_counts[i][j-1]
            if (i, j) in visited:
                if map[i][j] == "|":
                    loop_x_counts[i][j] +=1
                    first_turn = ""
                elif map[i][j] == "-":
                    pass
                else:
                    if map[i][j] == "L" or map[i][j] == "F":
                        first_turn = map[i][j]
                    elif map[i][j] == "J" and first_turn == "F":
                        loop_x_counts[i][j] += 1
                        first_turn = ""
                    elif map[i][j] == "7" and first_turn == "L":
                        loop_x_counts[i][j] += 1
                        first_turn = ""                                      

    # populate loop_y_counts
    first_turn = ""
    for j in range(0, len(map[0])):
        for i in range(0, len(map)):
            loop_y_counts[i][j] = 0 if i == 0 else loop_y_counts[i-1][j]
            if (i, j) in visited:
                if map[i][j] == "-":
                    loop_y_counts[i][j] +=1
                    first_turn = ""
                elif map[i][j] == "|":
                    pass
                else:
                    if map[i][j] == "F" or map[i][j] == "7":
                        first_turn = map[i][j]
                    elif map[i][j] == "J" and first_turn == "F":
                        loop_y_counts[i][j] += 1
                        first_turn = ""
                    elif map[i][j] == "L" and first_turn == "7":
                        loop_y_counts[i][j] += 1
                        first_turn = ""
    area = 0
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if not (i, j) in visited:
                if loop_y_counts[i][j] % 2 == 1 and loop_x_counts[i][j] % 2 == 1:
                    area += 1
    print(F"Area inside the main loop: {area}")
    if args.html != "":
        visualize(map, visited, loop_x_counts, loop_y_counts, args.html)


def replace_s(map, i, j):
    north_ok = False
    south_ok = False
    east_ok = False
    west_ok = False
    if i > 0:
        north_ok = map[i-1][j] in north_connections["S"]
    if i < len(map) - 1:
        south_ok = map[i+1][j] in south_connections["S"]
    if j > 0:
        west_ok = map[i][j-1] in west_connections["S"]
    if j < len(map[i]) - 1:
        east_ok = map[i][j+1] in east_connections["S"]
    if north_ok and south_ok:
        return "|"
    if north_ok and east_ok:
        return "L"
    if north_ok and west_ok:
        return "J"
    if south_ok and east_ok:
        return "F"
    if south_ok and west_ok:
        return "7"
    if east_ok and west_ok:
        return "-"
    raise ValueError("Unexpected state when replacing S " + str(i) + ", " + str(j))


unicode_mapping = {
    "F": "&#9487;",
    "7": "&#9491;",
    "L": "&#9495;",
    "J": "&#9499;",
    "|": "&#9475;",
    "-": "&#9473;",
    ".": "&nbsp;"
}

def visualize(map, visited, loop_x_counts, loop_y_counts, output_html):
    with open(output_html, "w") as output:
        output.write("<html><head><title>visualization</title></head>\n")
        output.write("<body style=\"background-color:black; color:white\">\n")
        output.write("<span style=\"font-family:monospace\">\n")
        for i in range(0, len(map)):
            for j in range(0, len(map[i])):
                if (i, j) in visited:
                    output.write("<span style=\"color:red; background-color:#220000;\">" + unicode_mapping[map[i][j]] + "</span>")
                elif loop_x_counts[i][j] % 2 == 1 and loop_y_counts[i][j] % 2 == 1:
                    output.write("<span style=\"color:yellow; background-color:#00AAAA;\">" + unicode_mapping[map[i][j]] + "</span>")
                else:
                    output.write(unicode_mapping[map[i][j]])
            output.write("<br/>\n")
        output.write("</span></body></html>\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Solve the Advent of Code 2013 day 10 puzzle. (2)')
    parser.add_argument("input", help="The input file")
    parser.add_argument('--html', help="Output file for html visualization", default="")
    main()

