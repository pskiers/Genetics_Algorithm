from math import sin


def decode(individual):
    if len(individual) != 4 * 5:
        raise ValueError('Bad genom lenght')
    x = [-16, -16, -16, -16]
    for i in range(4):
        for j in range(5):
            if individual[5*i+j] == 1:
                x[i] += 2**j
    return x


# PENALTY = 1000


def target_function(individual):
    x = decode(individual)
    y = ((x[0] + 2 * x[1] - 7) ** 2) + ((2*x[0] + x[1] - 5) ** 2)
    y += (sin(1.5*x[2]))**3+((x[2]-1)**2)*(1+2*(sin(1.5*x[3])**2))
    y += ((x[3] - 1) ** 2) * (1 + (sin(x[3]) ** 2))
    # for i in x:
    #     if i > 15:
    #         y += PENALTY * (i - 15) ** 2
    #     elif i < -16:
    #         y += PENALTY * (-16 - i) ** 2
    return y
