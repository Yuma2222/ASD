import sys
import time

from arrayProvider import randomArr, sortedArr, reversedArr, randomArr500K
from cocktailShakerSort import _cocktailSort
from heapsort import _heapSort
from mergeSort import _mergeSort
from quicksort import _quicksort


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


sys.setrecursionlimit(999999999)
testSortsFor(randomArr, "Random")
testSortsFor(sortedArr, "Sorted")
testSortsFor(reversedArr, "Reversed")
testSortsFor(randomArr500K, "Random500k")
