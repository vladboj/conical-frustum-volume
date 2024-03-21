import math


def compute_volume(a, b, c, d, h):
    # compute H to plug into the volume computation
    H = (math.sqrt(a * b) * h) / (math.sqrt(a * b) - math.sqrt(c * d))

    # volume computation
    volume = math.pi / 3 * ((a * b) * H - (c * d) * (H - h))

    return volume


# given the dimensions of the container and a height lower than the original height,
# i want to compute the volume of the subcontainer with that respective height
def compute_subcontainer_volume(a, b, c, d, h, new_height):
    # i mathematically found the following formula for finding the new minor and major axis
    # for the new eliptical base
    new_minor_axis = 2 * d + (new_height * (2 * b - 2 * d)) / h
    new_major_axis = 2 * c + (new_height * (2 * a - 2 * c)) / h
    new_volume = compute_volume(new_major_axis / 2, new_minor_axis / 2, c, d, new_height)
    return new_volume
