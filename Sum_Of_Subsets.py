from itertools import combinations
arr = list(map(int,input("Enter the elements").split()))
d = int(input("Enter the need sum:"))

count= 0
v_subset= []
n = len(arr)
for i in range(n+1):
    for subset in combinations(arr,i):
        if sum(subset) ==d:
            count+= 1
            v_subset.append(subset)
print("total number of sets giving",d ,"is : ",count)
print("The subsets giving",d,"as sum is ",v_subset)