x = [4,"Tom",1,"Michael",5,7,"Jimmy Smith"]

def draw_stars_str(list1):
    for val in list1:
        if type(val) == int:
            print "*" * val
        elif type(val) == str:
            print val[0].lower() * len(val)
    return draw_stars_str

print draw_stars_str(x)
