import fileinput
import parse


def main():
    total = 0
    lines = iter(fileinput.input())
    map = []
    for line in lines:
        map.append(line[:-1])

    for i in range(0 , len(map[0])):
        min_j = 0
        for j in range(0, len(map)):
            if map[j][i] == "#":
                min_j = j + 1
            elif map[j][i] == "O":
                total += len(map) - min_j
                min_j += 1
    print(total)

if __name__ == '__main__':
    main()