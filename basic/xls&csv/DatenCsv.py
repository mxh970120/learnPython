# -*- coding: utf-8 -*-
#import python packet 
from base64 import b64encode
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from twisted.internet.task import LoopingCall
from twisted.internet import ssl
from datetime import datetime
import os
import csv
from collections import OrderedDict




class Klasse(ApplicationSession):
    def __init__(self, config=None):

        ApplicationSession.__init__(self, config)
        self.MeterDataClamp = ['Clamp08']
        self.MeterDataKey = ['U1', 'U2', 'U3', 'I1', 'I2', 'I3', 'P1', 'P2', 'P3', 'Q1', 'Q2', 'Q3']
        self.WizDataClamp = ['Clamp1']
        self.WizDataKey = ['U1', 'U2', 'U3', 'I1', 'I2', 'I3', 'P1', 'P2', 'P3', 'Q1', 'Q2', 'Q3', 'f1', 'f2', 'f3']
        self.timestampKey = 'TimestampSYS'

        self.DataDict = {}

        self.csvName = 'WAGO_Messung_' + datetime.now().strftime('%Y%m%d_%H%M') + '.csv'
   
    def readMeter494(self, data):
        MeterDataDict = OrderedDict()
        for clamp in self.MeterDataClamp:
            time = datetime.fromtimestamp(int(data[clamp]['TimestampSYS'] / 1000)).strftime('%H:%M:%S')
            MeterDataDict['Time'] = time
            for key in self.MeterDataKey:
                MeterDataDict['Meter' + '_' + clamp + '_' + key] = data[clamp][key]

        if time in self.DataDict.keys():
            self.DataDict[time].update(MeterDataDict)
        else:
            self.DataDict[time] = MeterDataDict


    def readWiz495(self, data):
        WizDataDict = OrderedDict()
        for clamp in self.WizDataClamp:
            time = datetime.fromtimestamp(int(data[clamp]['TimestampSYS'] / 1000)).strftime('%H:%M:%S')
            WizDataDict['Time'] = time
            for key in self.WizDataKey:
                WizDataDict['Wiz' + '_' + clamp + '_' + key] = data[clamp][key]

        if time in self.DataDict.keys():
            self.DataDict[time].update(WizDataDict)
        else:
            self.DataDict[time] = WizDataDict


    def speichernCSV(self):
        print("speichern")
        csv_exists = os.path.isfile(self.csvName)
        speichernTime = []
        for time in self.DataDict.keys():
            if len(self.DataDict[time]) == 1 + len(self.MeterDataClamp)*len(self.MeterDataKey) + len(self.WizDataClamp)*len(self.WizDataKey):
                with open(self.csvName, 'a', newline = "") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=self.DataDict[time].keys())
                    if not csv_exists:
                        writer.writeheader()
                        csv_exists = True
                    writer.writerow(self.DataDict[time])
                speichernTime.append(time)

        for time in speichernTime:
            del self.DataDict[time]

    def onJoin(self, details):
        "Callback fired when WAMP session has been established."
        ApplicationSession.onJoin(self,details)
        print("onJoin")

        self.subscribe(self.readMeter494, u'')
        self.subscribe(self.readWiz495, u'')
        
        Loop = LoopingCall(self.speichernCSV)
        Loop.start(1)

    def onLeave(self, details):
        "Callback fired when WAMP session has is closed"
        ApplicationSession.onLeave(self, details)
        print("onLeave")



   