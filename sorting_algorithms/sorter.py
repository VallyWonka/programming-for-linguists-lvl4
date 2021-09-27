from collections import Counter


class Sorter:
    @staticmethod
    def counting_sort(array):
        max_number = max(array) + 1
        counter = Counter(array)
        sorted_list = []
        for i in range(max_number):
            if i in counter:
                sorted_list.extend([i for _ in range(counter.get(i))])
        return sorted_list

    @staticmethod
    def quick_sort(array):
        if len(array) > 1:
            pivot = array.pop(-1)
            left_array = [item for item in array if item < pivot]
            right_array = [item for item in array if item >= pivot]
            return Sorter.quick_sort(left_array) \
                   + [pivot] \
                   + Sorter.quick_sort(right_array)
        else:
            return array

    @staticmethod
    def bubble_sort(array):
        for i in range(len(array) - 1):
            counter = 0
            for j in range(len(array) - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    counter += 1
            if counter == 0:
                break
        return array
