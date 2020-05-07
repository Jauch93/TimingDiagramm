# -*- coding: utf-8 -*-

from enum import Enum

class ProcessState(Enum):
    WAITING = 0
    ACTIVE = 1
    FINISHED = 2

class Process:
    
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.state = ProcessState.WAITING
        self.activeTime = 0
        
    def tickUpdate(self):
        if self.state == ProcessState.WAITING:
            print("Process " + str(self.name) + " inactive.")
            
        elif self.state == ProcessState.ACTIVE:
            print("Process " + str(self.name) + " active.")
            self.activeTime += 1
            if (self.activeTime == self.duration):
                self.state = ProcessState.FINISHED
                self.processFinished()
                self.activeTime = 0
        
        elif self.state == ProcessState.FINISHED:
            print("Process " + str(self.name) + " finished.")
            self.state = ProcessState.WAITING
            
    def isFinished(self):
        if self.state == ProcessState.FINISHED:
            return True
        return False
        
    def processFinished(self):
        pass
        
    def activate(self):
        self.state = ProcessState.ACTIVE