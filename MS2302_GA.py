import numpy as np
import matplotlib.pyplot as plt
import random

# Read city data from file
def read_cities(filename):
    cities = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            name = parts[0]
            x, y = float(parts[1]), float(parts[2])
            cities.append((name, x, y))
    return cities

cities = read_cities('India_cities.txt')

# Calculate the Euclidean distance between two points
def distance(city1, city2):
    return np.sqrt((city1[1] - city2[1])**2 + (city1[2] - city2[2])**2)

# Calculate the total distance of a path
def total_distance(cities, path):
    dist = 0.0
    for i in range(len(path)):
        dist += distance(cities[path[i]], cities[path[(i + 1) % len(path)]])
    return dist

# Fitness function (inverse of total distance)
def fitness(path, cities):
    return 1 / total_distance(cities, path)

# Tournament selection
def tournament_selection(population, cities, tournament_size=3):
    selected = random.sample(population, tournament_size)
    selected = sorted(selected, key=lambda x: fitness(x, cities), reverse=True)
    return selected[0]

# Ordered crossover (OX)
def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[start:end] = parent1[start:end]
    
    pointer = end
    for gene in parent2:
        if gene not in child:
            if pointer >= size:
                pointer = 0
            child[pointer] = gene
            pointer += 1
    return child

# Swap mutation
def mutate(path, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(path)), 2)
        path[i], path[j] = path[j], path[i]
    return path

# Create initial population
def create_population(pop_size, cities):
    population = []
    for _ in range(pop_size):
        individual = random.sample(range(len(cities)), len(cities))
        population.append(individual)
    return population

# Genetic Algorithm
def genetic_algorithm(cities, pop_size=100, generations=500, mutation_rate=0.02):
    population = create_population(pop_size, cities)
    avg_fitness_history = []

    for generation in range(generations):
        fitnesses = [fitness(ind, cities) for ind in population]
        avg_fitness = np.mean(fitnesses)
        avg_fitness_history.append(avg_fitness)
        
        # Best individual for path tracing every 100 generations
        best_individual = population[np.argmax(fitnesses)]
        best_distance = 1 / max(fitnesses)

        if generation % 100 == 0:
            print(f'Generation {generation}: Best Distance = {best_distance:.2f}')
            plot_cities(cities, best_individual, generation)

        new_population = []
        for _ in range(pop_size):
            parent1 = tournament_selection(population, cities)
            parent2 = tournament_selection(population, cities)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population

    best_individual = population[np.argmax(fitnesses)]
    best_distance = 1 / max(fitnesses)
    print(f'Final Best Distance = {best_distance:.2f}')
    plot_cities(cities, best_individual, 'Final')
    
    # Plot average fitness over generations
    plot_avg_fitness(avg_fitness_history)

# Plot the cities and the path
def plot_cities(cities, path, generation):
    x = [cities[i][1] for i in path] + [cities[path[0]][1]]
    y = [cities[i][2] for i in path] + [cities[path[0]][2]]
    names = [cities[i][0] for i in path]

    plt.figure(figsize=(10, 8))
    plt.plot(x, y, 'o-', markersize=10, lw=2)
    for i, name in enumerate(names):
        plt.text(x[i], y[i], name, fontsize=12, ha='right')
    plt.title(f"Traveling Salesman Path - Generation {generation}")
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")
    plt.show()

# Plot average fitness over generations
def plot_avg_fitness(avg_fitness_history):
    plt.figure(figsize=(10, 6))
    plt.plot(avg_fitness_history, label="Average Fitness")
    plt.title("Average Fitness Over Generations")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.legend()
    plt.show()

# Test the Genetic Algorithm
if __name__ == "__main__":
    cities = read_cities('India_cities.txt')
    genetic_algorithm(cities)
