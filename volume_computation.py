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
    # firstly, compute the scaling factor using the new height in order to scale down the larger base
    scaling_factor = new_height / h
    new_base_semi_minor_axis = b * scaling_factor
    new_base_semi_major_axis = a * scaling_factor
    new_volume = compute_volume(
        new_base_semi_major_axis, new_base_semi_minor_axis, c, d, new_height)
    return new_volume
