import pygame
from math import radians, sin, cos
import datetime


class Clock():
    def __init__(self):
        # Constants
        self.width, self.height = 800, 800
        self.white = (255, 255, 255)
        self.blue = (34, 79, 228)
        self.FPS = 60
        self.center = (self.width//2, self.height//2)
        self.clock_radius = self.width//2

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Analog Clock")
        self.clock = pygame.time.Clock()

    def numbers(self, number, size, position):
        font = pygame.font.SysFont("Calibri", size, True, False)
        text = font.render(str(number), True, self.white)
        text_rect = text.get_rect(center=position)
        self.screen.blit(text, text_rect)

    def polar_to_cartesian(self, r, theta):
        x = r * sin(radians(theta))
        y = r * cos(radians(theta))
        return x + self.width//2, self.height//2 - y

    def draw_circle(self, screen):
        # main cricle
        pygame.draw.circle(self.screen, self.white,
                           self.center, self.clock_radius - 10, 5)
        # central circle
        pygame.draw.circle(screen, self.white, self.center, 12)

        # print numbers
        for number in range(1, 13):
            self.numbers(str(number), 60, self.polar_to_cartesian(
                self.clock_radius - 80, number * 30))

        for number in range(0, 360, 6):
            if number % 5:
                pygame.draw.line(self.screen, self.white, self.polar_to_cartesian(self.clock_radius-15, number),
                                 self.polar_to_cartesian(self.clock_radius - 30, number), 2)
            else:
                pygame.draw.line(self.screen, self.white, self.polar_to_cartesian(self.clock_radius-15, number),
                                 self.polar_to_cartesian(self.clock_radius - 35, number), 6)

    def draw_clock_hand(self):
        current_time = datetime.datetime.now()
        second = current_time.second
        minute = current_time.minute
        hour = current_time.hour

        # Hour
        R = self.clock_radius - 190
        theta = (hour + minute/60 + second/3600) * (360/12)
        pygame.draw.line(self.screen, self.white,
                         self.center, self.polar_to_cartesian(R, theta), 14)

        # Minute
        R = self.clock_radius - 150
        theta = (minute + second/60) * (360/60)
        pygame.draw.line(self.screen, self.white,
                         self.center, self.polar_to_cartesian(R, theta), 10)

        # Second
        R = self.clock_radius - 100
        theta = (second) * (360/60)
        pygame.draw.line(self.screen, self.white,
                         self.center, self.polar_to_cartesian(R, theta), 4)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            self.screen.fill(self.blue)
            self.draw_circle(self.screen)
            self.draw_clock_hand()

            pygame.display.update()
            self.clock.tick(self.FPS)


if __name__ == "__main__":
    myClock = Clock()
    myClock.run()
