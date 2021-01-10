# Sorting Visualizer

import math
import random
import time
import pygame
from element import Element
from element import draw
from merge_sort import mergeSort
from bubble_sort import bubbleSort
from selection_sort import selectionSort
from insertion_sort import insertionSort

pygame.init()


# Setting up Window and Display
WIDTH, HEIGHT = 800, 800
window = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Sorting Visualizer")


# Choose which algorithm you want to visualize
def algorithm(draw, array):
    # bubbleSort(draw, array)
    # selectionSort(draw, array)
    insertionSort(draw, array)
    # mergeSort(draw, array)


# Creating the input array object
def buildArray(my_list, array_size, WIDTH):
    array = []
    for i in range(array_size):
        array.append(Element(my_list[i], i, array_size, max(my_list)))
    return array


# Returns a random list
def createList():
    length = random.choice([i for i in range(30, 151)])
    while WIDTH % length != 0:
        length = random.choice([i for i in range(30, 151)])
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
                    started = False
                    my_list = createList()
                    array_size = len(my_list)
                    array = buildArray(my_list, array_size, WIDTH)
                    draw(window, array, array_size, WIDTH)
                    pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main(window, WIDTH)
