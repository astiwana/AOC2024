safe = 0

for i in range(1000):

    level = list(map(int, input().split()))
    bools = []

    for i in range(len(level) - 1):
        
        if level[i+1] > level[i] and abs(level[i+1] - level[i]) <= 3:
            bools.append(1)
        elif level[i+1] < level[i] and abs(level[i+1] - level[i]) <= 3:
            bools.append(0)
        else:
            bools.append(float('inf'))
    
    if sum(bools) == 0 or sum(bools) == len(level) - 1:
            safe += 1

print(safe)