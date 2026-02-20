import random
import time
import matplotlib.pyplot as plt

def max_heapily(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapily(arr, n, largest)
def build_max_heap(arr):
    n= len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapily(arr, n, i)
def heap_sort(arr):
    n = len(arr)
    build_max_heap(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[0], arr[i]
        max_heapily(arr, i, 0)
        return arr
    
if __name__ == "__main__":
    data= [5, 8, 1, 2, 6, 3, 9]
    print("original array:", data)
    print("sorted array:", heap_sort(data.copy()))
    
n=[random.randint(5000,6000) for _ in range(10)]
time_taken = []
for i in n:
    l = [random.randint(5000,6000) for _ in range(i)]
    start_time = time.time()
    heap_sort(l)
    end_time = time.time()
    time_taken.append(end_time-start_time)
    print (l)  
    print("Time taken: ",end_time-start_time,"seconds")

plt.plot(n, time_taken, marker='o')
plt.xlabel('List Size')
plt.ylabel('Time Taken (seconds)')
plt.title('Heap sorthing Time Complexity')
plt.grid(True)
plt.savefig('Heap_sort_time_complexity.png', dpi=300, bbox_inches='tight')
plt.show()