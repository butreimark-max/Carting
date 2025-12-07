import arcade
from pyglet.math import Vec2

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = ""


class Car(arcade.Sprite):
    start = False
    revers = False
    stop = False
    gear_1 = False
    gear_2 = False
    gear_3 = False

    def movement(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.start :  # todo: разобрать (так не пишем)
            self.change_y += 0.3
        if self.revers :
            self.change_y -= 0.1
        if self.stop :
            if self.change_y>0:
                self.change_y -=0.5
            else:
                self.change_y=0
        if self.gear_1:
            if self.change_y>10:
                self.change_y +=0.5
        if self.gear_3:
            if self.change_y>20:
                self.change_y +=0.8
        if self.gear_3:
            if self.change_y>30:
                self.change_y +=1

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background = arcade.load_texture("pixil-frame-0 (6).png")
        """--------------------Camera---------------"""
        self.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        """------------------Car----------------------"""
        self.first_car = Car("pixil-frame-0 (4).png")

        self.first_car.center_x = self.background.width // 2
        self.first_car.center_y = self.background.height // 2

        self.first_car.angle = 0

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.D:
            self.first_car.angle = -20
            self.first_car.change_x = 10
        if symbol == arcade.key.A:
            self.first_car.angle = 20
            self.first_car.change_x = -10
        if symbol == arcade.key.W:
            self.first_car.start = True
        if symbol == arcade.key.S:
            self.first_car.revers = True
        if symbol == arcade.key.SPACE:
            self.first_car.stop = True
        if symbol == arcade.key.X:
            self.first_car.gear_1= True
        if symbol == arcade.key.C:
            self.first_car.gear_2 = True
        if symbol == arcade.key.V:
            self.first_car.gear_3 = True

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.A:
            self.first_car.angle = 0
            self.first_car.change_x = 0
        if symbol == arcade.key.D:
            self.first_car.angle = 0
            self.first_car.change_x = 0
        if symbol == arcade.key.S:
            self.first_car.revers = False
        if symbol == arcade.key.W:
            self.first_car.start = False
        if symbol == arcade.key.SPACE:
            self.first_car.stop=False
        if symbol == arcade.key.Z:
            self.first_car.gear_1= False
        if symbol == arcade.key.C:
            self.first_car.gear_2 = False
        if symbol == arcade.key.V:
            self.first_car.gear_3 = False

    def on_draw(self):
        self.clear()
        self.camera.use()
        arcade.draw_lrwh_rectangle_textured(
            0, 0,
            self.background.width,
            self.background.height,
            self.background
        )
        self.first_car.draw()

    def on_update(self, delta_time):
        self.first_car.movement()

        camera_x = self.first_car.center_x - SCREEN_WIDTH / 2
        camera_y = self.first_car.center_y - SCREEN_HEIGHT / 2

        self.camera.move_to(Vec2(camera_x, camera_y))

        self.camera.angle = -self.first_car.angle



window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()

# https://api.arcade.academy/en/2.6.17/examples/index.html
"""
Найти все спрайты для проекта
Чекнуть остальные примеры проектов от аркейда
Обучить машину двигаться по нажатию


"""
