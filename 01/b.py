left = []
right = []

for i in range(1000):
    x, y = map(int, input().split())
    left.append(x)
    right.append(y)

score = 0

for i in range(1000):
    count = 0
    for j in range(1000):
        if left[i] == right[j]:
            count += 1
    score += count * left[i]

print(score)