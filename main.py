import random
from hollands_algorithm import hollands_algorithm
from target_function import target_function, decode
import numpy
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def main():
    pop_size = int(input("Enter population size: "))
    mutation_prob = float(input("Enter mutation probability: "))
    crossing_prob = float(input("Enter crossing probability: "))
    max_iterarions = int(input("Enter number of iterations: "))
    population = []
    coin = [True, False]
    for i in range(pop_size):
        individual = numpy.zeros(20)
        for j in range(20):
            drawn = random.choice(coin)
            individual[j] = drawn
        population.append(individual)
    best_x, best_ev, history, history_ev = hollands_algorithm(target_function,
                                                              population,
                                                              pop_size,
                                                              mutation_prob,
                                                              crossing_prob,
                                                              max_iterarions)
    print('Best found x = ', decode(best_x), "\n Best evaluation = ", best_ev)

    keys = []
    for i in range(max_iterarions):
        for j in range(pop_size):
            keys.append(i*pop_size*6/5+j)
    plt.plot(keys, history_ev)
    plt.show()

    to_show = [0,
               max_iterarions//7,
               2*max_iterarions//7,
               3*max_iterarions//7,
               4*max_iterarions//7,
               5*max_iterarions//7,
               6*max_iterarions//7,
               max_iterarions-1]
    for n in to_show:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x = [x[0] for x in history[(pop_size*n):(pop_size*(n+1))]]
        y = [x[1] for x in history[(pop_size*n):(pop_size*(n+1))]]
        z = [x[2] for x in history[(pop_size*n):(pop_size*(n+1))]]
        c = [x[3] for x in history[(pop_size*n):(pop_size*(n+1))]]
        img = ax.scatter(x, y, z, c=c, cmap=plt.hot())
        fig.colorbar(img)
        plt.show()


if __name__ == "__main__":
    main()
