import pygame  # noqa: D100
import random
from helper import calculate_distances
from algorithm import AntColony


pygame.init()

SCREENW = 1000
SCREENH = 800
FPS = 50
BGCOLOR = (0, 0, 0)
NUM_CITIES = 10

display = pygame.display.set_mode((SCREENW, SCREENH))  # w, h
clock = pygame.time.Clock()

# City coordinates
cities = []
for _ in range(NUM_CITIES):
    x = random.randint(0, SCREENW - 1)
    y = random.randint(0, SCREENH - 1)
    cities.append((x, y))

def game():
    """Main function of the game."""  # noqa: D401
    distances = calculate_distances(cities)
    ant_colony = AntColony(distances, n_ants=10)
    dist_visible = False
    best_path_visible = False
    best_path, best_path_length, pheromones = ant_colony.run()
    print("Distance:", best_path_length)
    while True:
        display.fill(BGCOLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_SPACE:
                    best_path, best_path_length, pheromones = ant_colony.run()
                    print("Distance", best_path_length)
                elif event.key == pygame.K_t:
                    dist_visible = not dist_visible
                elif event.key == pygame.K_b:
                    best_path_visible = not best_path_visible
                elif event.key == pygame.K_r:
                    ant_colony.reset_pheromones()
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if mouse_pressed[0]:
            for i, city in enumerate(cities):
                distance = ((mouse_pos[0] - city[0]) ** 2 + (mouse_pos[1] - city[1]) ** 2) ** 0.5
                if distance < 15:
                    cities[i] = mouse_pos
                    distances = calculate_distances(cities)
                    AntColony.update_distances(ant_colony, distances)
                    break

        for city in cities:
            pygame.draw.circle(display, (255, 0, 0), city, 5)

        if dist_visible:
            for i in range(len(distances)):
                for j in range(i + 1, len(distances)):
                    font = pygame.font.Font(None, 24)
                    distance_text = font.render(f"{distances[i][j]:.2f}", True, (255, 255, 255))
                    mid_x = (cities[i][0] + cities[j][0]) // 2
                    mid_y = (cities[i][1] + cities[j][1]) // 2
                    display.blit(distance_text, (mid_x, mid_y))
        if best_path_visible:
            for i in range(len(best_path)):
                start = cities[best_path[i]]
                end = cities[best_path[(i + 1) % len(best_path)]]
                pygame.draw.line(display, (255, 255, 255), start, end, 2)

        max_pheromone = max(max(row) for row in pheromones)
        for i in range(len(pheromones)):
            for j in range(i + 1, len(pheromones)):
                pheromone_percentage = pheromones[i][j] / max_pheromone
                if pheromone_percentage <= 0.1:
                    continue
                color = (int(pheromone_percentage * 255), int(pheromone_percentage * 255), 0)
                pygame.draw.line(display, color, cities[i], cities[j], 1)
        clock.tick(FPS)
        pygame.display.update()


if __name__ == "__main__":
    game()
    pygame.quit()
