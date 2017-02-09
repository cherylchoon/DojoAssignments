#Part I
def draw_stars(list):
    for number in list:
        print "*" * number
    return "Success!"

y = [4,6,1,3,5,7,25]
print draw_stars(y)

#Part II
x = [4,"Tom",1,"Michael",5,7,"Jimmy Smith"]

def draw_stars_str(list1):
    for val in list1:
        if type(val) == int:
            print "*" * val
        elif type(val) == str:
            print val[0].lower() * len(val)
    return "Success!"

draw_stars_str(x)
