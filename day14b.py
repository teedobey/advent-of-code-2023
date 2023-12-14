import fileinput
import parse
import copy

memo = {}
memo2 = {}

def main():
    total = 0
    lines = iter(fileinput.input())
    map = []
    for line in lines:
        map.append([ch for ch in line[:-1]])
    print()
    row_len = len(map[0])

    #m_print(map)
    #print()
    #print(m_key(map))
    #m_print(m_decode(m_key(map), row_len))

    for idx in range(0, 1000000000):
        old_map = copy.deepcopy(map)
        print(F"{idx} {len(memo)}")
        if m_key(old_map) in memo:
            map = m_decode(memo[m_key(old_map)], row_len)
            print(F"{memo2[m_key(old_map)]}")
        else:    
            for i in range(0 , len(map[0])):
                min_j = 0
                for j in range(0, len(map)):
                    if map[j][i] == "#":
                        min_j = j + 1
                    elif map[j][i] == "O":
                        #total += len(map) - min_j
                        if j != min_j:
                            map[min_j][i] = "O"
                            map[j][i] = "."
                        min_j += 1

            for i in range(0, len(map)):
                min_j = 0
                for j in range(0, len(map[i])):
                    if map[i][j] == "#":
                        min_j = j + 1
                    elif map[i][j] == "O":
                        if j != min_j:
                            map[i][min_j] = "O"
                            map[i][j] = "."
                        min_j += 1

            for i in range(0, len(map[0])):
                max_j = len(map) - 1
                for j in reversed(range(0, len(map))):
                    if map[j][i] == "#":
                        max_j = j - 1
                    elif map[j][i] == "O":
                        if j != max_j:
                            map[max_j][i] = "O"
                            map[j][i] = "."
                        max_j -= 1
            
            for i in range(0, len(map)):
                max_j = len(map[i]) - 1
                for j in reversed(range(0, len(map[i]))):
                    if map[i][j] == "#":
                        max_j = j - 1
                    elif map[i][j] == "O":
                        if j != max_j:
                            map[i][max_j] = "O"
                            map[i][j] = "."
                        max_j -= 1
            memo[m_key(old_map)] = m_key(map)            

            total = 0
            for i in range(0 , len(map[0])):
                for j in range(0, len(map)):
                    if map[j][i] == "O":
                        total += len(map) - j
            memo2[m_key(old_map)] = total
            print(total)

        if idx % 10000 == 0:
            print(F" {idx} {total}")
    print(total)

def m_print(m):
    for line in m:
        print("".join(line))

def m_key(m):
    ret = ""
    for line in m:
        ret += "".join(line)
    return ret

def m_decode(m_key, row_len):
    map = []
    for i in range(0, len(m_key), row_len):
        map.append([ch for ch in m_key[i:i+row_len]])
    return map
    
if __name__ == '__main__':
    main()