from BinarySearch import BinarySearch
from LinearSearch import LinearSearch

input_str = input("Enter an array of integers: ")
input_list = input_str.split()
nums = [int(item) for item in input_list]

input_target = input("Enter the target: ")
target = int(input_target)

target_index_Binary = BinarySearch(nums, target)
target_index_Linear = LinearSearch(nums, target)

if target_index_Binary != -1:
    print("Binary Search Loading.......")
    print("Target value found at index:", target_index_Binary)
else:
    print("Error!!")

if target_index_Linear != -1:
    print("Linear Search Loading.......")
    print("Target value found at index:", target_index_Linear)
else:
    print("Error!!")        