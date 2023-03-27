# Program to print following pattern
#          1 2 3 
#          4 5 6
#          7 8 9

n = int(input())
i=1
j=1
while i<=n:
    while j<=n*i:
        print(j,end=" ")
        j+=1
    print()
    i+=1