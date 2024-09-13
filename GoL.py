import numpy as np
import pygame as py
import sys
import time

py.init()

size = 1000, 640
space = (20,20)

screen = py.display.set_mode(size)
filas = size[1] // space[1]
columnas = size[0] // space[0]

running = False
alive = []
toDead = []
mapa = np.zeros((filas, columnas))

  
        
def userInput(mouse):
    if mouse[0] in range(0,columnas*space[0]) and mouse[1] in range(0, filas*space[1]):
        x = mouse[0] // space[0] 
        y = mouse[1] // space[1] 
        mapa[y][x] = 1

def borrar(mouse):
    if mouse[0] in range(0,columnas*space[0]) and mouse[1] in range(0, filas*space[1]):
        x = mouse[0] // space[0] 
        y = mouse[1] // space[1] 
        mapa[y][x] = 0

def drawMap():
    for i in range(0, filas):
        for j in range(0, columnas):
            if mapa[i][j] == 1:
                py.draw.rect(screen, (255,255,255), (j*space[0], i*space[1], space[0], space[1]))

def status():
    for rows in range(filas):
        for columns in range(columnas):
            cells = 0
            try:
                mainCell = [rows, columns]
                    
                for col in range(columns-1, columns+2):
                    for row in range(rows-1, rows+2):
                        try:
                            
                            cells += mapa[row][col]
                            
                        except:
                            pass
                cells -= mapa[mainCell[0]][mainCell[1]]
                if mapa[mainCell[0]][mainCell[1]] == 1 and cells < 2 or cells > 3:
                    toDead.append(mainCell)
                elif mapa[mainCell[0]][mainCell[1]] == 0 and cells == 3:
                    alive.append(mainCell)
            except:
                pass

def aplicateStatus():
    for cell in toDead:
        mapa[cell[0]][cell[1]] = 0
    
    for cell in alive:
        mapa[cell[0]][cell[1]] = 1

    toDead.clear()
    alive.clear()

if __name__ == "__main__":
    while True:
        screen.fill((0,0,0))

        mouse = py.mouse.get_pos()

        for e in py.event.get():
            if py.QUIT == e.type:
                sys.exit()
            if not running:
                if py.mouse.get_pressed()[0]:
                    userInput(mouse)
                elif py.mouse.get_pressed()[2]:
                    borrar(mouse)
                    
            if e.type == py.KEYDOWN:
                if e.key == py.K_ESCAPE:
                    sys.exit()
                
                if e.key == py.K_SPACE and not running:
                    running = True
                elif e.key == py.K_SPACE and running:
                    running = False
                if e.key == py.K_c and not running:
                    mapa = np.zeros((filas, columnas))

        if running:
            status()
            aplicateStatus()
            time.sleep(0.1)

        drawMap()
        py.display.update()

