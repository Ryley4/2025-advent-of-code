file = "/Users/ryley/Desktop/local-repo/2025-advent-of-code/day3/input.txt"

with open(file, "r") as f:
    banks = [line.strip() for line in f if line.strip()]

def max_joltage_for_bank(bank: str) -> int:

    bank = bank.strip()
    best = -1

    for i in range(len(bank)):
        a = int(bank[i])
        for j in range(i + 1, len(bank)):
            b = int(bank[j])
            val = 10 * a + b
            if val > best:
                best = val

    return best

total_output = sum(max_joltage_for_bank(bank) for bank in banks)
print(total_output)