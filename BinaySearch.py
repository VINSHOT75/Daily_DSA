a = [1,2,12,34,56,67,78]
n = 67
s = 0
e = len(a) -1
while True:
    mid = (s+e)//2
    if a[mid] == n :
        print('found') 
        break
    elif a[mid] > n:
        e = mid-1
    elif a[mid] < n:
        s = mid+1
    if s>e:
        print("not found")
        break
