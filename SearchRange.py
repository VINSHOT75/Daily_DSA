# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

# 1. Updated Binary search to find range of a number
# 2. Divided the code into two parts
#     1. One for finding first occurence
#     2. For finding last occurence
# 3. Generally, we will stop our code in Binary serach if we find the target.
# 4. Here for first occurence, we will keep going left for finding the element even if we find it in first iteration only.
# 5. For last occurence, we will keep finding the element in right even if we get it.

def f(a,t):
    F = -1 # First occurence
    L =-1 # Last occurence
    s= 0 # Start for first occurence
    e = len(a)-1 # End for first occurence
    s2 = s # First for last occurnence
    e2 = e # Last for last occurence

    # Iterating for First Occurence
    while e>=s:
        mid = (e-s)//2 + s
        if a[mid] == t:
            F = mid
            e = mid -1 
        if a[mid] > t:
            e=mid-1
        if a[mid] < t:
            s = mid+1  
          
    # Iterating for Last occurence
    while e2>=s2:
        mid2 = (e2-s2)//2 + s2 
        if a[mid2] == t:
            L = mid2
            s2 = mid2 + 1
        if a[mid2] > t:
            e2 = mid2 -1
        if a[mid2] < t:
            s2 = mid2 + 1

    return [f,L]

a= [2,2]
t = 2
f(a,t)