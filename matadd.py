r=int(input("Enter rows: "))
c=int(input("Enter columns: "))
A=[]
B=[]
print("Enter Matrix A:")
for i in range(r):
    row=[]
    for j in range(c):
        row.append(int(input()))
    A.append(row)
print("Enter Matrix B:")
for i in range(r):
    row=[]
    for j in range(c):
        row.append(int(input()))
    B.append(row)
print("Addition:")
for i in range(r):
    for j in range(c):
        print(A[i][j]+B[i][j],end=" ")
    print()