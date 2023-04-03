import pygame
import esper

from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_surface import CSurface

def system_color_change(world:esper.World, screen:pygame.Surface):
    components = world.get_components(CSurface, CTransform)
    screen_rect = screen.get_rect()

    c_s:CSurface
    c_t:CTransform
    for entity, (c_s, c_t) in components: # type: ignore
        color  = c_s.surf.get_at((0,0))
        obj_rect = c_s.surf.get_rect(topleft=c_t.pos)

        # set the red value to the relative position of the object in the screen height
        color[0] = int(obj_rect.y / screen_rect.height * 255)

        # set the green value to the relative position of the object in the screen width
        color[1] = int(obj_rect.x / screen_rect.width * 255)

        c_s.surf.fill(color)


