import numpy as np
#import matplotlib.pyplot as plt

import time
import os
import datetime
import math
from bluepy.btle import Scanner,DefaultDelegate
#part of UUID
#uuid="5204"
i = 0.5
str1 = "5204"
class ScanDelegate(DefaultDelegate):
    def _int_(self):
        DefaultDelegate.__init__(self)
        
    def handleDiscoverry(self,dev,isNewDev,isNewData):
        if isNewData:
            print("Discovered new data from",dev.addr)
        elif isNewData:
            print("Received new data from",dev.addr)
            
scanner=Scanner().withDelegate(ScanDelegate())
devices=scanner.scan(i)




def CalculateDistance (rssi,onerssi):
    " calculate the distance between Receiver and Transmitter "
    #1rssi:rssi of 1 meter away

    ratio=rssi/onerssi
    if ratio<1 :
        return math.pow(ratio,10)
    else :
        # distance=(0.89976)*math.pow(ratio,7.7095)+0.111
        # return distance
        distance=math.pow(10,abs(rssi-onerssi)/(10 * 2.5))

        return distance
sample_count = 0

#while  sample_count <= 10:
#     True:
#     scanner=Scanner().withDelegate(ScanDelegate())
#     returnedList =scanner.parse_events(sock, 5)
for dev in devices:
    for(adtype,desc,value) in dev.getScanData():
        if str(value).find(str1)!=-1:
                
            rssi = dev.rssi
            # txPower = dev.txPower
            rssi_feedback = -dev.rssi
            # output current time
            print(datetime.datetime.now().strftime('%H:%M:%S'))
            print("Devices %s (%s),RSSI=%d dB" % (dev.addr,dev.addrType,dev.rssi))
            print("%s= %s" % (desc,value))
sample_count = sample_count + 1            
if sample_count == 1:
    scanner=Scanner().withDelegate(ScanDelegate())
    devices=scanner.scan(i)

    for dev in devices:
        for(adtype,desc,value) in dev.getScanData():
            if str(value).find(str1)!=-1:
                
                rssi = dev.rssi
                # txPower = dev.txPower
                rssi_feedback = -dev.rssi
                # output current time
                print(datetime.datetime.now().strftime('%H:%M:%S'))
                print("Devices %s (%s),RSSI=%d dB" % (dev.addr,dev.addrType,dev.rssi))
                print("%s= %s" % (desc,value))
                RSSI1 = rssi
                print ("RSSI1 = ", RSSI1)
                RSSI_FB1 = rssi_feedback
                print (RSSI_FB1)
sample_count = sample_count + 1 
if sample_count == 2:
    scanner=Scanner().withDelegate(ScanDelegate())
    devices=scanner.scan(i)

    for dev in devices:
        for(adtype,desc,value) in dev.getScanData():
            if str(value).find(str1)!=-1:
                
                rssi = dev.rssi
                # txPower = dev.txPower
                rssi_feedback = -dev.rssi
                # output current time
                print(datetime.datetime.now().strftime('%H:%M:%S'))
                print("Devices %s (%s),RSSI=%d dB" % (dev.addr,dev.addrType,dev.rssi))
                print("%s= %s" % (desc,value))
                RSSI2 = rssi
                print ("RSSI2 = ", RSSI2)
                RSSI_FB2 = rssi_feedback
                print (RSSI_FB2)
sample_count = sample_count + 1 
if sample_count == 3:
    scanner=Scanner().withDelegate(ScanDelegate())
    devices=scanner.scan(i)

    for dev in devices:
        for(adtype,desc,value) in dev.getScanData():
            if str(value).find(str1)!=-1:
                
                rssi = dev.rssi
                # txPower = dev.txPower
                rssi_feedback = -dev.rssi
                # output current time
                print(datetime.datetime.now().strftime('%H:%M:%S'))
                print("Devices %s (%s),RSSI=%d dB" % (dev.addr,dev.addrType,dev.rssi))
                print("%s= %s" % (desc,value))
                RSSI3 = rssi
                print ("RSSI3 = ", RSSI3)
                RSSI_FB3 = rssi_feedback
                print (RSSI_FB3)
sample_count = sample_count + 1 
if sample_count == 4:
    scanner=Scanner().withDelegate(ScanDelegate())
    devices=scanner.scan(i)

    for dev in devices:
        for(adtype,desc,value) in dev.getScanData():
            if str(value).find(str1)!=-1:
                
                rssi = dev.rssi
                # txPower = dev.txPower
                rssi_feedback = -dev.rssi
                # output current time
                print(datetime.datetime.now().strftime('%H:%M:%S'))
                print("Devices %s (%s),RSSI=%d dB" % (dev.addr,dev.addrType,dev.rssi))
                print("%s= %s" % (desc,value))
                RSSI4 = rssi
                print ("RSSI4 = ", RSSI4)
                RSSI_FB4 = rssi_feedback
                print (RSSI_FB4)
sample_count = sample_count + 1 
if sample_count == 5:
    scanner=Scanner().withDelegate(ScanDelegate())
    devices=scanner.scan(i)

    for dev in devices:
        for(adtype,desc,value) in dev.getScanData():
            if str(value).find(str1)!=-1:
                
                rssi = dev.rssi
                # txPower = dev.txPower
                rssi_feedback = -dev.rssi
                # output current time
                print(datetime.datetime.now().strftime('%H:%M:%S'))
                print("Devices %s (%s),RSSI=%d dB" % (dev.addr,dev.addrType,dev.rssi))
                print("%s= %s" % (desc,value))
                RSSI5 = rssi
                print ("RSSI5 = ", RSSI5)
                RSSI_FB5 = rssi_feedback
                print (RSSI_FB5)
sample_count = sample_count + 1 
if sample_count == 6:
    scanner=Scanner().withDelegate(ScanDelegate())
    devices=scanner.scan(i)

    for dev in devices:
        for(adtype,desc,value) in dev.getScanData():
            if str(value).find(str1)!=-1:
                
                rssi = dev.rssi
                # txPower = dev.txPower
                rssi_feedback = -dev.rssi
                # output current time
                print(datetime.datetime.now().strftime('%H:%M:%S'))
                print("Devices %s (%s),RSSI=%d dB" % (dev.addr,dev.addrType,dev.rssi))
                print("%s= %s" % (desc,value))
                RSSI6 = rssi
                print ("RSSI6 = ", RSSI6)
                RSSI_FB6 = rssi_feedback
                print (RSSI_FB6)
sample_count = sample_count + 1 
if sample_count == 7:
    scanner=Scanner().withDelegate(ScanDelegate())
    devices=scanner.scan(i)

    for dev in devices:
        for(adtype,desc,value) in dev.getScanData():
            if str(value).find(str1)!=-1:
                
                rssi = dev.rssi
                # txPower = dev.txPower
                rssi_feedback = -dev.rssi
                # output current time
                print(datetime.datetime.now().strftime('%H:%M:%S'))
                print("Devices %s (%s),RSSI=%d dB" % (dev.addr,dev.addrType,dev.rssi))
                print("%s= %s" % (desc,value))
                RSSI7 = rssi
                print ("RSSI7 = ", RSSI7)
                RSSI_FB7 = rssi_feedback
                print (RSSI_FB7)
sample_count = sample_count + 1 
if sample_count == 8:
    scanner=Scanner().withDelegate(ScanDelegate())
    devices=scanner.scan(i)

    for dev in devices:
        for(adtype,desc,value) in dev.getScanData():
            if str(value).find(str1)!=-1:
                
                rssi = dev.rssi
                # txPower = dev.txPower
                rssi_feedback = -dev.rssi
                # output current time
                print(datetime.datetime.now().strftime('%H:%M:%S'))
                print("Devices %s (%s),RSSI=%d dB" % (dev.addr,dev.addrType,dev.rssi))
                print("%s= %s" % (desc,value))
                RSSI8 = rssi
                print ("RSSI8 = ", RSSI8)
                RSSI_FB8 = rssi_feedback
                print (RSSI_FB8)
sample_count = sample_count + 1 
if sample_count == 9:
    scanner=Scanner().withDelegate(ScanDelegate())
    devices=scanner.scan(i)

    for dev in devices:
        for(adtype,desc,value) in dev.getScanData():
            if str(value).find(str1)!=-1:
                
                rssi = dev.rssi
                # txPower = dev.txPower
                rssi_feedback = -dev.rssi
                # output current time
                print(datetime.datetime.now().strftime('%H:%M:%S'))
                print("Devices %s (%s),RSSI=%d dB" % (dev.addr,dev.addrType,dev.rssi))
                print("%s= %s" % (desc,value))
                RSSI9 = rssi
                print ("RSSI9 = ", RSSI9)
                RSSI_FB9 = rssi_feedback
                print (RSSI_FB9)
sample_count = sample_count + 1 
if sample_count == 10:
    scanner=Scanner().withDelegate(ScanDelegate())
    devices=scanner.scan(i)

    for dev in devices:
        for(adtype,desc,value) in dev.getScanData():
            if str(value).find(str1)!=-1:
                
                rssi = dev.rssi
                # txPower = dev.txPower
                rssi_feedback = -dev.rssi
                # output current time
                print(datetime.datetime.now().strftime('%H:%M:%S'))
                print("Devices %s (%s),RSSI=%d dB" % (dev.addr,dev.addrType,dev.rssi))
                print("%s= %s" % (desc,value))
                RSSI10 = rssi
                print ("RSSI10 = ", RSSI10)
                RSSI_FB10 = rssi_feedback
                print (RSSI_FB10)
sample_count = sample_count + 1 


# n_iter = 10
# sz = (n_iter,) # size of array
# z = [RSSI1,  RSSI2, RSSI3,  RSSI4,  RSSI5, RSSI6, RSSI7,  RSSI8,RSSI9,  RSSI10] 
# RSSI_m = np.median(z)
# value_1 = 1/abs(RSSI1-RSSI_m)
# value_2 = 1/abs(RSSI2-RSSI_m)
# value_3 = 1/abs(RSSI3-RSSI_m)
# value_4 = 1/abs(RSSI4-RSSI_m)
# value_5 = 1/abs(RSSI5-RSSI_m)
# value_6 = 1/abs(RSSI6-RSSI_m)
# value_7 = 1/abs(RSSI7-RSSI_m)
# value_8 = 1/abs(RSSI8-RSSI_m)
# value_9 = 1/abs(RSSI9-RSSI_m)
# value_10 = 1/abs(RSSI10-RSSI_m)

# #RSSI_AVG = (RSSI1 * value_1+ RSSI2 * value_2 + RSSI3 * value_3 + RSSI4 * value_4 + RSSI5 * value_5 +RSSI6 * value_6 + RSSI7 * value_7 + RSSI8 * value_8 + RSSI9 * value_9 + RSSI10 * value_10)/(value_1+value_2+value_3+value_4+value_5+value_6+value_7+value_8+value_9+value_10)
# #RSSI_FBAVG = (RSSI_FB1 + RSSI_FB2 + RSSI_FB3 + RSSI_FB4 + RSSI_FB5 + RSSI_FB6 + RSSI_FB7 + RSSI_FB8 + RSSI_FB9 + RSSI_FB10 )/10.0
# print ("Average = ",RSSI_m)
# # print ("FB Average = ",RSSI_FBAVG)
# sample_count = 0
# distance=CalculateDistance (RSSI_m,-61.0)
# print("distance is %s" % distance)
###########################################################################################################################################################333
#Kalman Filter
""" plt.rcParams['figure.figsize'] = (10, 8)

# intial parameters
""" 

n_iter = 10
sz = (n_iter,) # size of array
z = [RSSI1,  RSSI2, RSSI3,  RSSI4,  RSSI5, RSSI6, RSSI7,  RSSI8,RSSI9,  RSSI10]
Q = 1e-5 #process variance
# allocate space for arrays?
xhat=np.zeros(sz)      # a posteri estimate of x
P=np.zeros(sz)         # a posteri error estimate
xhatminus=np.zeros(sz) # a priori estimate of x
Pminus=np.zeros(sz)    # a priori error estimate
K=np.zeros(sz)         # gain or blending factor

R = 0.1**2 # estimate of measurement variance, change to see effect

# intial guesses
xhat[0] = -28.0
P[0] = 5.0

for k in range(1,n_iter):
    # time update
    xhatminus[k] = xhat[k-1]
    Pminus[k] = P[k-1]+Q

    # measurement update
    K[k] = Pminus[k]/( Pminus[k]+R )
    xhat[k] = xhatminus[k]+K[k]*(z[k]-xhatminus[k])
    P[k] = (1-K[k])*Pminus[k]

# plt.figure()
# plt.plot(z,'k+',label='noisy measurements')
# plt.plot(xhat,'b-',label='a posteri estimate')
# plt.legend()
# plt.title('Estimate vs. iteration step', fontweight='bold')
# plt.xlabel('Iteration')
# plt.ylabel('Received Signal Strength Indicator')
# plt.show()

print(xhat[k])
distance=CalculateDistance (xhat[k],-64.0)
print("distance is %s" % distance)





#Broadcasting beacon
#GPIO.output(16, True)
# cid = '1E 02 01 1A 1A FF 4C 00 02 15 E2 0A 39 F4 73 F5 4B C4 A1 2F 17 D2 AE 08 A9 61'
# aid = 30  # -> '00 00'
# uid = int(RSSI_AVG)  # -> '00 00'
# power = -59  # -> 'CA'
#Initialize iBeacon
# ib = iBeacon(cid , aid , uid , power)
# #Start broadcasting
# ib.startBeacon()
