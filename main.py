from inputs_getter import get_inputs
from height_computation import get_height
from volume_computation import compute_volume
from volume_computation import compute_subcontainer_volume
from solute_volume_computation import compute_solute_volume
from operator import itemgetter


def main():
    choice = int(input("1 -> normal user // 2 -> owner: "))
    if choice == 1:
        inputs = get_inputs()
        a, b, c, d, h = itemgetter('a', 'b', 'c', 'd', 'h')(inputs)
        choice = int(input("1 -> height computation // 2 -> volume computation // 3 -> new volume computation // 4 -> solute volume computation // 5 -> exit: "))
        while choice != 5:
            if choice == 1:
                wanted_volume = float(input("Enter wanted volume(ml): "))
                wanted_height = get_height(a, b, c, d, h, wanted_volume)
                print(f"The height corresponding to the wanted volume is {round(wanted_height, 2)}cm.")
            elif choice == 2:
                volume = compute_volume(a, b, c, d, h)
                print(f"The volume of the eliptical frustum with the given dimensions is {round(volume, 2)}cm3.")
            elif choice == 3:
                new_height = float(input("Enter new_height(cm): "))
                new_volume = compute_subcontainer_volume(a, b, c, d, h, new_height)
                print(f"The new volume of the eliptical frustum with the given dimensions and new height is {round(new_volume, 2)}cm3.")
            elif choice == 4:
                solvent_volume = float(input("Enter solvent's volume(cm3): "))
                solution_concentration = float(input("Enter solution concentration(closed interval (0,1)): "))
                solute_volume = compute_solute_volume(solvent_volume, solution_concentration)
                print(f"The volume of solute you need in order to achieve the wanted concentration is {round(solute_volume, 2)}.")
            choice = int(input("1 -> height computation // 2 -> volume computation // 3 -> new volume computation // 4 -> solute volume computation // 5 -> exit: "))
    elif choice == 2:
        choice = int(input("1 -> compute solute volume // 2 -> exit: "))
        while choice != 2:
            if choice == 1:
                height = float(input("Enter height(cm): "))
                mySubContainerVolume = compute_subcontainer_volume(26, 21, 21, 16, 22, height)
                solute_volume = compute_solute_volume(mySubContainerVolume, 0.03)
                print(f"Solute volume is {round(solute_volume, 2)} cm3.")
            choice = int(input("1 -> compute solute volume // 2 -> exit: "))


main()
