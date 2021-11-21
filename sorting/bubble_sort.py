# An implementation of the Bubble Sort Algorithm that counts the number of passes, swaps and comparisons.

def bubble_sort(numbers):

    # Whether the list of numbers has been sorted
    sorted = False

    # A counter for the number of passes
    num_passes = 0

    # A counter for the number of swaps
    num_swaps = 0

    # A counter for the number of comparisons
    num_comparisons = 0

    # Loop until the list is sorted
    while sorted != True:

        # Whether a swap was made
        swap_done = False

        # Loop for the number of elements in the list - 1, aka the number of comparisons needed in a complete pass
        for i in range(len(numbers) - 1):

            # Compare two numbers to see if they need swapping
            if numbers[i] > numbers[i + 1]:

                # Swap the numbers and increment num_swaps by 1
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swap_done = True
                num_swaps += 1
            
            # Increment num_comparisons by 1
            num_comparisons += 1
        
        # If no swap was made then the sort is complete
        if not swap_done:
            sorted = True

        # Increment num_passes by 1
        num_passes += 1

    # Return the sorted list and metrics
    return numbers, num_passes, num_swaps, num_comparisons


'''
Example:

>>>my_list = [5, 3, 8, 0, 9, 6, 8, 4]

>>>out = bubble_sort(my_list)

>>>print("Sorted list: ", out[0], "\n Number of Passes: ", out[1], "\n Number of Swaps: ", out[2], "\n Number of Comparisons: ", out[3])

Sorted list:  [0, 3, 4, 5, 6, 8, 8, 9]
 Number of Passes:  6 
 Number of Swaps:  12 
 Number of Comparisons:  42

'''