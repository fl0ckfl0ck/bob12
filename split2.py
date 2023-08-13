import time
start_time=time.time()
fname2='./security_revised_ver2.log'
f2=open(fname2,'w')
with open('security_revised.log','r') as f:
    while(True):
        txt=f.readline()
        if not txt:
            break
        if(len(txt)>200):
            line=txt[1:]
            line=line.replace('Jan','\nJan')
            line=line.replace('Feb','\nFeb')
            line=line.replace('Mar','\nMar')
            line=line.replace('Apr','\nApr')
            line=line.replace('May','\nMay')
            line=line.replace('Jun','\nJun')
            line=line.replace('Jul','\nJul')
            line=line.replace('Aug','\nAug')
            line=line.replace('Sep','\nSep')
            line=line.replace('Oct','\nOct')
            line=line.replace('Nov','\nNov')
            line=line.replace('Dec','\nDec')
            line=txt[0]+line
        f2.write(txt)     
    f2.close()
    elapse=str(time.time()-start_time)
    print(elapse+' seconds elapsed\n')
