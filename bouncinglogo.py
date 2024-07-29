import sys, random, time

try:
    import bext
except:
    print("This programme required bext, which can be installed by running 'pip install bext' in your terminal.")
    sys.exit(
    )

WIDTH, HEIGHT = bext.size()

WIDTH -= 1

NUMBER_OF_LOGOS = 5
PAUSE_AMOUNT = 0.2
COLOURS = ['red', 'green', 'yellow', 'blue']

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = [UP_RIGHT, UP_LEFT, DOWN_LEFT, DOWN_RIGHT]

COLOUR = 'colour'
X = 'x'
Y = 'y'
DIR = 'direction'

def main():
    bext.clear()

    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOUR: random.choice(COLOURS),
                      X: random.randint(1, WIDTH-4),
                      Y: random.randint(1, HEIGHT-4),
                      DIR: random.choice(DIRECTIONS)})
        if logos[-1][X] % 2 == 1:
            logos[-1][X] -= 1
        
    cornerBounces = 0

    while True:
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            print(' ', end='')

            originalDirection = logo[DIR]

            if logo[X] == 0 and logo[Y] ==0:
                logo[DIR] == DOWN_RIGHT
                cornerBounces += 1
            
            elif logo[X] == 0 and logo[Y] == HEIGHT -1:
                logo[DIR] == UP_RIGHT
                cornerBounces += 1

            
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] == DOWN_LEFT
                cornerBounces += 1

            
            elif logo[X] == 0 and logo[Y] == HEIGHT -1:
                logo[DIR] == UP_RIGHT
                cornerBounces += 1