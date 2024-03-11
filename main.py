from inputs_getter import get_inputs
from height_computation import get_height

def main():
    inputs, wanted_volume = get_inputs()
    wanted_height = get_height(inputs, wanted_volume)
    print(f"The height corresponding to the wanted volume is {round(wanted_height, 2)}cm.")

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
#---------------------
# for my particular container 2 the dimensions are:
# small base: 5(major axis) 5(minor axis)
# large base: 7(major axis) 7(minor axis)
# height: 13
# a = 3.5
# b = 3.5
# c = 2.5
# d = 2.5
# h = 13