import numpy as np
import csv


def multiply_matrix(A,B):
    result=[]
    # iterating by row of A
    for i in range(len(A)):
    
        # iterating by column by B
        for j in range(1):
    
            # iterating by rows of B
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[j][k]
    return result



H=[[1,1],[1,-1]]
H2=np.kron(H,H)
H4=np.kron(H2,H2)
H6=np.kron(H4,H2)
#print(H6)
print(*H6,sep="\n")
line=[]
num=[]
# with open("data_unique_50.txt",'r') as f:
#     for i in f.readlines():
#         line.append(i.rstrip())
#     #print(f.readline())
# #print(multiply_matrix(H2,line[0]))
with open('data_unique.txt', 'r') as f:
    data = csv.reader(f)
    data_lst = []
    for line in data:
        data_lst.append([int(x) for x in line])


#print((data_lst))

# for i in range(len(data_lst)):
#     print(H6@data_lst[i])
# #print(multiply_matrix(H2,data_lst[0]))