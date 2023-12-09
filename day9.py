import fileinput
import parse

def main():
    sum = 0
    lines = iter(fileinput.input())
    for line in lines:
        nums = [int(x) for x in line[:-1].split(" ")]
        sum += nums[-1]
        while not all([x == 0 for x in nums]):
            new_nums = []
            for i in range(1, len(nums)):
                new_nums.append(nums[i] - nums[i-1])
            sum += new_nums[-1]
            nums = new_nums
    print(sum)

if __name__ == "__main__":
    main()