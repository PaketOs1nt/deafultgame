import os
import platform
import sys
import time
import msvcrt

class ConsoleGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.clear_command = 'clear' if platform.system() != 'Windows' else 'cls'

    def clear_screen(self):
        os.system(self.clear_command)

    def draw(self):
        pass

    def update(self):
        pass

    def run(self):
        while True:
            self.clear_screen()
            self.draw()
            self.update()
            time.sleep(0.1)

class MyGame(ConsoleGame):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.player_x = width // 2
        self.player_y = height // 2

    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                if x == self.player_x and y == self.player_y:
                    print("P", end=" ")
                else:
                    print(".", end=" ")
            print()

    def update(self):
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()
            if key == 'w' and self.player_y > 0:
                self.player_y -= 1
            elif key == 'a' and self.player_x > 0:
                self.player_x -= 1
            elif key == 's' and self.player_y < self.height - 1:
                self.player_y += 1
            elif key == 'd' and self.player_x < self.width - 1:
                self.player_x += 1

# Запускаємо гру
game = MyGame(20, 10)
game.run()
