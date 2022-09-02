# Ashutosh Kumar Singh
#Run Digital Annealer for N iterations. 

# path:   /home/ashutosh/Digital_annealer/Digital_Annealer/bin_SI/2x16



import subprocess
import os
import time
import shutil

N=5000
one = time.time()
for i in range(N):
    subprocess.run(['./annealer_gpu_SI', '-a', 'J_Matrix_2x16.txt', '-l', 'linear_2x16.txt', '-x', '3', '-y', '0.01', '-n', '10', '-m', '100', '-d'])
    #time.sleep(3)
    filename='spins_2x16_run_{}_.txt'.format(i)
    os.rename('spins_2x16.txt',filename)
    target='run_2x16'
    shutil.move(filename,target)
    #time.sleep(2)
print("Done {} number of times".format(N))
two=time.time()
print("Time taken to complete {} runs: ".format(N),int(two-one), "seconds")

      
'''import shlex
print(shlex.split("./annealer_gpu_SI -a J_Matrix_4x4.txt -l linear_4x4.txt -x 6.4 -y 0.001 -n 35 -m 9000 -d"))'''