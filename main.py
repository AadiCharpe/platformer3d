from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from csv import reader
app = Ursina()
with open('leveldata.csv', 'r') as f:
    lines = reader(f)
    linelist = list(lines)
    level = 0
    start = [[float(x) if '.' in x else int(x) for x in val.split('|')] for val in linelist[0]]
    levels = [[[float(x) if '.' in x else int(x) for x in val.split('|')] for val in line] for line in linelist[1:]] + [[]]
platforms = []
spring = False

class Platform(Entity):
    def __init__(self, position=(0,0,0), plat_id=0):
        self.plat_id = plat_id
        self.colors = [[50, 50, 50], [232, 19, 19], [178, 178, 178], [245, 245, 17], [24, 232, 24]]
        self.timer = 0.75
        model = 'cube' if plat_id % 2 == 0 else 'plane'
        super().__init__(model=model, scale=2, collider=model, texture='white_cube', color=rgb(self.colors[plat_id][0], self.colors[plat_id][1], self.colors[plat_id][2]), position=position)

def reset():
    player.position = (0, 1, 0)
    for plat in platforms:
        if plat.plat_id == 2:
            plat.enable()
            plat.timer = 0.75
            plat.color = rgb(178, 178, 178)

def update():
    global level, spring
    if player.y < -3:
        reset()
    for plat in platforms:
        if player.intersects(plat):
            if plat.plat_id == 1:
                reset()
            elif plat.plat_id == 2:
                plat.timer -= time.dt
                plat.color=rgb(178 + (1 - plat.timer) * 60, 178 + (1 - plat.timer) * 60, 178 + (1 - plat.timer) * 60)
                if plat.timer <= 0:
                    plat.disable()
            elif plat.plat_id == 3:
                player.jump_height = 15
                player.gravity = 0.5
                spring = True
            elif plat.plat_id == 4:
                level += 1
                createLevel()
                reset()
    if not spring:
        player.jump_height = 3
        player.gravity = 0.75
    spring = False

def createLevel():
    if level != 0:
        [destroy(e) for e in platforms]
        platforms.clear()
    for i in start:
        platforms.append(Platform(position=(i[0], i[1], i[2]), plat_id=i[3]))
    for i in levels[level]:
        platforms.append(Platform(position=(i[0], i[1], i[2]), plat_id=i[3]))

createLevel()
Sky()
player = FirstPersonController(gravity=0.75, jump_height=3, collider='box')
app.run()