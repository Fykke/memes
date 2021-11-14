import pygame
import time
pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("IT'S ABOUT DRIVE 😤 IT'S ABOUT POWER 🔥WE STAY HUNGRY😈WE DEVOUR 👹PUT IN THE WORK 💪PUT IN THE HOURS ⌚AND TAKE WHATS OURS 🥶")
carImg = pygame.image.load('rock1.png')
carImg = pygame.transform.scale(carImg, (40, 40))

play_error_sound = False 
FPS = 60 
clock = pygame.time.Clock()
t0 = time.time()
x =  (W//2)
y = (H//2)
sound = pygame.mixer.Sound("rock_sound2.wav")

while True:

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           exit()

    sc.fill((30, 30, 30))
    sc.blit(carImg, (x, y))
    t1 = time.time()
    dt = t1-t0
    print(dt)

    keys = pygame.key.get_pressed()   
    if keys[pygame.K_a]:
        x -= 5
    if keys[pygame.K_w]:
        y -= 5
    if keys[pygame.K_d]:
        x += 5
    if keys[pygame.K_s]:
        y += 5
    if keys[pygame.K_SPACE]:
        t0 = t1
        carImg = pygame.image.load('rock2.png')
        carImg = pygame.transform.scale(carImg, (80, 80))
        sc.blit(carImg, (x, y))
        pygame.mixer.Sound.play(sound)

    if dt >= 1.5:
        t0 = t1
        carImg = pygame.image.load('rock1.png')
        carImg = pygame.transform.scale(carImg, (40, 40))
    
    clock.tick(FPS)
    pygame.display.update()