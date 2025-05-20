# Pygame game template
import pygame as pg
import sys
import config as c # Import the config module
from enemy import Enemy

def init_game():
    pg.init()
    pg.font.init
    screen = pg.display.set_mode((c.WINDOW_WIDTH, c.WINDOW_HEIGHT)) # Use constants from config
    pg.display.set_caption(c.TITLE)
    return screen

def handle_events():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                return False
    return True




def main():
    screen = init_game()
    clock = pg.time.Clock() # Initalize the clock here
    # Enenmy
    enemy_group = pg.sprite.Group()
    enemy_image = pg.image.load('images/enemy_1.png').convert_alpha()
    enemy = Enemy((200, 300), enemy_image)
    enemy_group.add(enemy)


    running = True
    while running:
        running = handle_events()
        screen.fill(c.GREEN) # Use color from config
        
        enemy.move()
        enemy_group.draw(screen)



        pg.display.flip()
        # Limit the frame rate to the specified frames per second
        clock.tick(c.FPS) # Use the clock to control the frame rate

    pg.quit()
    sys.exit()

if __name__ == '__main__':
    main()



