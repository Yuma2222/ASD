import sys
import time

from arrayProvider import randomArr, sortedArr, reversedArr, randomArr500K
from sorting_algorithms.cocktailShakerSort import _cocktailSort
from sorting_algorithms.heapsort import _heapSort
from sorting_algorithms.mergeSort import _mergeSort
from sorting_algorithms.quicksort import _quicksort


def quicksortTest(array, name):
    start_time = time.time()
    _quicksort(array, 0, len(array) - 1)
    print("Quicksort-" + name + ": %s seconds" % (time.time() - start_time).__round__(4))


def heapSortTest(array, name):
    start_time = time.time()
    _heapSort(array)
    print("heapSort-" + name + ": %s seconds" % (time.time() - start_time).__round__(4))


def cocktailSortTest(array, name):
    start_time = time.time()
    _cocktailSort(array)
    print("cocktailSort-" + name + ": %s seconds" % (time.time() - start_time).__round__(4))


def mergeSortTest(array, name):
    start_time = time.time()
    _mergeSort(array)
    print("mergeSort-" + name + ": %s seconds" % (time.time() - start_time).__round__(4))


def testSortsFor(array, name):
    print("--- --- --- " + name + " --- --- ---")
    heapSortTest(array, name)
    cocktailSortTest(array, name)
    mergeSortTest(array, name)
    # quicksortTest(array, name)
    print("")


if __name__ == '__main__':
    try:
        sys.setrecursionlimit(999999999)
        testSortsFor(randomArr, "Random")
        testSortsFor(sortedArr, "Sorted")
        testSortsFor(reversedArr, "Reversed")
        testSortsFor(randomArr500K, "Random500k")
    except Exception as e:
        print("Error during execution, exception: ", e)
