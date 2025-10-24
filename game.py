import pygame
pygame.init()

# Screen
Screen_width = 800
Screen_height = 600
screen = pygame.display.set_mode((Screen_width, Screen_height))
clock = pygame.time.Clock()

# Collision function
def circle_rect_collision(circle_pos, circle_radius, rect):
    cx, cy = circle_pos
    closest_x = max(rect.left, min(cx, rect.right))
    closest_y = max(rect.top, min(cy, rect.bottom))
    distance_x = cx - closest_x
    distance_y = cy - closest_y
    return (distance_x ** 2 + distance_y ** 2) < (circle_radius ** 2)

# Ground setup
ground_level = 450
floor = pygame.Rect(0, ground_level, 800, 150)

# Players
player = pygame.Rect(200, ground_level - 50, 50, 50)
player2 = pygame.Rect(600, 400, 50, 50)

# Ball
ball_y = 430
ballpos = [Screen_width / 2, ball_y]
ballvel_y = 0
ballradius = 20
ballcolor = (255, 255, 255)

# Physics
velocity_y = 0
gravity = 0.5
jump_strength = -12

run = True
while run:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  

    # Key input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= 3
    if keys[pygame.K_d]:
        player.x += 3
    if keys[pygame.K_w] and player.bottom >= ground_level:
        velocity_y = jump_strength

    # Gravity update for player
    velocity_y += gravity
    player.y += velocity_y

    # Gravity update for ball
    ballvel_y += gravity
    ballpos[1] += ballvel_y

    # Ground collision
    if player.bottom >= ground_level:
        player.bottom = ground_level
        velocity_y = 0

    if ballpos[1] + ballradius >= floor.top:
        ballpos[1] = floor.top - ballradius
        ballvel_y = -ballvel_y * 0.7  # bounce a bit

    # Ball collision with player
    if circle_rect_collision(ballpos, ballradius, player):
        ballvel_y = -10

    # Drawing
    screen.fill((0, 0, 255))
    pygame.draw.rect(screen, (0, 255, 0), floor)
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen, (1, 21, 33), player2)
    pygame.draw.circle(screen, ballcolor, (int(ballpos[0]), int(ballpos[1])), ballradius)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
