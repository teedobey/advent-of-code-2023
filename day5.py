import fileinput
import parse

def main():
    sum = 0
    lines = iter(fileinput.input())
    first_line = next(lines)
    seeds = [int(x) for x in first_line[7:].split(" ")]
    seeds_done = [False for x in seeds]
    for line in lines:
        line = line[:-1] # remove \n
        print(line)
        if len(line) == 0 or line.endswith("map:"):
            # if not seeds_done, it will map to itself, so no-op.
            print(seeds)
            seeds_done = [False for x in seeds]            
            continue # skip descriptions        
        map = [int(x) for x in line.split(" ")]
        for i, seed in enumerate(seeds):
            if not seeds_done[i] and seed >= map[1] and seed < map[1] + map[2]:
                seeds[i] = map[0] + (seed - map[1])
                seeds_done[i] = True
    print(min(seeds))
            
if __name__ == '__main__':
    main()