import time
start_time=time.time()
fname2='./security_revised.log'
f2=open(fname2,'w')
with open('security.log','rb') as f:
    while(True):
        txt=f.read(500).decode('utf-8')
        if(txt==''):
            break
        txt=txt.replace('Jan','\nJan')
        txt=txt.replace('Feb','\nFeb')
        txt=txt.replace('Mar','\nMar')
        txt=txt.replace('Apr','\nApr')
        txt=txt.replace('May','\nMay')
        txt=txt.replace('Jun','\nJun')
        txt=txt.replace('Aug','\nAug')
        txt=txt.replace('Sep','\nSep')
        txt=txt.replace('Oct','\nOct')
        txt=txt.replace('Nov','\nNov')
        txt=txt.replace('Dec','\nDec')
        txt=txt.replace('Aug','\nSun')
        f2.write(txt)
        #print(txt)
    elapse=str(time.time()-start_time)
    print(elapse+' seconds elapsed\n')
    print(txt)
    f2.close()

