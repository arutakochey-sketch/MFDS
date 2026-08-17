r=int(input("Enter rows: "))
c=int(input("Enter columns: "))
A=[]
print("Enter Matrix:")
for i in range(r):
    row=[]
    for j in range(c):
        row.append(int(input()))
    A.append(row)
print("Transpose:")
for j in range(c):
    for i in range(r):
        print(A[i][j],end=" ")
    print()