import math


def compute_volume(a, b, c, d, h):
    # compute H to plug into the volume computation
    H = (math.sqrt(a * b) * h) / (math.sqrt(a * b) - math.sqrt(c * d))

    # volume computation
    volume = math.pi / 3 * ((a * b) * H - (c * d) * (H - h))

    return volume


def main():
    print("The volume of the frustum with the given dimension is " +
          str(round(compute_volume(26, 21, 21, 16, 10) / 1000, 2)) + " liters.")


if __name__ == "__main__":
    main()
