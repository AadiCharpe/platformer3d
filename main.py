from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
start = [[0, 0, 0, 0], [0, 0, -2, 0], [0, 0, 2, 0], [2, 0, 0, 0], [2, 0, -2, 0], [2, 0, 2, 0]]
levels = [[[5, 0, 0, 0], [8, 0, 3, 0], [12, 1, 3, 0], [15, 2, 5, 0], [16, 2, 8, 0], [20, 2, 8, 0], [24, 2, 8, 0], [28, 2, 8, 0], [30, 2, 8, 0], [32, 2.5, 12, 0], [36, 3, 12, 0], [38, 3, 12, 0], [38, 5, 12, 0], [38, 7, 12, 0], [38, 3, 8, 0], [40, 3, 12, 0], [44, 3, 12, 4], [44, 3, 14, 4], [44, 3, 10, 4], [46, 3, 12, 4], [46, 3, 14, 4], [46, 3, 10, 4]], []]
level = 0
platforms = []

class Platform(Entity):
    def __init__(self, position=(0,0,0), plat_id=0):
        self.plat_id = plat_id
        self.colors = [[50, 50, 50], [232, 19, 19], [178, 178, 178], [245, 245, 17], [24, 232, 24]]
        self.timer = 0.75
        model = 'cube' if plat_id % 2 == 0 else 'plane'
        super().__init__(model=model, scale=2, collider=model, texture='white_cube', color=rgb(self.colors[plat_id][0], self.colors[plat_id][1], self.colors[plat_id][2]), position=position)

def update():
    global level
    if player.y < -1:
        player.position = (0, 1, 0)
    for plat in platforms:
        if player.intersects(plat):
            if plat.plat_id == 1:
                player.position = (0, 1, 0)
            elif plat.plat_id == 2:
                plat.timer -= time.dt
                plat.color=rgb(178 + (1 - plat.timer) * 60, 178 + (1 - plat.timer) * 60, 178 + (1 - plat.timer) * 60)
                if plat.timer <= 0:
                    platforms.remove(plat)
                    destroy(plat)
            elif plat.plat_id == 3:
                player.gravity = -2
            elif plat.plat_id == 4:
                level += 1
                createLevel()
                player.position = (0, 1, 0)
    if player.gravity < 0.75:
        player.gravity += time.dt * 5
    if player.gravity > 0.75:
        player.gravity = 0.75

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