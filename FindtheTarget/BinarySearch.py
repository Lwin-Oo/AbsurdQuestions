
def BinarySearch(nums, target):
    
    """
        :type nums: List[int]
        :type target: int
        :rtype: int
    """
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left+right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1    

input_str = input("Enter an array of integers: ")
input_list = input_str.split()
nums = [int(item) for item in input_list]

input_target = input("Enter the target: ")
target = int(input_target)

target_index = BinarySearch(nums, target)

if target_index != -1:
    print("Target value found at index:", target_index)
else:
    print("Error!!")    