from collections import Counter
import sys

# Read canvas size.
width, height = map(int, input().split())
canvas = {}

# Draw rectangles
colors = {0}
for line in sys.stdin.readlines():
    color, x0, y0, w, h = map(int, line.split)
    colors.add(color)
    for x in range(x0, x0 + w):
        for y in range(y0, y0 + h):
            canvas[x,y] = color


# Count areas.
count = Counter()
for x in range(width):
    for y in range(height):
        color = canvas.get((x,y),0)
        count[color] += 1

for k, v in sorted(count.items()):
    print(k,v)