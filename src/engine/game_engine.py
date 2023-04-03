import esper
import pygame
import json

from src.ecs.systems.s_color_change import system_color_change
from src.ecs.systems.s_rendering import system_render
from src.ecs.systems.s_movement import system_movement
from src.ecs.systems.s_screen_bounce import system_screen_bounce
from src.ecs.systems.s_enemy_spawner import system_enemy_spawner

from src.create.prefab_creator import crear_nivel, crear_cuadrado


class GameEngine:
    def __init__(self) -> None:
        pygame.init()

        self.cfg_route = "./ECS_01_00/assets/cfg_03/" # esta ruta se puede editar para cambiar el nivel

        self.clock = pygame.time.Clock()
        self.is_running = False
        self.delta_time = 0
        self.ecs_world = esper.World()
        self.config = json.load(
            open(self.cfg_route + "window.json"))
        self.framerate = self.config["framerate"]
        self.height = self.config["size"]["h"]
        self.width = self.config["size"]["w"]
        self.screen = pygame.display.set_mode(
            (self.width, self.height), pygame.SCALED)
        pygame.display.set_caption(self.config["title"])

    def run(self) -> None:
        self._create()
        self.is_running = True
        while self.is_running:
            self._calculate_time()
            self._process_events()
            self._update()
            self._draw()
        self._clean()

    def _create(self):
        # propiedades = json.load(
        #     open("./ECS_01_00/assets/cfg/enemies.json"))
        # for obj_name in propiedades:
        #     obj = propiedades[obj_name]
        #     crear_cuadrado(self.ecs_world,
        #                    pygame.Vector2(0, 0),
        #                    pygame.Vector2(obj["velocity_min"], obj["velocity_max"]),
        #                    pygame.Color(obj["color"]["r"], obj["color"]["g"], obj["color"]["b"]),
        #                    pygame.Vector2(obj["size"]["x"], obj["size"]["y"])
        #                    )
        enemyInfo = json.load(
            open(self.cfg_route + "enemies.json"))
        levelInfo = json.load(
            open(self.cfg_route + "level_01.json"))
        crear_nivel(self.ecs_world, levelInfo["enemy_spawn_events"], enemyInfo)


    def _calculate_time(self):
        self.clock.tick(self.framerate)
        self.delta_time = self.clock.get_time() / 1000.0

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_running = False

    def _update(self):
        system_movement(self.ecs_world, self.delta_time)
        system_screen_bounce(self.ecs_world, self.screen)
        # system_color_change(self.ecs_world, self.screen)
        system_enemy_spawner(self.ecs_world, self.delta_time)

    def _draw(self):
        self.screen.fill(pygame.Color(self.config["bg_color"]["r"],
                                      self.config["bg_color"]["g"],
                                      self.config["bg_color"]["b"]))
        system_render(self.ecs_world, self.screen)

        pygame.display.flip()

    def _clean(self):
        pygame.quit()
