import random

def set_locations(key = None):
    locatios = {
        1: "8ª/AJ",
        2: "8ª/GB",
        3: "8ª/GRA",
        4: "8ª/GRA/USA",
        5: "8ª/GRD",
        6: "8ª/GRG",
        7: "8ª/GRR",
        8: "8ª/SL",
        9: "8ª/GRS"
    }
    
    if key is None:
        key = random.randint(1, 9)

    return locatios[key]