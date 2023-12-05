import fileinput
import parse

def main():
    sum = 0
    lines = iter(fileinput.input())
    first_line = next(lines)
    seeds_input = [int(x) for x in first_line[7:].split(" ")]
    seeds = []
    for i, seed_input in enumerate(seeds_input):
        if i % 2 == 0:
            seed_start = seed_input
        else:
            seed_end = seed_input
            seeds.append([[seed_start, seed_end + seed_start - 1], False])
    new_seeds = seeds
    for line in lines:
        line = line[:-1] # remove \n
        seeds = new_seeds
        print(seeds)
        print(line)
        if len(line) == 0 or line.endswith("map:"):
            # if not seeds_done, it will map to itself, so no-op.                        
            new_seeds = [[range, False] for [range, done] in seeds]
            continue # skip descriptions        
        new_seeds = []
        map = [int(x) for x in line.split(" ")]
        print(seeds)
        for i, seed in enumerate(seeds):
            if seed[1]: # already done
                new_seeds.append(seed)
                continue
            range_intersect = intersect(seed[0], [map[1], map[1] + map[2] - 1])
            remainder_ranges = difference(seed[0], range_intersect)
            print(range_intersect)
            if range_intersect is not None:
                for r in remainder_ranges:
                    new_seeds.append([r, False])
                new_seeds.append([[map[0] + range_intersect[0] - map[1], map[0] + range_intersect[1] - map[1]], True])
            else:
                new_seeds.append(seed)
    print(min(seeds))
            
def intersect(p1, p2):
    if p1[0] > p2[1] or p1[1] < p2[0]:
        return None
    return [max(p1[0], p2[0]), min(p1[1], p2[1])]

def difference(p1, p2):
    if p2 is None:
        return [p1] # no intersection
    if p1[0] > p2[1] or p1[1] < p2[0]:
        return [p1] # no intersection
    res = []
    if p1[0] < p2[0]:
        res += [[p1[0], p2[0]-1]]
    if p1[1] > p2[1]:
        res += [[p2[1]+1, p1[1]]]
    return res

if __name__ == '__main__':
    main()