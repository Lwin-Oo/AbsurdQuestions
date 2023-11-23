def add_array(arr1, arr2, result):
    for i in range(len(arr1)):
        result[i] = arr1[-(i + 1)] + arr2[-(i + 1)]

def main():
    N = int(input("Enter the size of the arrays (N ≤ 20): "))
    
    if N > 20 or N <= 0:
        print("Invalid size. Please enter a valid size (1 to 20).")
        return
    
    arr1 = [int(input(f"Enter element {i + 1} for the first array: ")) for i in range(N)]
    arr2 = [int(input(f"Enter element {i + 1} for the second array: ")) for i in range(N)]
    result = [0] * N

    add_array(arr1, arr2, result)

    print("Resultant array after adding in reverse order:")
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
