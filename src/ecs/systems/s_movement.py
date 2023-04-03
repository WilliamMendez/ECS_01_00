import esper

from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity

def system_movement(world:esper.World, dt:float):
    components = world.get_components(CVelocity, CTransform)

    c_v:CVelocity
    c_t:CTransform
    for entity, (c_v, c_t) in components: # type: ignore
        # print(type(c_v))
        c_t.pos += c_v.vel * dt
