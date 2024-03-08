from math import cos, pi, sin

xs = []
n = -pi
while True:
    xs.append(n)
    n += 0.001
    if n > pi:
        break

h = 0.001

ys = []
cosy = []
for x in xs:
    y = (sin(x + h) - sin(x)) / h
    ys.append(y)
    cosy.append(cos(x))

for i in range(len(xs)):
    print(f"{xs[i]}: {ys[i]}, {cosy[i]}")
    if i > 10:
        break  # only print the first 10
