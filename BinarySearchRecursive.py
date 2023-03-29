def BinarySearch(s,e,a,n):
    # mid = (s+e)//2  This can create problem if e is too large
    mid = (e-s)//2 + s
    if a[mid] == n:
        return 'found'
    if s>=e:
        return 'not found'
    elif a[mid] > n:
        return BinarySearch(s,mid-1,a,n)
    elif a[mid] < n :
        return BinarySearch(mid+1,e,a,n)


a = [1,2,12,34,56,67,78]
n = 12
x = BinarySearch(0,6,a,n)
print(x)