import csv
import time
import os
temp=[]
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
    a=list(divide_chunks(temp[0], n))
    print(*a, sep = "\n")




    with open('data.txt','a') as wr:
        #wr.write("Run {} \n".format(i) )
        for lines in a:
            #res=  str(lines)[1:-1]
            #res = [i.replace('"', '') for i in res]
            wr.write(f"{lines}\n")
        #wr.write("************************************ \n")
two=time.time()

#List = open("data.txt").readlines()
#print(*List, sep = "\n")    
# sort_and_deduplicate(List)
# print(*List, sep = "\n")
# mylist2=[]
# for thing in List:
#     thing=tuple(thing)
#     mylist2.append(thing)
# set(mylist2)
# print(mylist2)    
print("Time taken to complete {} runs:".format(n),two-one)

os.remove('data.txt')