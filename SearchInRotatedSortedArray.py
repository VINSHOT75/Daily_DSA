# ToDo: Check with Rishabh

def f(a,t):
    s = 0
    n = len(a)
    e = n -1
    mid = (e-s)//2 + s
    if a[0]>a[n-1]:
        if a[mid] > a[0]:
            if t<a[0]:
                s = mid+1
            if t > a[0]:
                e = mid
            if t == a[0]:
                return 0
        elif a[mid] == a[0]:
            s = mid + 1
            if t == a[0]:
                return 0
        else:
            if t < a[0]:
                e = mid 
            if t > a[0]:
                s = mid 
            if t == a[0]:
                return 0
    if a[s] < a[0]:
        s,e =e,s
        print(s,e)

        while s<=e:
            mid = (e-s)//2 + s
        if a[mid] == t:
            return mid
        if a[mid]>t:    
            s = mid + 1
        if a[mid] < t:
            e = mid -1       

    # print(s,e)
    while s <= e :
        mid = (e-s)//2 + s
        if a[mid] == t:
            return mid
        if a[mid]>t:
            e = mid -1
        if a[mid] < t:
            s = mid + 1
    return -1

# nums = [1,3]
# target = 1
nums = [5,1,3]
target = 1
target = 3

print(f(nums,target))