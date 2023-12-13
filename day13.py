import fileinput
import parse


def main():
    total = 0
    lines = iter(fileinput.input())
    map = []
    maps = []
    numsx = []
    for line in lines:
        if len(line[:-1]) == 0:
            maps.append(map)
            map = []
        else:
            map.append(line[:-1])
    for map in maps:
        (listx, listy) = count_reflections(map)
        print(F"{listx} {listy}")
        if len(listx) > 0 and len(listy) > 0:
            minx = min(listx)
            miny = min(listy)
            if minx < miny:
                total += minx*100
            else:
                total += miny
        else:
            if len(listx) > 0:
                total += min(listx) * 100
            else: 
                total += min(listy)        
    print(total)


def count_reflections(map):
    retx = []
    rety = []
    numsx = []
    for i in range(0, len(map)):
        numx = decode(map[i])
        numsx.append(numx)
    numsy = []
    for j in range(0, len(map[0])):
        numy = decode([map[i][j] for i in range(0, len(map))])
        numsy.append(numy)

    for i in range(1, len(numsx)):
        part_a = numsx[:i]
        part_b = numsx[i:]
        if len(part_a) < len(part_b):
            part_b = part_b[: len(part_a)]
        else:
            part_a = part_a[-len(part_b) :]
        part_a.reverse()
        #diff = set(part_a).symmetric_difference(set(part_b))
        #diff = list(diff)
        #if len(diff) == 2:
        #    if is_pow2(diff[0] ^ diff[1]):
        #        retx.append(i)
        #        break
        if part_a == part_b:
            retx.append(i)
    for i in range(1, len(numsy)):
        part_a = numsy[:i]
        part_b = numsy[i:]
        if len(part_a) < len(part_b):
            part_b = part_b[: len(part_a)]
        else:
            part_a = part_a[-len(part_b) :]
        part_a.reverse()
        #diff = set(part_a).symmetric_difference(set(part_b))
        #diff = list(diff)
        #if len(diff) == 2:
        #    if is_pow2(diff[0] ^ diff[1]):
        #        retx.append(i)
        #        break        
        if part_a == part_b:
            rety.append(i)
    return (retx, rety)


def decode(s):
    ret = 0
    for c in s:
        if c == "#":
            ret = ret + 1
        ret = ret << 1
    return ret

def is_pow2(x):
    return (x & (x - 1)) == 0

if __name__ == "__main__":
    main()
