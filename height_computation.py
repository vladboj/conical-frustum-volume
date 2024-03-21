from volume_computation import compute_volume


def get_height(A, B, C, D, H, wanted_volume):
    # a, b, and h will remain constant because of the design of the program
    # c and d will remain constant because a real life frustum container is upside down

    # TOLERANCE is the value by which the computed volume can differ from
    # the wanted volume in order for the wanted_height to be accepted
    TOLERANCE = 0.01

    # implement a binary search algorithm to find the wanted_height
    prev_a, prev_b, prev_c, prev_d = A, B, C, D
    bottom, top = 0, H
    while bottom < top:
        wanted_height = (bottom + top) / 2
        a = (prev_a + prev_c) / 2
        b = (prev_b + prev_d) / 2
        volume = compute_volume(a, b, C, D, wanted_height)
        if abs(volume - wanted_volume) <= TOLERANCE:
            return wanted_height
        elif volume < wanted_volume:
            bottom = wanted_height
            prev_c = a
            prev_d = b
        elif volume > wanted_volume:
            top = wanted_height
            prev_a = a
            prev_b = b
    return -1
