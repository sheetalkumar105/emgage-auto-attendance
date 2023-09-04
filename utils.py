import os
import json
import sys
from AttendanceCapture import AttendanceCapture

class Utils(object):

    property = ''
    latitude = ''
    longitude = ''
    dir_path = ''

    def __init__(self):
        pass

    def runInParallel(*fns):
        proc = []
        for fn in fns:
            p = Process(target=fn)
            p.start()
            proc.append(p)
        for p in proc:
            p.join()

    
    def runScript(self, data):
        self.callAttendance(data)

    def callAttendance(self, data):
        a = AttendanceCapture()
        try:
            a.execureSteps(data)
        except Exception as error:
            print('Unable run script' + str(error))


    def __str__(self):
        return "User(id='%s')" % self.id
