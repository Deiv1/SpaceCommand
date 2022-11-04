from operator import truediv
import pygame
import os
import time
import random
pygame.font.init()  #Initialize fonts

# Initalize Pygame surface for drawing(size only)
WIDTH = 750
HEIGHT = 750
WXH = [WIDTH, HEIGHT] #Width x Height
WINDOW = pygame.display.set_mode(WXH)
pygame.display.set_caption("Space Command")

# Load image assets
# Enemy ships
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

# Player Ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background Image and fit window
BG = pygame.image.load(os.path.join("assets", "background-black.png"))
BG = pygame.transform.scale(BG, WXH)

#colour constants
WHITE = (255,255,255)
RED = (255,0,0)

# Set up fonts
# font colour and attributes
ANTIALIAS = True
FONT_SIZE = 50
# Create main font
main_font = pygame.font.SysFont("comicsans", FONT_SIZE)


# Define movable objects
class Ship:
    def __init__(self, x, y, health=100):
        self.x, self.y = x,y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
        
    def draw(self, window): #draw the ship on specified surface
        window.blit(self.ship_img, (self.x, self.y))        
        
    def move(self, x, y):  #move the ship relative to current position +/- x,y and prevent from going off screen
        if (self.x + x > 0) and (self.x + x + self.ship_img.get_width() < WIDTH):
            self.x += x
        if (self.y + y > 0) and (self.y + y + self.ship_img.get_height() < HEIGHT):
            self.y += y
        
    def position(self, x, y): #set the current position of the ship
        self.x = x
        self.y = y

    def set_ship_img(self, ship_img, laser_img): #load graphics for the ship
        self.ship_img = ship_img
        self.laser_img = laser_img
        
    def shoot(self):  #shoot stuff
        self.laser_img = self.laser_img

class Player(Ship):

    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

class Enemy(Ship):

    def __init__(self, x, y, colour, health=100):
        super().__init__(x,y,health)

def main():
    whatthe = 1
    # Collision checking setup
    run = True
    FPS = 60 #Frames per second
    clock = pygame.time.Clock()

    # Game Play Variables
    level = 1
    lives = 5
    velocity = 300
    player_velocity = velocity // FPS #adjust velocity for variable FPS
    
    # Create ship object
    player_ship = Player(300, 600)
    def redraw_window():

        #Cover previous screen
        WINDOW.blit(BG, (0,0))

        # Print user info
        level_label=main_font.render(f"Level: {level}", ANTIALIAS, WHITE)
        lives_label=main_font.render(f"Lives: {lives}", ANTIALIAS, WHITE)

        WINDOW.blit(level_label, (10,10))
        WINDOW.blit(lives_label,(BG.get_width()-10-lives_label.get_width(),10))
        player_ship.draw(WINDOW)

        #Update Surface
        pygame.display.update()

    while run:
        
        #wait for tick
        clock.tick(FPS)

        #draw window
        redraw_window()

        #Check for user inputs
        for event in pygame.event.get():

            #Check for QUIT
            if event.type == pygame.QUIT:
                run = False

        # Check key presses and perform actions    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_ship.move(player_velocity, 0)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_ship.move(-player_velocity, 0)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player_ship.move(0, -player_velocity)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
           	player_ship.move(0, player_velocity)


main()
