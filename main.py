import random
from hollands_algorithm import hollands_algorithm
from target_function import target_function, decode
import numpy
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from math import sqrt


def main():
    pop_size = int(input("Enter population size: "))
    mutation_prob = float(input("Enter mutation probability: "))
    crossing_prob = float(input("Enter crossing probability: "))
    max_iterarions = int(input("Enter number of iterations: "))
    coin = [True, False]
    keys = []
    history = []
    best_points = {}
    for _ in range(25):
        population = []
        for i in range(pop_size):
            individual = numpy.zeros(20)
            for j in range(20):
                drawn = random.choice(coin)
                individual[j] = drawn
            population.append(individual)
        best_x, best_ev, hist, history_ev = hollands_algorithm(target_function,
                                                               population,
                                                               pop_size,
                                                               mutation_prob,
                                                               crossing_prob,
                                                               max_iterarions)
        best_points[best_ev] = decode(best_x)
        history.extend(history_ev)
        keys.extend(range(len(history_ev)))

    b_evaluation = min(best_points.keys())
    print('Best found x = ', best_points[b_evaluation], "Best evaluation = ", b_evaluation)

    plt.plot(keys, history, markersize=1, marker='.', linewidth=0)
    plt.show()

    keys = range(max_iterarions)
    values = [history[(pop_size*n):(pop_size*(n+1))] for n in range(max_iterarions*25)]
    val = []
    for i in range(max_iterarions):
        val.append(values[i])
        for j in range(1, 24):
            val[i].extend(values[i + j * max_iterarions])
    mean = [sum(i) for i in val]
    plt.plot(keys, mean)
    plt.show()

    var = []
    for i in range(max_iterarions):
        var.append(0)
        for point in val[i]:
            var[i] += (point - mean[i])**2
    sigma = [sqrt(v/(pop_size*25)) for v in var]
    plt.plot(keys, sigma)
    plt.show()

if __name__ == "__main__":
    main()
