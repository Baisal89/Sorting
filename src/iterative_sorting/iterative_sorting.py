


# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i#establishes first index
        for j in range(i+1, len(arr)):#the array besides the first
            if arr[cur_index] > arr[j]:# if the first is greater than anything
                cur_index = j#new starting point
        arr[i], arr[cur_index] = arr[cur_index], arr[i]  #x,y = y,x swap notation
    return arr

    
​
# ​
# # TO-DO: Complete the selection_sort() function below 
# def selection_sort( arr ):
#     # loop through n-1 elements
#     # (n-1 because after the sort, the one remaining will be the largest)
#     for i in range(0, len(arr) - 1):
#         print(arr)
#         cur_index = i
#         smallest_index = cur_index
#         # TO-DO: find next smallest element
#         for j in range(cur_index, len(arr)):
#             if arr[j] < arr[smallest_index]:
#                 smallest_index = j
#         # (hint, can do in 3 loc)
#         # TO-DO: swap
#         arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]









list = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # Make a flag to show if swaps have occured
    # For each elements in the array....
        #Check it's neighbor to the right./...
            # If neighbor is smaller swap and make Flag true
        # If you get to the end and swps have occured, start again
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr)-1): 
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swapped = True
    return arr




# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    # first is to tally all of the occurances of each number and make an array that is ordered by index of all numbers 0-9
    # second is to add the tally number to the next number in the line
    count_index = [0,0,0,0,0,0,0,0,0,0]
    for i in range(len(arr)):#tally occurances
        count_index[arr[i]] += 1
    for i in range(len(count_index)):#add the previous number to the next number
        count_index[i] = count_index[i]+count_index[i-1]
    count_index.pop()
    count_index.insert(0,0)#shift all numbers to the right
    output_arr = [0]*len(arr)
    for i in range(len(arr)):#populate output array
        output_arr[count_index[arr[i]]] = arr[i]
        count_index[arr[i]]+=1
    return output_arr
