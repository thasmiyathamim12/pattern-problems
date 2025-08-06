n = int(input("enter a num:"))
for i in range(n):
    for j in range(n):
        print("#",end ="  ")
    print() for square
n = int(input("enter a num:"))
for i in range(n):
    for j in range(i+1):
        print("#",end ="  ")
    print()

n=int(input("num:"))
for i in range(1,n+1):
    print(" # "*i) for increaing pattern

n = int(input("enter a num:"))
for i in range(n):
    for j in range(i,n):
        print("*",end ="  ")
    print()

n=int(input())
for i in range(n):
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i+1):
        print("*",end=" ")
    print()


n=int(input())
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("* ",end=' ')
    print()

hill pattern
n=int(input())
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=' ')
    for j in range(i):
        print("*",end= " ")
    print()

n=int(input("enter a num:"))
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(" *",end=" ")
    for j in range(1,n):
        print(" *",end=" ")

    print()
