import esper


class CEnemySpawner:
    def __init__(self, spawnEventData: list, enemies: dict) -> None:
        self.spawnEventData = spawnEventData
        self.spawnTimer = 0.0
        self.enemies = enemies
        self.created = [0 for i in range(len(self.spawnEventData))]
