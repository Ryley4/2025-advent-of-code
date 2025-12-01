
file = "/Users/ryley/Desktop/local-repo/2025-advent-of-code/day1/input.txt"

position = 50
zero_counter = 0

with open(file, "r") as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue

        direction = line[0]
        steps = int(line[1:])

        if direction == 'R':
            position = (position + steps) % 100
        elif direction =='L':
            position = (position - steps) % 100

        if position == 0:
            zero_counter += 1

print("Password: ", zero_counter)