import fileinput
import parse


def main():
    lines = iter(fileinput.input())
    time = int(next(lines)[:-1].split(":")[1].replace(" ", ""))
    distance = int(next(lines)[:-1].split(":")[1].replace(" ", ""))
    print(time)
    print(distance)
    sum = 0
    for j in range(1, time):
        if (j * (time - j)) > distance:
            sum += 1
    print(sum)


if __name__ == "__main__":
    main()
