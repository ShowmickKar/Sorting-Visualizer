import pygame
from element import Element


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