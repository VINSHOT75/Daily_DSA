# When we can neglect the left or right part by finding
# a possible or not possible solution on a sorted ans search space. we can use binary search


def f(x):
    s = 0
    e = x -1
    if x == 1:
        return 1
    while s<=e:
        mid = (e-s)//2 + s
        midSquare = mid * mid
        if midSquare == x:
            return mid
        if midSquare < x:
            s = mid + 1
        if midSquare > x:
            e = mid -1
    if x < midSquare:
        return mid -1
    return mid
    



x= int(input("enter number = "))
print(f(x))