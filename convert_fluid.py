# function that converts fluids to mL
def convert_fluid(amount, unit):
    """function that converts amount in unit to mL
    Can handle fl_oz, pint, cup
    Will return False if another unit is provided.
    """
    if unit == "fl_oz":
        return amount * 29.57
    elif unit == "pint":
        return amount * 473.18
    elif unit == "cup":
        return amount * 236.59
    else
        print("Did not recognize the provided unit. \
            Returning False. Expect the rest of your program to fail.")
        return False
