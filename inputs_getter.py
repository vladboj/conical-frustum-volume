import os
from PIL import Image


def get_inputs():
    # show image for user so that he understands what each input means
    script_directory = os.path.dirname(__file__)
    image_path = os.path.join(script_directory, "assets", "eliptical_frustum.png")
    img = Image.open(image_path)
    img.show()

    # place inputs in a dictionary
    variables = ['a', 'b', 'c', 'd', 'h']
    inputs = {}

    for variable in variables:
        inputs[variable] = float(input(f"{variable}(cm) = "))

    return inputs
