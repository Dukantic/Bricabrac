from function_usefull  import *
explanation_philipe = """
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
| This function converts the height in meter to Robert and the weight in kilograms to Philipe |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
"""
def philipe():

    print(explanation_philipe)
    height = number_input("The height : ") / 1.73
    weight = number_input("The weight : ") / 97

    print(f"The height is {height} Robert and the weight {weight} Philipe.")