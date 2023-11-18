t = 0


def setup():
    size(600, 600)
    noStroke()


def draw():
    global t, points
    # amplitudes
    a1, a2 = 100, 200
    # frequencies
    f1, f2 = 1, 2
    # phase shifts
    p1, p2 = 0, PI / 2
    # decay constants
    d1, d2 = 0.02, 0.02
    background(255)
    translate(width / 2, height / 2)
    x = a1 * cos(f1 * t + p1) * exp(-d1 * t)
    y = a2 * cos(f2 * t + p2) * exp(-d2 * t)
    points.append([x, y])

    # draw lines between points in list
    for i, p in enumerate(points):
        stroke(0)
        if i < len(points) - 1:
            line(p[0], p[1], points[i + 1][0], points[i + 1][1])
    t += .1
