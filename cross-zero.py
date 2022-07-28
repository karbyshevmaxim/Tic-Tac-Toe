import pygame as pg
import sys
import time

FPS = 60
WINDOW = (800, 400)

count = 0
steps = 0
line_color = (160, 82, 45)
dictionary = [[230, 66.5], [400, 66.5], [570, 66.5], [230, 200], [400, 200], [570, 200], [230, 333], [400, 333], [570, 333]]

def plus(x, types, field):
    if types == 1:
        field[x] = 1
    if types == 0:
        field[x] = 2

    return 0

def analysis(field, types, steps):
    if (field[0] == 1 and field[1] == 1 and field[2] == 1 or
        field[0] == 1 and field[3] == 1 and field[6] == 1 or
        field[0] == 1 and field[4] == 1 and field[8] == 1 or
        field[2] == 1 and field[4] == 1 and field[6] == 1 or
        field[2] == 1 and field[5] == 1 and field[8] == 1 or
        field[3] == 1 and field[4] == 1 and field[5] == 1 or
        field[6] == 1 and field[7] == 1 and field[8] == 1 or
        field[1] == 1 and field[4] == 1 and field[7] == 1):
        if types == 1:
            print("X   wins!")
            time.sleep(3)
            pg.quit()
            sys.exit()
        else:
            print("O   wins!")
            time.sleep(3)
            pg.quit()
            sys.exit()
            
    if (field[0] == 2 and field[1] == 2 and field[2] == 2 or
        field[0] == 2 and field[3] == 2 and field[6] == 2 or
        field[0] == 2 and field[4] == 2 and field[8] == 2 or
        field[2] == 2 and field[4] == 2 and field[6] == 2 or
        field[2] == 2 and field[5] == 2 and field[8] == 2 or
        field[3] == 2 and field[4] == 2 and field[5] == 2 or
        field[6] == 2 and field[7] == 2 and field[8] == 2 or
        field[1] == 2 and field[4] == 2 and field[7] == 2):
        if types == 1:
            print("X   wins!")
            time.sleep(3)
            pg.quit()
            sys.exit()
            
        else:
            print("O   wins!")
            time.sleep(3)
            pg.quit()
            sys.exit()
    if steps == 9:
        print("DRAW")
        time.sleep(3)
        pg.quit()
        sys.exit()
            

def square(coords, array):
    if(coords[0] > 150 and coords[0] < 310 and coords[1] > 0 and coords[1] < 133):
        return 1 - array[0]
        
    if(coords[0] > 310 and coords[0] < 490 and coords[1] > 0 and coords[1] < 133):
        return 2 - array[1]
        
    if(coords[0] > 490 and coords[0] < 650 and coords[1] > 0 and coords[1] < 133):
        return 3 - array[2]
        
    if(coords[0] > 150 and coords[0] < 310 and coords[1] > 133 and coords[1] < 266):
        return 4 - array[3]
        
    if(coords[0] > 310 and coords[0] < 490 and coords[1] > 133 and coords[1] < 266):
        return 5 - array[4]
        
    if(coords[0] > 490 and coords[0] < 650 and coords[1] > 133 and coords[1] < 266):
        return 6 - array[5]
        
    if(coords[0] > 150 and coords[0] < 310 and coords[1] > 266 and coords[1] < 400):
        return 7 - array[6]
        
    if(coords[0] > 310 and coords[0] < 490 and coords[1] > 266 and coords[1] < 400):
        return 8 - array[7]
        
    if(coords[0] > 490 and coords[0] < 650 and coords[1] > 266 and coords[1] < 400):
        return 9 - array[8]

    return 0
        
class Symbol:
    def __init__(self, types, coords):
        self.types = types
        self.coords = coords
        
    def draw(self, screen):
        self.screen = screen
        
        if(self.types == 1):
            pg.draw.line(self.screen, (245, 0, 0), [(int)(self.coords[0] - 50), (int)(self.coords[1] - 50)], [(int)(self.coords[0] + 50), (int)(self.coords[1] + 50)], 2)
            pg.draw.line(self.screen, (245, 0, 0), [self.coords[0] - 50, self.coords[1] + 50], [self.coords[0] + 50, self.coords[1] - 50], 2)
        else:
            pg.draw.circle(self.screen, (245, 0, 0), [(int)(self.coords[0]), (int)(self.coords[1])], 50, 2)

        return 0


keks = []
array = [0, 0, 0, 0, 0, 0, 0, 0, 0]
field = [0, 0, 0, 0, 0, 0, 0, 0, 0]

print("Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает. \nПервый ход делает игрок, ставящий крестики.\n\n")
print("----------------------------------------------")
time.sleep(3)
screen = pg.display.set_mode((800, 400))
pg.display.set_caption("Cross - zero")
bg_color = (245, 222, 179)
timer = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            coords = pg.mouse.get_pos()
            if(square(coords, array)):
                count += 1
                count = count % 2
                steps += 1
                x = square(coords, array)
                plus(x - 1, count, field)
                kek = Symbol(count, dictionary[x - 1])
                keks.append(kek)
                array[x - 1] = x
                         
    pg.draw.line(screen,line_color, [310, 0], [310, 400], 2)
    pg.draw.line(screen,line_color, [490, 0], [490, 400], 2)
    pg.draw.line(screen,line_color, [150, 133], [650, 133], 2)
    pg.draw.line(screen,line_color, [150, 266], [650, 266], 2)
    for kek in keks:
        kek.draw(screen)
        
    pg.display.flip()
    analysis(field, count, steps)
    screen.fill(bg_color)
    timer.tick(FPS)


