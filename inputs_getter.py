from PIL import Image


def get_inputs():
    # show image for user so that he understands what each input means
    img = Image.open("./assets/eliptical_frustum.png")
    img.show()

    # place inputs in a dictionary
    variables = ['a', 'b', 'c', 'd', 'h']
    inputs = {}

    for variable in variables:
        inputs[variable] = float(input(f"{variable}(cm) = "))

    # place the only separate input from the dict into a variable
    wanted_volume = float(input("wanted_volume(ml) = "))

    return inputs, wanted_volume
