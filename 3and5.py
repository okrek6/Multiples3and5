total = 0

for i in range(0,10):
    if i % 3 == 0 or i % 5 == 0:
        total = total + i
    print(total)
