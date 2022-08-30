#Ashutosh Kumar Singh
#This code returns the number of unique elements in the list for boolean search
#
#Date: 30th Aug'22



import csv
import time
import os
import itertools
temp=[]
store=[]
new_k = []
n=4                                             #split_the_1st_row_in
N=50						#number of iterations for data set
def divide_chunks(l, n):
     
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]      

one=time.time()
for i in range(N):
    with open('data/spins_2x4_run_{}_.txt'.format(i)) as tsv:
        temp = [x.strip().split('\t') for x in tsv]
    temp[0] = [ int(x) for x in temp[0] ]
    
    a=list(divide_chunks(temp[0], n))
    #print(*a, sep = "\n")
    
    with open('data.txt','a') as wr:
        for lines in a:
            store.append(lines)
            wr.write(f"{lines}\n")
            #wr.write("%s\n" % lines)                   #use this for older python versions
two=time.time()
for elem in store:
    if elem not in new_k:
        new_k.append(elem)
store = new_k
print(*store, sep="\n")
print("Time taken to complete {} runs:".format(n),two-one)

os.remove('data.txt')
