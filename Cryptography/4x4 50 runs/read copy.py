import csv
import time
import os
import itertools
temp=[]
store=[]
n=4                                             #split_the_1st_row_in
def divide_chunks(l, n):
     
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]      

one=time.time()
for i in range(50):
    with open('data/spins_4x4_run_{}_.txt'.format(i)) as tsv:
        temp = [x.strip().split('\t') for x in tsv]
        #for line in csv.reader(tsv, dialect="excel-tab"):
            #print(line)

        #print( list(zip(*(line.strip().split('\t') for line in inp))) )    

    #print(temp[0])
    temp[0] = [ int(x) for x in temp[0] ]
    #temp[0] = str(temp[0])[1:-1]
    a=list(divide_chunks(temp[0], n))
    #print(*a, sep = "\n")
    #print(a)




    with open('data.txt','a') as wr:
        #wr.write("Run {} \n".format(i) )
        for lines in a:
            #res=  str(lines)[1:-1]
            #res = [i.replace('"', '') for i in res]
            store.append(lines)
            wr.write(f"{lines}\n")
        #wr.write("************************************ \n")
two=time.time()
#store.sort()
new_k = []
for elem in store:
    if elem not in new_k:
        new_k.append(elem)
store = new_k
#print store
#list(store for store,_ in itertools.groupby(store))
    # lines = rd.readlines()   
    # lines = [line.rstrip() for line in lines]
print(*store, sep="\n")
print("Time taken to complete {} runs:".format(n),two-one)

os.remove('data.txt')