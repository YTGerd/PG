import time
import math
from bluepy.btle import Scanner,DefaultDelegate


class ScanDelegate(DefaultDelegate):
    def _int_(self):
        DefaultDelegate.__init__(self)
        
    def handleDiscoverry(self,dev,isNewDev,isNewData):
        if isNewData:
            print("Discovered new data from",dev.addr)
        elif isNewData:
            print("Received new data from",dev.addr)
            




def CalculateDistance (rssi,onerssi):
    " calculate the distance between Receiver and Transmitter "
    # 1rssi:rssi of 1 meter away
    ratio=rssi/onerssi
    if ratio<1 :
        return math.pow(ratio,10)
    else :
        distance=(0.89976)*math.pow(ratio,7.7095)+0.111
        return distance


def getCharacteristic ():
    
    scanner=Scanner().withDelegate(ScanDelegate())
    devices=scanner.scan(0.3)
    for dev in devices:
        for(adtype,desc,value) in dev.getScanData():

            
            if str(value).find("8856")!=-1:
            # timestamp
               
                t=time.time()
                distance=CalculateDistance (dev.rssi,-60)
                uuid="8856"
               # print("distance is %s" % distance)
                usefulInformation=("%s ,%s ,%s " % (t,distance,uuid))
                
                
                return usefulInformation
    return("cannot detect the target object")
   







