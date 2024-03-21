from inputs_getter import get_inputs
from height_computation import get_height
from volume_computation import compute_volume
from volume_computation import compute_subcontainer_volume
from operator import itemgetter


def main():
    inputs = get_inputs()
    a, b, c, d, h = itemgetter('a', 'b', 'c', 'd', 'h')(inputs)
    choice = int(input("1 -> height computation // 2 -> volume computation // 3 -> new volume computation // 4 -> exit: "))
    while choice != 4:
        if choice == 1:
            wanted_volume = float(input("Enter wanted volume: "))
            wanted_height = get_height(a, b, c, d, h, wanted_volume)
            print(f"The height corresponding to the wanted volume is {round(wanted_height, 2)}cm.")
        elif choice == 2:
            volume = compute_volume(a, b, c, d, h)
            print(f"The volume of the eliptical frustum with the given dimensions is {round(volume, 2)}cm3.")
        elif choice == 3:
            new_height = float(input("Enter new_height: "))
            new_volume = compute_subcontainer_volume(a, b, c, d, h, new_height)
            print(f"The new volume of the eliptical frustum with the given dimensions and new height is {round(new_volume, 2)}cm3.")
        choice = int(input("1 -> height computation // 2 -> volume computation // 3 -> new volume computation // 4 -> exit: "))


if __name__ == '__main__':
    main()


# for my particular container 1 the dimensions are:
# small base: 42(major axis) 32(minor axis)
# large base: 52(major axis) 42(minor axis)
# height: 22
# a = 26
# b = 21
# c = 21
# d = 16
# h = 22
# ---------------------
# for my particular container 2 the dimensions are:
# small base: 5(major axis) 5(minor axis)
# large base: 7(major axis) 7(minor axis)
# height: 13
# a = 3.5
# b = 3.5
# c = 2.5
# d = 2.5
# h = 13
