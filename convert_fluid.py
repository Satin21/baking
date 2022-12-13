# function that converts fluids to mL
def convert_fluid(amount, unit):
    """function that converts amount in unit to mL"""
    if unit == "fl_oz":
        return amount * 29.57
    if unit == "pint":
        return amount * 473.18
    if unit == "cup":
        return amount * 236.59
    return False
