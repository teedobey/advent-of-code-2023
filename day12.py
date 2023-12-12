import fileinput
import parse


def main():
    sum = 0
    lines = iter(fileinput.input())
    for line in lines:
        springs = line[:-1].split(" ")[0]
        numbers = line[:-1].split(" ")[1]
        numbers = [int(x) for x in numbers.split(",")]
        springs_len = len(springs)
        score = compute(numbers, springs, "")
        print(f"Score: {score} for {numbers} and {springs}")
        sum += score
    print(sum)


def compute(numbers, springs, acc):
    # print(F"Got {numbers} and {springs}")
    if len(numbers) == 0 and len(springs) == 0:
        # print("END")
        # print(acc)
        return 1
    if len(numbers) == 0 and all([x != "#" for x in springs]):
        # print("END")
        # print(acc)
        return 1
    if len(numbers) == 0:
        # print("BAD")
        return 0
    total = 0
    next_num = numbers[0]
    max_iter = len(springs) - sum(numbers)
    # print(F"max_iter: {max_iter}")
    if max_iter < 0:
        return 0
    for i in range(0, max_iter + 1):
        if is_ok(next_num, i, springs):
            # print(F"OK. Calling compute({numbers[1:]}, {springs[(i+next_num+1):]})")
            if len(springs[(i + next_num) :]) == 0 or springs[i + next_num] != "#":
                total += compute(
                    numbers[1:],
                    springs[(i + next_num + 1) :],
                    acc
                    + "".join(["." for x in range(i)])
                    + "".join(["#" for x in range(next_num)])
                    + ".",
                )

    return total


def is_ok(next_sum, offset, springs):
    #print(f"Checking {next_sum} at {offset} in {springs[offset:offset+next_sum]}")
    for i in range(0, offset):
        if springs[i] == "#":
            return False
    for i in range(0, next_sum):
        if springs[offset + i] == ".":
            return False
    return True


if __name__ == "__main__":
    main()
