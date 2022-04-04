from re import L
from draw_algorithms import draw_columns
from database_management import *
import time

def bubbleSort(drawInfo, array, sort, ascending = True):
    array = drawInfo.array

    startTimer = time.time()
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            num1 = array[j]
            num2 = array[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                array[j], array[j + 1] = array[j + 1], array[j]
                draw_columns.drawList(drawInfo, {j: drawInfo.Green, j + 1: drawInfo.Red}, True)
                yield True
    
    endTimer = time.time()
    elapsedTime = endTimer-startTimer
    EventCreate(array, sort, elapsedTime)
    return array

def insertionSort(drawInfo, array, sort, ascending=True):
    array = drawInfo.array

    startTimer = time.time()
    for i in range(len(array) - 1):
        current = array[i]

        while True:
            ascending_sort = i > 0 and array[i - 1] > current and ascending
            descending_sort = i > 0 and array[i - 1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            array[i] = array[i - 1]
            i = i -1
            array[i] = current
            draw_columns.drawList(drawInfo, {i: drawInfo.Green, i - 1: drawInfo.Red}, True)
            yield True

    endTimer = time.time()
    elapsedTime = endTimer-startTimer
    EventCreate(array, sort, elapsedTime)
    return array

def selectionSort(drawInfo, array, sort, ascending=True):

    array = drawInfo.array

    startTimer = time.time()

    for i in range(len(array) - 1):
        Min = i

        for j in range(i + 1, len(array) - 1):

            if (array[j] > array[Min] and not ascending) or (array[j] < array[Min] and ascending):
                Min = j
        
        array[i], array[Min] = array[Min], array[i]
        draw_columns.drawList(drawInfo, {i: drawInfo.Green, i + 1: drawInfo.Red}, True)
        yield True

    endTimer = time.time()
    elapsedTime = endTimer-startTimer
    EventCreate(array, sort, elapsedTime)
    return array