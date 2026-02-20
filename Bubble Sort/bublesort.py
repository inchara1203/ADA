import random
import time
import matplotlib.pyplot as plt

def buble_sorthing(l):
    n=len(l)
    for i in range(n-1): 
        for j in range(n-i-1):
            if(l[j]>l[j+1]):
                l[j],l[j+1] = l[j+1],l[j]


n=[random.randint(5000,6000) for _ in range(10)]
time_taken = []
for i in n:
    l = [random.randint(5000,6000) for _ in range(i)]
    start_time = time.time()
    buble_sorthing(l)
    end_time = time.time()
    time_taken.append(end_time-start_time)
    print (l)  
    print("Time taken: ",end_time-start_time,"seconds")

plt.plot(n, time_taken, marker='o')
plt.xlabel('List Size')
plt.ylabel('Time Taken (seconds)')
plt.title('Insertion Sort Time Complexity')
plt.grid(True)
plt.savefig('bubles_sort_time_complexity.png', dpi=300, bbox_inches='tight')
plt.show()