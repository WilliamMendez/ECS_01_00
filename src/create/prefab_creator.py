import esper
import pygame

from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity

def crear_cuadrado(ecs_world: esper.World, pos:pygame.Vector2, vel:pygame.Vector2, color:pygame.Color, size:pygame.Vector2) -> None:
    cuad_entity = ecs_world.create_entity()
    ecs_world.add_component(
        cuad_entity, CSurface(size, color))
    ecs_world.add_component(
        cuad_entity, CTransform(pos))
    ecs_world.add_component(
        cuad_entity, CVelocity(vel))

def crear_nivel(ecs_world: esper.World, spawnEventData: list, enemies: dict) -> None:
    spawner_entity = ecs_world.create_entity()
    ecs_world.add_component(
        spawner_entity, CEnemySpawner(spawnEventData, enemies))


