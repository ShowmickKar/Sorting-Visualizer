import math
import random
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 800


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
CYAN = (0, 255, 255)


def draw(window, array, array_size, WIDTH):
    window.fill(BLACK)
    for element in array:
        element.draw(window)
    pygame.display.update()


class Element:
    def __init__(self, int_value, index, array_size, largest_element):
        self.int_value = int_value
        self.index = index
        self.width = WIDTH // array_size
        self.array_size = array_size
        self.poistion = self.index * self.width
        self.color = WHITE
        self.largest_element = largest_element
        self.max_height = WIDTH
        self.height = (self.int_value * WIDTH) // self.largest_element

    def draw(self, window):
        pygame.draw.rect(
            window, self.color, (self.poistion, 0, self.width, self.height)
        )

    @staticmethod
    def currentlyComparing(element1, element2):
        element1.color, element2.color = RED, RED

    @staticmethod
    def doneComparing(element1, element2):
        element1.color, element2.color = WHITE, WHITE

    @staticmethod
    def toSwap(element1, element2):
        element1.color, element2.color = RED, RED

    @staticmethod
    def swap(element1, element2):
        element1.int_value, element2.int_value = element2.int_value, element1.int_value
        element1.height, element2.height = element2.height, element1.height
        return element1, element2

    @staticmethod
    def transformElement(one, other, index):
        one.int_value, one.height, one.index = other.int_value, other.height, index

    def __gt__(self, other):
        return self.int_value > other.int_value

    def __lt__(self, other):
        return self.int_value < other.int_value

    def __le__(self, other):
        return self.int_value <= other.int_value

    def __ge__(self, other):
        return self.int_value >= other.int_value

    def __le__(self, other):
        return self.int_value <= other.int_value
