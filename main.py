from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
level = [[0, 0, 0], [4, 0, 0], [8, 0, 3], [12, 1.5, 4], [15, 3, 8]]
def update():
    if player.y < -1:
        player.position = (0, 1, 0)
for i in level:
    ground = Entity(model='cube', scale=2, collider='cube', texture='white_cube', position=(i[0], i[1], i[2]))
Sky()
player = FirstPersonController(gravity=0.75, jump_height=3)
app.run()