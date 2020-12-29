import pygame
from element import Element


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