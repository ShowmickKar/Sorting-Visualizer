import math
import random
import time
import pygame

HEIGHT, WIDTH = 800, 800
window = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Sorting Visualizer")

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

window.fill(RED)


class Element:
    def __init__(self, int_value, index, array_size, largest_element):
        self.int_value = int_value
        self.index = index
        self.width = WIDTH // array_size
        self.array_size = array_size
        self.poistion = self.index * self.width
        self.color = CYAN
        self.largest_element = largest_element
        self.max_height = WIDTH
        self.height = (self.int_value * WIDTH) // self.largest_element

    def draw(self, window):
        pygame.draw.rect(
            window, self.color, (self.poistion, 0, self.width, self.height)
        )

    @staticmethod
    def currentlyComparing(element1, element2):
        element1.color, element2.color = GREEN, GREEN

    @staticmethod
    def doneComparing(element1, element2):
        element1.color, element2.color = CYAN, CYAN

    @staticmethod
    def toSwap(element1, element2):
        element1.color, element2.color = RED, RED

    @staticmethod
    def swap(element1, element2):
        element1.int_value, element2.int_value = element2.int_value, element1.int_value
        element1.height, element2.height = element2.height, element1.height
        return element1, element2

    def __gt__(self, other):
        return self.int_value > other.int_value

    def __lt__(self, other):
        return self.int_value < other.int_value


def draw(window, array, array_size, WIDTH):
    for element in array:
        element.draw(window)
    pygame.display.update()


def bubbleSort(draw, array):
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            Element.currentlyComparing(array[i], array[j])
            draw()
            if array[i] > array[j]:
                Element.toSwap(array[i], array[j])
                draw()
                array[i], array[j] = Element.swap(array[i], array[j])
                draw()
            Element.doneComparing(array[i], array[j])
            draw()


def algorithm(draw, array):
    bubbleSort(draw, array)


def buildArray(my_list, array_size, WIDTH):
    array = []
    for i in range(array_size):
        array.append(Element(my_list[i], i, array_size, max(my_list)))
    return array


def createList():
    length = random.choice([i for i in range(30, 100)])
    while WIDTH % length != 0:
        length = random.choice([i for i in range(30, 100)])
    my_list = [i + 1 for i in range(length)]
    random.shuffle(my_list)
    return my_list


def main(window, WIDTH):
    my_list = createList()
    array_size = len(my_list)
    array = buildArray(my_list, array_size, WIDTH)

    started = False
    run = True
    while run:
        draw(window, array, array_size, WIDTH)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if started:
                continue
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    started = True
                    algorithm(lambda: draw(window, array, array_size, WIDTH), array)
                    started = False
                if event.key == pygame.K_c:
                    window.fill(RED)
                    started = False
                    my_list = createList()
                    array_size = len(my_list)
                    array = buildArray(my_list, array_size, WIDTH)
                    pygame.display.update()
    pygame.quit()


main(window, WIDTH)
