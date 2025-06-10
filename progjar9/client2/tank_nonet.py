import pygame
import sys

# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Progjar Tank  Game")

clock = pygame.time.Clock()
FPS = 60

image_size=(64,64)
tank_images = {
    "up": pygame.transform.scale(pygame.image.load("p1/tank_up.png"), image_size),
    "down": pygame.transform.scale(pygame.image.load("p1/tank_down.png"), image_size),
    "left": pygame.transform.scale(pygame.image.load("p1/tank_left.png"), image_size),
    "right": pygame.transform.scale(pygame.image.load("p1/tank_right.png"), image_size),
}

class Tank:
    def __init__(self):
        self.image = tank_images["up"]
        self.direction = "up"
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_UP]:
            self.y -= self.speed
            self.direction = "up"
        elif keys[pygame.K_DOWN]:
            self.y += self.speed
            self.direction = "down"
        elif keys[pygame.K_LEFT]:
            self.x -= self.speed
            self.direction = "left"
        elif keys[pygame.K_RIGHT]:
            self.x += self.speed
            self.direction = "right"
        self.image = tank_images[self.direction]

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

tank = Tank()

while True:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    tank.move(keys)
    tank.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)
