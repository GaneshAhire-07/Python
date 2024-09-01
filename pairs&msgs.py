# Part 1: Finding pairs whose product is 1947

# Function to find pairs whose product is 1947
def find_pairs(product):
    pairs = []
    for i in range(1, int(product**0.5) + 1):
        if product % i == 0:
            pairs.append([i, product // i])
    return pairs

# Get pairs for product 1947
product = 1947
pairs = find_pairs(product)
print("Pairs whose product is 1947:", pairs)

# Part 2: Looping through range M to N and printing messages based on conditions

# Reading M and N from the user
M = int(input("Enter the value of M: "))
N = int(input("Enter the value of N: "))

# Counters for each message type
starks_count = 0
lannisters_count = 0
tullies_count = 0

# Looping from M to N (including N)
for i in range(M, N + 1):
    if (i + 1) % 3 == 0 and (i - 1) % 4 == 0:
        print("Starks")
        starks_count += 1
    elif (i + 1) % 2 == 0 and (i - 1) % 5 == 0:
        print("Lannisters")
        lannisters_count += 1
    else:
        print("Tullies")
        tullies_count += 1

# Printing the counts for each message type
print(f"Starks count: {starks_count}")
print(f"Lannisters count: {lannisters_count}")
print(f"Tullies count: {tullies_count}")
