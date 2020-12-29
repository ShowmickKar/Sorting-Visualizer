import pygame
from element import Element


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
                pygame.time.delay(10)
                draw()
            draw()
        k *= 2
