left = []
right = []

for i in range(1000):
    x, y = map(int, input().split())
    left.append(x)
    right.append(y)

left.sort()
right.sort()

diff = 0

for i in range(1000):
    if right[i] > left[i]:
        diff += right[i] - left[i]
    else:
        diff += left[i] - right[i]
        
print(diff)