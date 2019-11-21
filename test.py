#!/usr/bin/env python2
# -*- coding: utf-8 -*-

 
import time, math, datetime
import numpy as np
from os import getcwd
from threading import Thread
from bluepy.btle import Scanner, DefaultDelegate


class KalmanFilter(object):
    def __init__(self, process_variance,estimated_measurement_variance):
        self.process_variance = process_variance
        self.estimated_measurement_variance = estimated_measurement_variance
        self.posteri_estimate = 1.0
        self.posteri_error_estimate = 2.0

    def input_latest_noisy_measurement(self, measurement):
        priori_estimate = self.posteri_estimate
        priori_error_estimate = self.posteri_error_estimate + self.process_variance

        blending_factor = priori_error_estimate / (priori_error_estimate + self.estimated_measurement_variance)
        self.posteri_estimate = priori_estimate + blending_factor * (measurement - priori_estimate)
        self.posteri_error_estimate = (1 - blending_factor) * priori_error_estimate

    def get_latest_estimated_measurement(self):
        return self.posteri_estimate


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        self.RSSI = self.DEV = self.dist = self.dist_kal = 0
        self.stoppped = False

        self.process_variance = 1e-3
        self.estimated_measurement_variance = 0.4 ** 2 
        self.kalman_filter = KalmanFilter(self.process_variance, self.estimated_measurement_variance)
        DefaultDelegate.__init__(self)
        self.scanner = Scanner()

    def stop(self):
        self.stopped = True

    def start(self):
        # start the thread to read frames from the device output
        Thread(target=self.update, name="iBeacon").start()
        print("Staring ibeacon")
        return self

    def distance(self, n=2.5, txpower=-63.5):
        if(self.RSSI/txpower)<1:
            return(math.pow(self.RSSI/txpower,10))
        else:
        #return (abs(self.RSSI)/(10.0*n*math.log10(math.exp(1)))) - (txpower/(10.0*n*math.log10(math.exp(1)))) # convert RSSI to Distance
            return(math.pow(10,abs(self.RSSI-txpower)/(10*n)))
    def update_file(self):
        f = open('ibeacon.txt', 'w')
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        string = '%s\t%2.2f' % (st, self.dist_kal)
        f.write(string)
        f.close()

    def update(self):
         #prctl.set_name("iBeacon")
        count = 0
        while(not self.stoppped):
            try:
                devices = self.scanner.scan(0.1)
                for dev in devices:
                    # print(dev.addr)
                    for(adtype,desc,value) in dev.getScanData():
                        if str(value).find("5204")!=-1 :
                            self.RSSI = dev.rssi
                            self.DEV = dev.addr
                            self.dist = self.distance()
                            self.kalman_filter.input_latest_noisy_measurement(self.dist)
                            self.dist_kal = self.kalman_filter.get_latest_estimated_measurement()
                            self.update_file()
                            count = 0
                        #print "Device %s, RSSI=%d dB" % (dev.addr,dev.rssi)
            except:
                self.dist_kal = 0
                if count >= 4:
                    print("no ibeacon found")
                    self.update_file()
                count += 1
                time.sleep(1)

class iBeacon():
    def __init__(self):
        self.scan = ScanDelegate()
        self.scanner = self.scan.scanner.withDelegate(self.scan)
        self.scan.start()

if __name__ == "__main__":


    beacon = iBeacon()

    while(1):
        print("RSSI: %s/n Distance: %s/n Kalmann distance: %s/n" %(beacon.scan.RSSI, beacon.scan.dist, beacon.scan.dist_kal))
        time.sleep(0.5)

