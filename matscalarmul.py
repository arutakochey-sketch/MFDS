r=int(input("Enter rows: "))
c=int(input("Enter columns: "))
A=[]
print("Enter Matrix:")
for i in range(r):
    row=[]
    for j in range(c):
        row.append(int(input()))
    A.append(row)
x=int(input("Enter scalar: "))
print("Result:")
for i in range(r):
    for j in range(c):
        print(A[i][j]*x,end=" ")
    print()