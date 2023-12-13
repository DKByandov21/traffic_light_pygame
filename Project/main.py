import numpy as np
import time
import pygame
from function.simulate_traffic_light import simulate_traffic_light

pygame.init()

traffic_light = np.array([[5, 2, 1],
                          [0, 1, 1],  
                          [1, 2, 5]])

simulate_traffic_light(traffic_light)
