# https://leetcode.com/problems/binary-search/description/

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

def search_2D_matrix(matrix, target):
    
    # loop through the main array
    main_left = 0
    main_right = len(matrix) - 1

    targetRow = []
   
    while main_left <= main_right:
        main_mid = (main_left + main_right) // 2

        # first element is larger, we decrease the right
        if matrix[main_mid][0] > target:
            main_right = main_mid - 1

        # last element is smaller, then we increase the left
        elif matrix[main_mid][-1] < target:
            main_left = main_mid + 1
        else:
            targetRow = matrix[main_mid]
            break
    
    # print(targetRow)
    left = 0
    right = len(targetRow) - 1

    while left <= right:
        mid = (left + right) // 2

        if targetRow[mid] == target:
            return True
        
        elif targetRow[mid] > target:
            right = mid - 1
        
        else:
            left = mid + 1

    return False

    # then loop through the sub arrays

print(search_2D_matrix(matrix, target))

# TODO: learn matrix flattening for a one pass solution
