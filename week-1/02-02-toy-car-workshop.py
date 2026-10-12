MIN_WHEEL = 4
MIN_BODY = 1
MIN_FIGURES = 2

def cars(i_wheels, i_bodies, i_figures):
    i_counter = 0
    b_check = True
    while b_check:
        i_wheels -= MIN_WHEEL
        i_bodies -= MIN_BODY
        i_figures -= MIN_FIGURES

        if i_wheels > 0 and i_bodies > 0 and i_figures > 0:
            i_counter += 1
        else:
            b_check = False

    return i_counter

print(cars(2, 48, 76), cars(2, 48, 76) == 0)
print(cars(43, 15, 87), cars(43, 15, 87) == 10)
print(cars(88, 37, 17), cars(88, 37, 17) == 8)