import esper
import pygame

from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity


def system_screen_bounce(world: esper.World, screen: pygame.Surface):
    components = world.get_components(CTransform, CSurface, CVelocity)
    screen_rect = screen.get_rect()

    c_t: CTransform
    c_s: CSurface
    c_v: CVelocity
    for entity, (c_t, c_s, c_v) in components:  # type: ignore
        obj_rect = c_s.surf.get_rect(topleft=c_t.pos)

        if obj_rect.left <= 0 or obj_rect.right >= screen_rect.width:
            c_v.vel.x *= -1
            obj_rect.clamp_ip(screen_rect)
            if obj_rect.left <= 0: # Se agrega el condicional extra para evitar que el objeto se quede pegado a la pared
                obj_rect.left = 1
            elif obj_rect.right >= screen_rect.width:
                obj_rect.right = screen_rect.width - 1
            c_t.pos.x = obj_rect.x
        if obj_rect.top <= 0 or obj_rect.bottom >= screen_rect.height:
            c_v.vel.y *= -1
            obj_rect.clamp_ip(screen_rect)
            if obj_rect.top <= 0:
                obj_rect.top = 1
            elif obj_rect.bottom >= screen_rect.height:
                obj_rect.bottom = screen_rect.height - 1
            c_t.pos.y = obj_rect.y

