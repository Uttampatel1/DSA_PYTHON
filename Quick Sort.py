def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    
    else:
        pivot = x[0]
        i=0

        for j in range(len(x)-1):
            if x[j+1] < pivot:
                x[j+1], x[i+1] = x [i+1] , x[j+1]
                i += 1

        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])

        return first_part + second_part

def reverse_quicksort(x):
    if len(x) < 2:
        return x
    else:
        pivot = x[-1] # last one on the list is the pivot
        less = [i for i in x if i <= pivot] # i in all the table
        greater = [i for i in x[:-1] if i > pivot] #our last element
        return reverse_quicksort(greater) + [pivot] + reverse_quicksort(less)

alist = [30,4,6,1,25,69,199,2,5,12]
print(quicksort(alist)) 

# time complexity of bubble sort is : 
    # Best Case Complexity   : O(n log(n))
    # Average Case Complexity: O(n log(n))
    # Worst Case Complexity  : O(n^2)

# space complexity of bubble sort is : O(n*logn)



## ****  Udacity **** ##

# """Implement quick sort in Python.
# Input a list.
# Output a sorted list."""

# def parts(array,start ,end):
#     pivot = array[end]
#     left = start
#     right = end -1
#     yes = True
    
#     while yes:
        
#         while right >= left and array[right] >= pivot:
#             right = right - 1
            
#         while array[left] <= pivot and left <= right:
#             left = left + 1

#         if right < left:
#             yes = False
#         else:
#             m = array[right]
#             array[right] = array[left]
#             array[left] = m

#     m = array[end]
#     array[end] = array[left]
#     array[left] = m

#     return left

# def recursive_sort(array,start,end):
#     if start < end:
#         partition = parts(array,start,end)
#         recursive_sort(array,start+1,end)
#         recursive_sort(array,start,end -1)

# def quicksort(array):
#     recursive_sort(array,0,len(array)-1)
#     return array

# test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
# print (quicksort(test))

#  space complexity of bubble sort is : O(1)
