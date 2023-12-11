import fileinput
import parse

def main():
    sum = 0
    lines = iter(fileinput.input())
    vertexes = set()
    line_count = 0
    line_len = 0
    for i, line in enumerate(lines):
        line_count += 1
        line_len = len(line) - 1
        for j, ch in enumerate(line[:-1]):
            if ch == "#":
                vertexes.add((i, j))
    acc_row = 0
    new_vertexes = set()
    for i in range(0, line_count):
        if not any([p[0] == i for p in vertexes]):
            acc_row += 1
        else:
            for v in [p for p in vertexes if p[0] == i]:
                new_vertexes.add((v[0] + acc_row, v[1]))
    vertexes = new_vertexes
   
    new_vertexes = set()
    acc_col = 0
    for j in range(0, line_len):
        if not any([p[1] == j for p in vertexes]):
            acc_col += 1
        else:
            for v in [p for p in vertexes if p[1] == j]:
                new_vertexes.add((v[0], v[1] + acc_col))
    
    print(F"acc_row: {acc_row}; acc_col: {acc_col}")
    vertexes = new_vertexes

    total_distance = 0
    for v in vertexes:
        for v1 in vertexes:
            total_distance += abs(v[0] - v1[0]) + abs(v[1] - v1[1])
                
    print(total_distance // 2)


if __name__ == "__main__":
    main()
