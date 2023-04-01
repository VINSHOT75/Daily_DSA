# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

# First easy solution can be that print the index  of highest element in array
# One line solution in python is 
#     return (arr.index(max(arr)))

# Second approach is- find largest element using Binary search.
# Because it is a mountain pattern, only the largest element will have its neighbours smaller than itself
# Corner elements are escaped.

def f(a):
    s = 0
    n = len(a)-1
    e = n

    while e>=s:
        mid = (e-s)//2 + s
        if mid == 0:
            mid = mid +1
        if mid == n:
            mid = mid + 1
        if a[mid]>a[mid-1] and a[mid]>a[mid+1]:
            return mid
        elif a[mid]>= a[mid -1] and a[mid]<=a[mid+1]:
            s = mid + 1
        elif a[mid]<= a[mid -1] and a[mid]>=a[mid+1]:
            e = mid -1

a = [3,9,8,6,4]
print(f(a))