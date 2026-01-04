import matplotlib.pyplot as plt
import math


def draw_square(x, y, size, angle):
    angles = [
        angle,
        angle + math.pi / 2,
        angle + math.pi,
        angle + 3 * math.pi / 2,
        angle
    ]

    xs = [x + size * math.cos(a) for a in angles]
    ys = [y + size * math.sin(a) for a in angles]

    plt.plot(xs, ys, color="darkred")


def pythagoras_tree(x, y, size, angle, level):
    if level == 0:
        return

    draw_square(x, y, size, angle)

    x_top = x + size * math.cos(angle)
    y_top = y + size * math.sin(angle)

    left_angle = angle + math.pi / 4
    right_angle = angle - math.pi / 4

    new_size = size * math.sqrt(2) / 2

    pythagoras_tree(
        x_top,
        y_top,
        new_size,
        left_angle,
        level - 1
    )

    pythagoras_tree(
        x_top + new_size * math.cos(left_angle),
        y_top + new_size * math.sin(left_angle),
        new_size,
        right_angle,
        level - 1
    )


def main():
    level = int(input("Введіть рівень рекурсії: "))

    plt.figure(figsize=(8, 8))
    pythagoras_tree(0, 0, 1, math.pi / 2, level)
    plt.axis("equal")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()