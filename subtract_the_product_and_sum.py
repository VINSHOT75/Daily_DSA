# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

def f(n):
    s,m=0,1
    while n>0:
        x = n%10
        s = s + x
        m = m * x
        n = n//10
    print(m,s)
    return m-s
print(f(234))