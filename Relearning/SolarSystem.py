import sys, pygame

pygame.init()
screensize = 700, 500
sunsize = 20, 20
sunrect = screensize[0]/2 - sunsize[0], screensize[1]/2 - sunsize[1]

screen = pygame.display.set_mode(screensize)
# Creates the Sun
sun = pygame.Surface(sunsize)
pygame.draw.circle(sun, [255, 255, 0], [10, 10], 10)

# Create Planets
planet = []
planets = [[9, 9], [12, 12], [13, 13], [10, 10], [38, 38], [36, 36], [20, 20], [18, 18], [6, 6]]
planetcolours = [[192, 192, 192], [102, 51, 0], [0, 0, 255], [255, 0, 0], [255, 153, 51],
                 [204, 204, 0], [102, 178, 255], [0, 0, 153], [102, 0, 204]]
planetsrect = []
distance = 40
for x in range(9):
    planetsrect.append([sunrect[0], sunrect[1] + distance])
    distance += 40
    if x > 3:
        distance += 5
for x in range(len(planets)):
    planet.append(pygame.Surface(planets[x]))
    pygame.draw.circle(planet[x], planetcolours[x],
                       [round(planets[x][0]/2), round(planets[x][1]/2)], round(planets[x][0]/2))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill([0, 0, 0])
    screen.blit(sun, sunrect)
    for x in range(len(planet)):
        screen.blit(planet[x], planetsrect[x])
    pygame.display.flip()
