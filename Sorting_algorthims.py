from re import L
from draw_algorithms import draw_columns
from database_management import *
import time

def bubbleSort(drawInfo, array, sort, ascending = True):
    lst = drawInfo.lst

    startTimer = time.time()
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_columns.drawList(drawInfo, {j: drawInfo.Green, j + 1: drawInfo.Red}, True)
                yield True
    
    endTimer = time.time()
    elapsedTime = endTimer-startTimer
    EventCreate(array, sort, elapsedTime)
    return lst

def insertionSort(drawInfo, array, sort, ascending=True):
    lst = drawInfo.lst

    startTimer = time.time()
    for i in range(len(lst) - 1):
        current = lst[i]

        while True:
            ascending_sort = i > 0 and lst[i - 1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[i] = lst[i - 1]
            i = i -1
            lst[i] = current
            draw_columns.drawList(drawInfo, {i: drawInfo.Green, i - 1: drawInfo.Red}, True)
            yield True

    endTimer = time.time()
    elapsedTime = endTimer-startTimer
    EventCreate(array, sort, elapsedTime)
    return lst

def selectionSort(drawInfo, array, sort, ascending=True):

    lst = drawInfo.lst

    startTimer = time.time()

    for i in range(len(lst) - 1):
        Min = i

        for j in range(i + 1, len(lst) - 1):

            if (lst[j] > lst[Min] and not ascending) or (lst[j] < lst[Min] and ascending):
                Min = j
        
        lst[i], lst[Min] = lst[Min], lst[i]
        draw_columns.drawList(drawInfo, {i: drawInfo.Green, i + 1: drawInfo.Red}, True)
        yield True

    endTimer = time.time()
    elapsedTime = endTimer-startTimer
    EventCreate(array, sort, elapsedTime)
    return lst