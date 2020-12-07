import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Christmas Invaders")
icon = pygame.image.load('santa-claus.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('sleigh.png')
playerX = 370
playerY = 480

def player(x, y):
     screen.blit(playerImg, (X, Y))

running = True
while running:

    screen.fill((0, 0, 0))
    playerX += 0.2
    print(playerX)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:   
                print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                print("Right arrow pressed")
        if event.type == pygame.KEYUP:
            if evnet.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystroke has been released")                
           

    player(playerX, playerY)
    pygame.display.update()