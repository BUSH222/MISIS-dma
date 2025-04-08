import numpy as np
import random


class AntColony:
    def __init__(self, distances, n_ants, alpha=1, beta=2, evaporation_rate=0.5, pheromone_deposit=1):
        self.distances = distances
        self.n_ants = n_ants
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.pheromone_deposit = pheromone_deposit
        self.n_cities = len(distances)
        self.pheromones = np.ones((self.n_cities, self.n_cities))

    def run(self):
        best_path = None
        best_path_length = float('inf')

        # for _ in range(self.n_iterations):
        paths = []
        path_lengths = []

        for _ in range(self.n_ants):
            path = self.construct_solution()
            path_length = self.calculate_path_length(path)
            paths.append(path)
            path_lengths.append(path_length)

            if path_length < best_path_length:
                best_path = path
                best_path_length = path_length

        self.update_pheromones(paths, path_lengths)
        return best_path, best_path_length, self.pheromones

    def construct_solution(self):
        path = [random.randint(0, self.n_cities - 1)]
        while len(path) < self.n_cities:
            current_city = path[-1]
            probabilities = self.calculate_transition_probabilities(current_city, path)
            next_city = self.select_next_city(probabilities)
            path.append(next_city)
        return path

    def calculate_transition_probabilities(self, current_city, visited):
        probabilities = []
        for city in range(self.n_cities):
            if city in visited:
                probabilities.append(0)
            else:
                pheromone = self.pheromones[current_city][city] ** self.alpha
                visibility = (1 / self.distances[current_city][city]) ** self.beta
                probabilities.append(pheromone * visibility)
        total = sum(probabilities)
        return [p / total for p in probabilities]

    def select_next_city(self, probabilities):
        return np.random.choice(range(self.n_cities), p=probabilities)

    def calculate_path_length(self, path):
        length = 0
        for i in range(len(path) - 1):
            length += self.distances[path[i]][path[i + 1]]
        length += self.distances[path[-1]][path[0]]  # Return to start
        return length

    def update_pheromones(self, paths, path_lengths):
        self.pheromones *= (1 - self.evaporation_rate)
        for path, length in zip(paths, path_lengths):
            for i in range(len(path) - 1):
                self.pheromones[path[i]][path[i + 1]] += self.pheromone_deposit / length
            self.pheromones[path[-1]][path[0]] += self.pheromone_deposit / length  # Return to start

    def update_distances(self, new_distances):
        self.distances = new_distances
        assert self.n_cities == len(new_distances)


if __name__ == "__main__":
    distances = [
        [0, 2, 2, 5],
        [2, 0, 4, 3],
        [2, 4, 0, 1],
        [5, 3, 1, 0]
    ]
    ant_colony = AntColony(distances, n_ants=10)
    while input() == '':
        best_path, best_path_length, pheromones = ant_colony.run()
        print("Best path:", best_path)
        print("Best path length:", best_path_length)
