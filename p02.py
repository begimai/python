sum = 0
c = 0
with open("test.txt") as f:
    lines = f.readlines()
    for line in lines:
        sum += int(line)
        c += 1
print("Total sum is ", sum)
print("Avg is ", round(sum/c, 2))
print("Number of elements is ", c)