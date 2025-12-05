import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = ""

class Car (arcade.Sprite):
    def movement(self):
        pass
class truck (arcade.Sprite):
    def movement_truck(self):
        self.center_x += self.change_x
        self.center_y += self.change_y


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        """-----------------BackGround---------"""
        self.race_road =truck ("pixil-frame-0 (6).png")
        self.race_road.center_x = SCREEN_WIDTH
        self.race_road.center_y = SCREEN_HEIGHT / 1.5
        self.race_road.scale = 4
        """------------------Car----------------------"""
        self.first_car =Car ("pixil-frame-0 (4).png")
        self.first_car.center_x = SCREEN_WIDTH /2
        self.first_car.center_y = SCREEN_HEIGHT / 2
        self.first_car.angle=0
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==arcade.key.D:
            self.race_road.angle=20
            self.race_road.change_x = -10
        if symbol==arcade.key.A:
            self.race_road.angle=-20
            self.race_road.change_x=10
        if symbol==arcade.key.S:
            self.race_road.change_y= 10
        if symbol==arcade.key.W:
            self.race_road.change_y=-10

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol==arcade.key.A:
            self.race_road.angle=0
            self.race_road.change_x = 0
        if symbol==arcade.key.D:
            self.race_road.angle=0
            self.race_road.change_x=0
        if symbol==arcade.key.W:
            self.race_road.change_y= 0
        if symbol==arcade.key.S:
            self.race_road.change_y=0
    def on_draw(self):
        self.clear()
        self.race_road.draw()
        self.first_car.draw()

    def on_update(self, delta_time):
        self.first_car.movement()
        self.race_road.movement_truck()

window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()

#https://api.arcade.academy/en/2.6.17/examples/index.html
"""
Найти все спрайты для проекта
Чекнуть остальные примеры проектов от аркейда
Обучить машину двигаться по нажатию


"""