def insertion_sort(arr):
    for i in range(1, len(arr)):
        k = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > k:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = k
arr= int(input("Enter number of elements: "))
n= input("Enter the elements")


print("Original array:", n)
insertion_sort(n)
print("Sorted array:", n)