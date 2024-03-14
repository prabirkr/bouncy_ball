import pygame
import pygame.freetype

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()

#Initializing the display window
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncy Ball Game")

#Starting coordinates of the paddle
rect_x = 400
rect_y = 580

#initial speed of the paddle
rect_change_x = 0
rect_change_y = 0

#initial position of the ball
ball_x = 50
ball_y = 50

#speed of the ball
ball_change_x = 5
ball_change_y = 5

score = 0

#draws the paddle. Also restricts its movement between the edges
#of the window.
def drawrect(screen,x,y):
    if x <= 0:
        x = 0
    if x >= 699:
        x = 699    
    pygame.draw.rect(screen,RED,[x,y,100,20])

# Function to display game over message box
def game_over(score):
    pygame.font.init()
    font = pygame.font.SysFont('Calibri', 30)
    text_surface = font.render('Game Over! Score: ' + str(score), True, WHITE)
    text_rect = text_surface.get_rect(center=(size[0] / 2, size[1] / 2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)  # Display the message for 2 seconds
    pygame.quit()

#game's main loop    
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect_change_x = -6
            elif event.key == pygame.K_RIGHT:
                rect_change_x = 6
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                rect_change_x = 0

    screen.fill(BLACK)
    rect_x += rect_change_x
    ball_x += ball_change_x
    ball_y += ball_change_y

    # Ball movement and collision detection
    if ball_x < 0:
        ball_x = 0
        ball_change_x = -ball_change_x
    elif ball_x > 785:
        ball_x = 785
        ball_change_x = -ball_change_x
    elif ball_y < 0:
        ball_y = 0
        ball_change_y = -ball_change_y
    elif ball_y > 600:
        game_over(score)

    # Check if the ball hits the paddle
    if ball_x > rect_x and ball_x < rect_x + 100 and ball_y == 565:
        ball_change_y = -ball_change_y
        score += 1

    pygame.draw.rect(screen, WHITE, [ball_x, ball_y, 15, 15])
    drawrect(screen, rect_x, rect_y)

    #score board
    font = pygame.font.SysFont('Calibri', 15, False, False)
    text = font.render("Score = " + str(score), True, WHITE)
    screen.blit(text, [600, 100])       

    pygame.display.flip()         
    clock.tick(60)

pygame.quit()
