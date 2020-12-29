# Sorting Visualizer

import math
import random
import time
import pygame


# Setting up Window and Display
WIDTH, HEIGHT = 800, 800
window = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Sorting Visualizer")


# Defining Colors
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

# Defining the Array Element Class
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


def draw(window, array, array_size, WIDTH):
    window.fill(RED)
    for element in array:
        element.draw(window)
    pygame.display.update()


# Insertion Sort
def insertionSort(draw, array):
    for i in range(1, len(array)):
        j = i
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        while array[j] < array[j - 1] and j > 0:
            Element.currentlyComparing(array[j], array[j - 1])
            draw()
            Element.toSwap(array[j], array[j - 1])
            draw()
            array[j], array[j - 1] = Element.swap(array[j], array[j - 1])
            draw()
            Element.doneComparing(array[j], array[j - 1])
            draw()
            j -= 1


# Selection Sort
def selectionSort(draw, array):
    for i in range(len(array) - 1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        temp = array[i]
        index = i
        for j in range(i + 1, len(array)):
            Element.currentlyComparing(array[i], array[j])
            draw()
            if array[j] < temp:
                temp = array[j]
                index = j
            Element.doneComparing(array[i], array[j])
        if temp < array[i]:
            Element.toSwap(array[i], array[index])
            draw()
            array[i], array[index] = Element.swap(array[i], array[index])
            draw()
            Element.doneComparing(array[i], array[index])
            draw()


# Bubble Sort
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


# Merge Sort
def mergeSort(draw, array):
    length = len(array)
    temp = [None for i in range(length)]
    k = 1
    while k < length:
        for left in range(0, length - k, k * 2):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            right = left + k
            right_end = right + k
            if right_end > length:
                right_end = length
            index, i, j = left, left, right
            while i < right and j < right_end:
                Element.currentlyComparing(array[i], array[j])
                draw()
                if array[i] < array[j]:
                    temp[index] = array[i].int_value
                    Element.doneComparing(array[i], array[j])
                    draw()
                    i += 1
                else:
                    temp[index] = array[j].int_value
                    Element.doneComparing(array[i], array[j])
                    draw()
                    j += 1
                index += 1
            while i < right:
                temp[index] = array[i].int_value
                i += 1
                index += 1
            while j < left:
                temp[index] = array[j].int_value
                j += 1
                index += 1
            for index in range(left, right_end):
                if temp[index]:
                    array[index] = Element(
                        temp[index],
                        index,
                        len(array),
                        array[index].largest_element,
                    )
                pygame.time.delay(20)
                draw()
            draw()
        k *= 2


# Choose which algorithm you want to visualize
def algorithm(draw, array):
    # bubbleSort(draw, array)
    # selectionSort(draw, array)
    # insertionSort(draw, array)
    mergeSort(draw, array)


# Creating the input array object
def buildArray(my_list, array_size, WIDTH):
    array = []
    for i in range(array_size):
        array.append(Element(my_list[i], i, array_size, max(my_list)))
    return array


# Returns a random list
def createList():
    length = random.choice([i for i in range(90, 151)])
    while WIDTH % length != 0:
        length = random.choice([i for i in range(90, 151)])
    my_list = [i + 1 for i in range(length)]
    random.shuffle(my_list)
    return my_list


# Main function
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
