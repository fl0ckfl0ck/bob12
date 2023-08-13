import time
start_time=time.time()
with open('security_revised_ver2.log','r') as f:
    while(True):
        txt=f.readline()
        if not txt:
            break
        if(len(txt)>150):
            print(txt)
    elapse=str(time.time()-start_time)
    print(elapse+' seconds elapsed\n')
