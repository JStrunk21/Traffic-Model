import pygame
import random
import numpy as np

# Simulation Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BACKGROUND_COLOR = (200, 200, 200)
ROAD_COLOR = (50, 50, 50)
LANE_COUNT = 3
VEHICLE_SPEED_RANGE = (2, 6)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Traffic Simulator")
clock = pygame.time.Clock()

class Vehicle:
    def __init__(self, x, y, speed=None, color=(0, 0, 255), width=40, height=20):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed if speed else random.randint(*VEHICLE_SPEED_RANGE)
        self.color = color

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

class Road:
    def __init__(self):
        self.lane_width = SCREEN_WIDTH // LANE_COUNT
        self.vehicles = []

    def add_vehicle(self):
        lane_x = random.randint(0, LANE_COUNT - 1) * self.lane_width + (self.lane_width // 4)
        new_vehicle = Vehicle(lane_x, -50)
        self.vehicles.append(new_vehicle)

    def update(self):
        for vehicle in self.vehicles:
            vehicle.move()
        self.vehicles = [v for v in self.vehicles if v.y < SCREEN_HEIGHT]

    def draw(self, screen):
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, ROAD_COLOR, (0, 100, SCREEN_WIDTH, SCREEN_HEIGHT - 200))
        for vehicle in self.vehicles:
            vehicle.draw(screen)

class TrafficSimulator:
    def __init__(self):
        self.road = Road()
        self.running = True

    def run(self):
        while self.running:
            screen.fill(BACKGROUND_COLOR)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            if random.random() < 0.1:  # Randomly add vehicles
                self.road.add_vehicle()
            
            self.road.update()
            self.road.draw(screen)
            
            pygame.display.flip()
            clock.tick(30)  # 30 FPS

        pygame.quit()

if __name__ == "__main__":
    sim = TrafficSimulator()
    sim.run()
