import random

def set_locations(key = None):
    locatios = {
        1: "8ª/AJ - Sala 302 - 8ª/AJ",
        2: "8ª/CP - Sala 101 - 8ª/CP",
        3: "8ª/GB - Sala 304-A - 8ª/GB",
        4: "8ª/GRA - Sala 301 - 8ª/GRA",
        5: "8ª/GRA/USA - Sala T02 - 8ª / GRA/USA",
        6: "8ª/GRD - Sala 203 - 8ª/GRD",
        7: "8ª/GRG - Sala 103 - 8ª/GRG",
        8: "8ª/GRR - Sala 201 - 8ª/GRR",
        9: "8ª/SL - Sala 303-B - 8ª/SL"
    }
    
    if key is None:
        key = random.randint(1, 9)

    return locatios[key]