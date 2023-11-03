import time
from BinarySearch import BinarySearch
from LinearSearch import LinearSearch

def test_binary_search():
    test_nums = list(range( 1000000, 0, -1 ))
    target = 999999999

    start_time = time.time()
    result = BinarySearch(test_nums, target)
    end_time = time.time()
    time_taken = (end_time - start_time) * 1000
    formatted_time = "{:.5f}".format(time_taken)

    expected_result = BinarySearch(test_nums, target)

    assert result == expected_result, "Test failed: target value not found or incorrect index"
    print("Test passed: Target value found at index:", result)
    print("Time taken: by BINARY {} ms".format(formatted_time))

def test_linear_search():
    test_nums = list(range( 1000000, 0, -1 ))
    target = 999999999

    start_time = time.time()
    result = LinearSearch(test_nums, target)
    end_time = time.time()
    time_taken = (end_time - start_time) * 1000
    formatted_time = "{:.5f}".format(time_taken)

    expected_result = LinearSearch(test_nums, target)

    assert result == expected_result, "Test failed: target value not found or incorrect index"
    print("Test passed: Target value found at index:", result)
    print("Time taken by LINEAR: {} ms".format(formatted_time))

# Run the test case
if __name__ == "__main__":
    test_binary_search()
    test_linear_search()