import esper
import pygame

from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform

def system_render(world:esper.World, screen:pygame.Surface):
    components = world.get_components(CTransform, CSurface)

    c_t:CTransform
    c_s:CSurface
    for entity, (c_t, c_s) in components: # type: ignore
        screen.blit(c_s.surf, c_t.pos)
