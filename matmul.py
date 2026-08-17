r1=int(input("Rows of A: "))
c1=int(input("Columns of A: "))
r2=int(input("Rows of B: "))
c2=int(input("Columns of B: "))
if c1!=r2:
    print("Multiplication not possible")
else:
    A=[]
    B=[]
    print("Enter Matrix A:")
    for i in range(r1):
        row=[]
        for j in range(c1):
            row.append(int(input()))
        A.append(row)
    print("Enter Matrix B:")
    for i in range(r2):
        row=[]
        for j in range(c2):
            row.append(int(input()))
        B.append(row)
    result=[]
    for i in range(r1):
        row=[]
        for j in range(c2):
            s=0
            for k in range(c1):
                s=s+A[i][k]*B[k][j]
            row.append(s)
        result.append(row)
    print("Multiplication:")
    for row in result:
        print(row)