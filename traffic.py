import pygame
import numpy as np

# Initialize Pygame\pygame.init()

# Simulation Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BACKGROUND_COLOR = (200, 200, 200)
ROAD_COLOR = (50, 50, 50)
VEHICLE_COLOR = (0, 0, 255)
LANE_COUNT = 3
VEHICLE_SPEED = 5

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Traffic Simulation")

class Vehicle:
    def __init__(self, x, y, width=40, height=20):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = VEHICLE_SPEED

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, VEHICLE_COLOR, (self.x, self.y, self.width, self.height))

class Road:
    def __init__(self):
        self.lane_width = SCREEN_WIDTH // LANE_COUNT
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def update(self):
        for vehicle in self.vehicles:
            vehicle.move()

    def draw(self, screen):
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, ROAD_COLOR, (0, 100, SCREEN_WIDTH, SCREEN_HEIGHT - 200))
        for vehicle in self.vehicles:
            vehicle.draw(screen)

# Main simulation loop
def main():
    clock = pygame.time.Clock()
    road = Road()
    road.add_vehicle(Vehicle(200, 150))
    road.add_vehicle(Vehicle(400, 100))

    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        road.update()
        road.draw(screen)
        
        pygame.display.flip()
        clock.tick(30)  # 30 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
