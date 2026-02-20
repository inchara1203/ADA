import random
import time

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
    
print (n_list)
print (sort_times)