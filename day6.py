import fileinput
import parse

def main():
    prod = 1
    lines = iter(fileinput.input())
    times = [int(x) for x in next(lines)[:-1].split(":")[1].split(" ") if x != ""]
    distances = [int(x) for x in next(lines)[:-1].split(":")[1].split(" ") if x != ""]
    print(times)
    print(distances)
    for i in range(0, len(times)):
        sum =  0
        for j in range(1, times[i]):
            if (j * (times[i] - j)) > distances[i]:
                sum += 1
        prod *= sum
    print(prod)

if __name__ == '__main__':
    main()    