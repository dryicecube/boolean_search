#Ashutosh Kumar Singh
#This code returns the number of unique elements in the list for boolean search
#
#Date: 30th Aug'22

# /home/ashutosh/Digital_annealer/Data_analysis/2x16

import csv
import time
import os
import itertools
temp=[]
store=[]
new_k = []
n=16                                           #split_the_1st_row_in
N=5000                                            #number of iterations for data set
def divide_chunks(l, n):
     
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]      

one=time.time()
for i in range(N):
    with open('run_2x16_100steps_5000/spins_2x16_run_{}_.txt'.format(i)) as tsv:
        temp = [x.strip().split('\t') for x in tsv]
    temp[0] = [ int(x) for x in temp[0] ]
    
    a=list(divide_chunks(temp[0], n))
    #print(*a, sep = "\n")
    
    with open('data__100_steps5000.txt','a') as wr:
        for lines in a:
            store.append(lines)
            #wr.write(f"{lines}\n")
            wr.write("%s\n" % lines)
two=time.time()
for elem in store:
    if elem not in new_k:
        new_k.append(elem)
store = new_k
with open('data_unique_100steps_5000.txt','w') as f:
    for lines in store:
        lines = str(lines)[1:-1]
        f.write("%s\n" % lines)
        #wr.write(f"{lines}\n")
print(*store, sep="\n")
print("Time taken to complete {} runs:".format(n),two-one)

#os.remove('data.txt')
