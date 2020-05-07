# -*- coding: utf-8 -*-

from enum import Enum

class ConditionState(Enum):
    WAITING = 0
    TRIGGERED = 1

class Condition:
    def __init__(self):
        self.dependingProcess = None
        self.wakingProcess = None
        
    def setDependingProcess(self, process):
        self.dependingProcess = process
        
    def setWakingProcess(self, process):
        self.wakingProcess = process
        
    def tickUpdate(self):
        if self.dependingProcess.isFinished():
            self.wakingProcess.activate()