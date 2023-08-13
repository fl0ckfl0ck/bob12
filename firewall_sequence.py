import time, ipaddress
from datetime import datetime
start_time=time.time()

fname2='security_0.log'
sequence=1
f2=open(fname2,'w')
#with open('sample.log','r', encoding='utf-8-sig') as f:
with open('security_standard_ver2.log','r', encoding='utf-8-sig') as f:
    while(True):
        if(sequence%10000000==0):
            f2.close()
            fname2='security_'+str(int(sequence/10000000))+".log"
            f2=open(fname2,'w')
        txt=f.readline()
        if not txt:
            break
        line=str(sequence)+','+txt
        f2.write(line)
        sequence+=1
f2.close()
elapse=str(time.time()-start_time)
print(elapse+' seconds elapsed\n')

