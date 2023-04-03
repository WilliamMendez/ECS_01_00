import math
import random
import esper
import pygame

from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.create.prefab_creator import crear_cuadrado


def system_enemy_spawner(world: esper.World, dt: float) -> None:
    components = world.get_component(CEnemySpawner)

    c_e: CEnemySpawner
    for entity, (c_e) in components:  # type: ignore
        # print(type(c_e))
        # print(c_e)
        c_e.spawnTimer += dt
        for spawnEvent in c_e.spawnEventData:
            if c_e.spawnTimer >= spawnEvent["time"] and c_e.created[c_e.spawnEventData.index(spawnEvent)] < 1:
                index = c_e.spawnEventData.index(spawnEvent)
                c_e.created[index] += 1
                name = spawnEvent["enemy_type"]
                enemy = c_e.enemies[name]
                speed = random.randint(enemy["velocity_min"], enemy["velocity_max"])
                movement_angle = random.randint(0, 360)
                x_speed = round(speed * math.cos(movement_angle))
                y_speed = round(speed * math.sin(movement_angle))
                crear_cuadrado(world,
                            pygame.Vector2(spawnEvent["position"]["x"], spawnEvent["position"]["y"]),
                            pygame.Vector2(x_speed, y_speed),
                            pygame.Color(enemy["color"]["r"], enemy["color"]["g"], enemy["color"]["b"]),
                            pygame.Vector2(enemy["size"]["x"], enemy["size"]["y"])
                )

