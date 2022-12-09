from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import uniform

app = Ursina()
ground = Entity(model='plane',
                texture='grass',
                collider='mesh',
                scale=(100, 1, 100))

player = FirstPersonController()
sky = Sky()
level = 1
blocks = []
direction = []
window.fullscreen = True


def upadte():
    global level
    i = 0
    for block in blocks:
        block.x -= direction[i] * time.dt
        if abs(block.x) > 5:
            direction[i] *= -1
        if block.intersects().hit:
            player.x -= direction[i] * time.dt
        i = i + 1
    if player.z > 56 and level == 1:
        level = 2
        sky.texture = 'sky_sunset'


for i in range(8):
    r = uniform(-2, 2)
    block = Entity(model='cube',
                   color=color.azure,
                   texture='white_cube',
                   position=(r, 1 + i, 3 + i * 5),
                   scale=(3, 0.5, 3),
                   collider='box')
    if r < 0:
        direction.append(1)
    else:
        direction.append(-1)
    blocks.append(block)

goal = Entity(color=color.green,
              model='cube',
              texture='white_cube',
              position=(0, 9, 46),
              scale=(10, 1, 10),
              collider='box')
pillar = Entity(color=color.gold,
                model='cube',
                position=(0, 34, 50),
                scale=(1, 50, 1))

app.run()
