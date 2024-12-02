safe = 0

for i in range(1000):

    level = list(map(int, input().split()))

    for i in range(len(level)):
        
        level_copy = level.copy()
        level_copy.pop(i)
        bools = []

        for i in range(len(level_copy) - 1):
            
            if level_copy[i+1] > level_copy[i] and abs(level_copy[i+1] - level_copy[i]) <= 3:
                bools.append(1)
            elif level_copy[i+1] < level_copy[i] and abs(level_copy[i+1] - level_copy[i]) <= 3:
                bools.append(0)
            else:
                bools.append(float('inf'))

        if sum(bools) == 0 or sum(bools) == len(level_copy) - 1:
            safe += 1
            break

print(safe)