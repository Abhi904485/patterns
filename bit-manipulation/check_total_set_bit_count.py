number = 2
count = 0
for i in range(32):
    if (number & (1 << i)) != 0:
        count += 1
print(count)