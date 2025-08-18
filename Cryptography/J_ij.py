import numpy as np


H=[[1,1],[1,-1]]

H2=np.kron(H,H)
H4=np.kron(H2,H2)
H6=np.kron(H4,H2)
H8=np.kron(H6,H2)
H10=np.kron(H8,H2)
#print(*H2, sep="\n")
#print(H2[1][3])
n=len(H10)                             #size of matrix
#with open("J_ij.txt" as w):
#print(len(H2))
with open("J_ij_.{}.txt".format(n) ,"w") as f:
    for i in range(n):
        for j in range(n):
            #print(i+1,' ',j+len(H2)+1,' ', H2[i][j])
            f.write(str(i+1)+ ' ' + str(j+n+1)+' '+ str(H10[i][j]) + "\n" )