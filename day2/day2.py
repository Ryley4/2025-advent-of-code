
file = "/Users/ryley/Desktop/local-repo/2025-advent-of-code/day2/input.txt"

def read_puzzle_input(file):
    with open(file, "r") as f:
        return f.read().strip()

def parse_ranges(s):
    ranges = []
    for part in s.split(","):
        start, end = part.split("-")
        ranges.append((int(start), int(end)))
    
    return ranges

def is_invalid_id(n):
    s = str(n)

    if len(s) % 2 == 1:
        return False
    
    half = len(s) // 2
    first = s[:half]
    second = s[half:]

    return first == second

def sum_invalid_ids(ranges):
    total = 0
    count = 0

    for start, end in ranges:
        for n in range(start, end + 1):
            if is_invalid_id(n):
                total += n
                count += 1

    return total, count

if __name__ == "__main__":
    puzzle_input = read_puzzle_input(file)

    ranges = parse_ranges(puzzle_input)
    total, count = sum_invalid_ids(ranges)

    print("\n")
    print("Number of invalid IDs: ", count)
    print("Sum of invalid IDs: ", total)
    print("\n")