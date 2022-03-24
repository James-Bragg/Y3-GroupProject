from draw_algorithms import draw_columns


#       sort_list = ["Quick Sort", "Bubble Sort", "Insertion Sort"]
class sortingAlgorithms:

    def bubbleSort(drawInfo, ascending = True):
        lst = drawInfo.lst

        for i in range(len(lst) - 1):
            for j in range(len(lst) - 1 - i):
                num1 = lst[j]
                num2 = lst[j + 1]

                if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    draw_columns.drawList(drawInfo, {j: drawInfo.Green, j + 1: drawInfo.Red}, True)
                    yield True

        return lst

    def insertionSort(drawInfo, ascending=True):
        lst = drawInfo.lst
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

        return lst