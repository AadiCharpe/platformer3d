from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
level = [[0, 0, 0, 0], [0, 0, -2, 0], [0, 0, 2, 0], [2, 0, 0, 0], [2, 0, -2, 0], [2, 0, 2, 0], [5, 0, 0, 0], [9, 0, 3, 0], [13, 1.5, 4, 0], [16, 3, 8, 0]]
platforms = []
class Platform(Entity):
    def __init__(self, position=(0,0,0), plat_id=0):
        self.plat_id = plat_id
        self.colors = [[50, 50, 50], [232, 19, 19], [178, 178, 178], [245, 245, 17]]
        self.timer = 0.75
        model = 'cube' if plat_id % 2 == 0 else 'plane'
        super().__init__(model=model, scale=2, collider=model, texture='white_cube', color=rgb(self.colors[plat_id][0], self.colors[plat_id][1], self.colors[plat_id][2]), position=position)
def update():
    if player.y < -1:
        player.position = (0, 1, 0)
    for plat in platforms:
        if player.intersects(plat):
            if plat.plat_id == 1:
                player.position = (0, 1, 0)
            elif plat.plat_id == 2:
                plat.timer -= time.dt
                if plat.timer <= 0:
                    platforms.remove(plat)
                    destroy(plat)
            elif plat.plat_id == 3:
                player.gravity = -2
    if player.gravity < 0.75:
        player.gravity += time.dt * 5
for i in level:
    platforms.append(Platform(position=(i[0], i[1], i[2]), plat_id=i[3]))
Sky()
player = FirstPersonController(gravity=0.75, jump_height=3, collider='box')
app.run()