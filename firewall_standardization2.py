import time, ipaddress
from datetime import datetime
start_time=time.time()
fname2='security_standard_ver2.log'
f2=open(fname2,'w')
#with open('sample.log','r', encoding='utf-8-sig') as f:
with open('security_standard_ver1.log','r', encoding='utf-8-sig') as f:
    while(True):
        txt=f.readline()
        if not txt:
            break
        t_line=txt.split(' ')
        timestamp=t_line[0]
        employee_id=t_line[1]
        source_ip=str(int(ipaddress.IPv4Address(t_line[2])))
        source_mac=str(int(t_line[3].replace(':',''),16))
        source_port=str(t_line[4])
        destination_ip=str(int(ipaddress.IPv4Address(t_line[6])))
        destination_mac=str(int(t_line[7].replace(':',''),16))
        destination_port=str(t_line[8])
        packet_size=str(t_line[9])
        line=timestamp+","+employee_id+","+source_ip+","+source_mac+","+source_port+","+destination_ip+","+destination_mac+","+destination_port+","+packet_size
        f2.write(line)
        
f2.close()
elapse=str(time.time()-start_time)
print(elapse+' seconds elapsed\n')