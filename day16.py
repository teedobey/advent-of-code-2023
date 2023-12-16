import fileinput
import parse

N = 0
S = 1
E = 2
W = 3

def main():
    total = 0
    lines = iter(fileinput.input())
    map = []
    for line in lines:
        map.append(line[:-1])

    q = []
    visited = set()
    q.append((0,0,E))
    while len(q) > 0:
        cur = q.pop()
        print(F"{cur}")
        visited.add(cur)
        next = evaluate(cur[0], cur[1], cur[2], map)
        q += [n for n in next if not n in visited]    
    visited_cord = set()
    for v in visited:
        visited_cord.add((v[0], v[1]))
    print(F"OK {len(visited_cord)}")


def evaluate(x, y, z, map):
    ret = []
    if map[x][y] == ".":
        ret.append(direction(x, y, z, map))
    if map[x][y] == "/":
        ret.append(direction(x, y, reflect1(z), map))
    if map[x][y] == "\\":
        ret.append(direction(x, y, reflect2(z), map))
    if map[x][y] == "|":
        if z == E or z == W:
            ret.append(direction(x, y, N, map))
            ret.append(direction(x, y, S, map))
        else:
            ret.append(direction(x, y, z, map))
    if map[x][y] == "-":
        if z == N or z == S:
            ret.append(direction(x, y, E, map))
            ret.append(direction(x, y, W, map))
        else:
            ret.append(direction(x, y, z, map))
    return [r for r in ret if r is not None]


def reflect1(z): # /
    if z == N:
        return E
    if z == S:
        return W
    if z == E:
        return N
    if z == W:
        return S
    return ""
    
def reflect2(z): # \
    if z == N:
        return W
    if z == S:
        return E
    if z == E:
        return S
    if z == W:
        return N
    return ""

def direction(x, y, z, map):
    if z == N:
        if x > 0:
            return (x-1, y, z)
        else:
            return None
    if z == S:
        if x < len(map) - 1:
            return (x+1, y, z)
        else:
            return None
    if z == E:
        if y < len(map[x]) - 1:
            return (x, y+1, z)
        else:
            return None
    if z == W:
        if y > 0:
            return (x, y-1, z)
        else:
            return None
    return None

if __name__ == "__main__":
    main()
