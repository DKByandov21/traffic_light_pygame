import pygame
import time


def simulate_traffic_light(traffic_light_matrix):
    screen = pygame.display.set_mode((300, 600))
    pygame.display.set_caption("Traffic Light Simulation")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        for i, phase in enumerate(traffic_light_matrix.T):
            for j, duration in enumerate(phase):
                if i == 0: 
                    pygame.draw.circle(screen, (255, 0, 0), (150, 200), 50)
                elif i == 1: 
                    pygame.draw.circle(screen, (255, 255, 0), (150, 300), 50) 
                elif i == 2:  
                    pygame.draw.circle(screen, (0, 255, 0), (150, 400), 50)

                pygame.display.flip()
                time.sleep(duration)

        running = False

    pygame.quit()
