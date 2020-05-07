# -*- coding: utf-8 -*-

class TimingDiagramm:
    
    def __init__(self):
        self.processes = []
        self.conditions = []
        self.tickCount = 0
    
    def generate(self, tickCount):
        for i in range(0, tickCount):
            self.tickUpdate()
    
    def addProcess(self, process):
        self.processes.append(process)
    
    def addCondition(self, cond):
        self.conditions.append(cond)
        
    def tickUpdate(self):
        self.tickCount += 1
        
        # Check Conditions
        for cond in self.conditions:
            cond.tickUpdate()
            
        # Update All Processes
        for process in self.processes:
            process.tickUpdate()