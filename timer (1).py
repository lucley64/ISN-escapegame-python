import time

montemps=time.time()
while(1):
    y=time.time()-montemps
    time.sleep(1)
    print (time.localtime(y)[3]-1,'h',time.localtime(y)[4],'min',time.localtime(y)[5],'s')
    if time.localtime(y)[3]-1>=1:
        break
print('fin')