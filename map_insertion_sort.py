import random
import time
import matplotlib.pyplot as plt

n = [random.randint(5000,6000) for _ in range(10)]
def insertion_sort(arr):
    for i in range(1, len(arr)):
        k = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > k:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = k


insertion_sort(n)
print("Sorted array:", n)

n_list = [5000, 5200, 5400, 5600, 5800, 6000]
sort_times = []
for n in n_list:
    l = [random.randint(1,100) for _ in range(n)]
    s_t = time.time()
    insertion_sort(l)
    e_t = time.time()
    sort_times.append(e_t - s_t)
    
plt.plot(n_list, sort_times, marker='o')
plt.xlabel('List Size')
plt.ylabel('Time Taken (seconds)')
plt.title('Insertion Sort Time Complexity')
plt.grid(True)
plt.savefig('insertion_sort_time_complexity.png', dpi=300, bbox_inches='tight')
plt.show()
