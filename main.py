# for my particular container the dimensions are:
# small base: 42(semi-major axis) 32(semi-minor axis)
# large base: 52(semi-major axis) 42(semi-minor axis)
# height: 22
#---------------------
# a = 26
# b = 21
# c = 21
# d = 16
# h = 22

from inputs_getter import get_inputs
from height_computation import get_height

def main():
    inputs, wanted_volume = get_inputs()
    wanted_height = get_height(inputs, wanted_volume)
    print(f"The height corresponding to the wanted volume is {round(wanted_height, 2)}cm.")

if __name__ == '__main__':
    main()
