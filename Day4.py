from collections import Counter

with open("input_day4.dat") as file:
    lines = file.read().splitlines()
print(lines)
n_pass = 0
for passfrase in lines:
    counter = Counter(passfrase.split())
    print(counter)
    if any(v > 1 for v in counter.values()):
        pass
    else:
        n_pass += 1
print(n_pass)
