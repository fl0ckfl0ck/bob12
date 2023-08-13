import time
from datetime import datetime
start_time=time.time()
fname2='security_standard_ver1.log'
f2=open(fname2,'w')
with open('security_revised_ver2.log','r', encoding='utf-8-sig') as f:
    while(True):
        txt=f.readline()
        if not txt:
            break
        txt=txt.replace('BoB_Forensics ','')
        txt_split=txt.split(' ',5)
        month=txt_split[0]
        day=txt_split[1]
        year=txt_split[2]
        time=txt_split[4]
        timestampSTRING=year+'-'+month+'-'+day+' '+time
        timestampFORMAT="%Y-%b-%d %H:%M:%S"
        timestamp=str(int(datetime.strptime(timestampSTRING,timestampFORMAT).timestamp()))
        line=str(timestamp) + " " + txt_split[5]
        f2.write(line)
    f2.close()
    elapse=str(time.time()-start_time)
print(elapse+' seconds elapsed\n')

