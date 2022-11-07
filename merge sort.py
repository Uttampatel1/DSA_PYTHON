def combine(left_sublist,right_sublist):
    i , j = 0 ,0
    result = []

    # iterate through both left and right sublist
    while i< len(left_sublist) and j<len(right_sublist):
        # if left value is lower then right then append it to the result
        if left_sublist[i] <= right_sublist[j]:
            result.append(left_sublist[i])
            i += 1

        # if left value is lower then left then append it to the result
        else:
            result.append(right_sublist[j])
            j += 1
    
    # concatenate the rest of the left and right sublists
    result += left_sublist[i:]
    result +=right_sublist[j:]

    #return the result
    return result



def merge_sort(input_list):
	#if list contains only 1 element return it
	if len(input_list) <= 1:
		return input_list
	else:
		#split the lists into two sublists and recursively split sublists
		midpoint = int(len(input_list)/2)
		left_sublist = merge_sort(input_list[:midpoint])
		right_sublist = merge_sort(input_list[midpoint:])
		#return the merged list using the merge_list function above
		return combine(left_sublist,right_sublist)

#test run
number_list = [10,100,5,3,22,1,5,8,12,9,6,12,53,75,22,83,123,12123]
print (merge_sort(number_list))
# [1, 3, 5, 5, 6, 8, 9, 10, 12, 12, 22, 22, 53, 75, 83, 100, 123, 12123]

# time complexity of merge sort is : O(n log(n))
# space complexity of merge sort is : O(n)


