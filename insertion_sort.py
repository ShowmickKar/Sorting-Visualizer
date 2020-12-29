import pygame
from element import Element


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