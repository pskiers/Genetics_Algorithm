import random
import numpy
from target_function import decode


def evaluate(target_function, population):
    return [target_function(individual) for individual in population]


def find_best(population, evaluations):
    best = 0
    for i in range(len(evaluations)):
        if evaluations[best] >= evaluations[i]:
            best = i
    return population[best], evaluations[best]


def reproduction(population, evaluations, population_size):
    norm = min(evaluations) + 1
    if norm > 0:
        norm = 0
    normed_ev = [evaluation - norm for evaluation in evaluations]
    legend = [(population[i], normed_ev[i]) for i in range(len(population))]
    legend = sorted(legend, key=lambda x: x[1], reverse=True)
    normed_ev = sorted(normed_ev)
    ev_sum = sum(normed_ev)
    new_popuulation = []
    while len(new_popuulation) < population_size:
        drawn = random.uniform(1, ev_sum)
        i = 0
        while drawn > 0:
            drawn -= normed_ev[i]
            i += 1
        new_popuulation.append(legend[i-1][0])
    return new_popuulation


def cross_and_mutate(reproduced, mutation_probability, crossing_probability):
    crossed = []
    if len(reproduced) % 2 == 1:
        crossed.append(random.choice(reproduced))
    for _ in range(len(reproduced)//2):
        parent1 = random.choice(reproduced)
        parent2 = random.choice(reproduced)
        drawn = random.random()
        if drawn < crossing_probability:
            genom_lenght = len(parent1)
            kid1 = numpy.zeros(genom_lenght)
            kid2 = numpy.zeros(genom_lenght)
            crossing_point = random.randint(1, genom_lenght-1)
            for i in range(crossing_point):
                kid1[i] = parent1[i]
                kid2[i] = parent2[i]
            for i in range(crossing_point, genom_lenght):
                kid1[i] = parent2[i]
                kid2[i] = parent1[i]
            crossed.append(kid1)
            crossed.append(kid2)
        else:
            crossed.append(parent1)
            crossed.append(parent2)
    for i in range(len(crossed)):
        for j in range(len(crossed[i])):
            drawn = random.random()
            if drawn < mutation_probability:
                if crossed[i][j] == 1:
                    crossed[i][j] = 0
                else:
                    crossed[i][j] = 1
    return crossed


def hollands_algorithm(target_function,
                       population,
                       population_size,
                       mutation_probability,
                       crossing_probability,
                       max_iterations):
    history = []
    history_ev = []
    iteration = 0
    evaluations = evaluate(target_function, population)
    best_x, best_ev = find_best(population, evaluations)
    while iteration < max_iterations:
        reproduced = reproduction(population, evaluations, population_size)
        crossed_and_mutated = cross_and_mutate(reproduced,
                                               mutation_probability,
                                               crossing_probability)
        history_ev.extend(evaluations)
        evaluations = evaluate(target_function, crossed_and_mutated)
        new_best_x, new_best_ev = find_best(crossed_and_mutated, evaluations)
        if new_best_ev <= best_ev:
            best_x = new_best_x
            best_ev = new_best_ev
        history.extend([decode(individual) for individual in population])
        population = crossed_and_mutated
        iteration += 1
        if iteration % 1000 == 0:
            print('Current generation: ', iteration)
    return best_x, best_ev, history, history_ev
