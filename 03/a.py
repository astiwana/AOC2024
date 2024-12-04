import re
import sys

text = ""
for line in sys.stdin:
    text += line

pattern = r"mul\(\d+,\d+\)"

matches = re.findall(pattern, text)
mul = 0

for match in matches:
    _, nums = match.split("(")
    x, y = map(int, nums.strip(")").split(','))
    mul += x * y

print(mul)