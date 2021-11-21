# An implementation of the Quick Sort Algorithm that counts the number of pivots and comparisons. Uses the median value as pivot.

from math import ceil

# Create counters for the number of pivots and comparisons
num_pivots = 0
num_comparisons = 0

def quick_sort(numbers):

    global num_pivots
    global num_comparisons

    # The length of the list
    length = len(numbers)

    # If the length of the sublist is 0, then we have used every value as a pivot in this sublist
    if length < 1:
        return numbers

    # The pivot element, the middle number or, if list has an even number of elements, the element to the right of the middle
    pivot_index = ceil((length - 1)/2)

    # Create lists to hold elements that are greater and lesser than the pivot element
    greater = []
    lesser = []

    if length == 1:
        # If the length of the list is 1, then we would simply compare it to the two values next to it and ensure it is in the correct place,
        # however we cannot do this here as the implementation doesn't allow for it, so assume it is in the correct place and increment number of comparisons by 1
        num_comparisons += 1

    # Save value of pivot and remove pivot from list
    pivot = numbers[pivot_index]
    numbers.pop(pivot_index)

    # Increment number of pivots
    num_pivots += 1

    # Compare each element to the pivot and append to the appropriate list
    for element in numbers:
        (greater if element > pivot else lesser).append(element)

        # Increment the number of comparisons
        num_comparisons += 1

    # Recursively apply this algorithm to each sublist until the all numbers have been used as pivots
    return quick_sort(lesser) + [pivot] + quick_sort(greater)

'''
Example

>>>my_list = [5, 3, 8, 0, 9, 6, 8, 4]
>>>sorted = quick_sort(my_list)
>>>print(len(sorted), num_pivots)
8 8
>>>print(num_comparisons)
24
>>>print(sorted)
[0, 3, 4, 5, 6, 8, 8, 9]
'''