from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

ground = Entity(model='plane', scale=8, collider='mesh', texture='brick')

player = FirstPersonController()
app.run()