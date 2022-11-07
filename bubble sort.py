
def bubble_sort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# def bubble_sort(list):
# 	length = len(list) - 1
# 	sorted = False
# 	while not sorted:
# 		sorted = True
# 		for i in range(length):
# 			if list[i] > list[i + 1]:
# 				sorted = False
# 				list[i], list[i + 1] = list[i + 1], list[i]
# 	return list

if __name__ == '__main__':
    list = [5, 4, 3, 2, 1]
    print(bubble_sort(list))

# time complexity of bubble sort is : O(n^2)
# space complexity of bubble sort is : O(1)