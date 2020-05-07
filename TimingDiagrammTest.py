# -*- coding: utf-8 -*-

from Condition import Condition
from Process import Process
from TimingDiagramm import TimingDiagramm

diagramm = TimingDiagramm()

cond = Condition()
cond2 = Condition()

process1 = Process("WUTSCHELN", 3)

process2 = Process("WEDELN", 4)

cond.setDependingProcess(process1)
cond.setWakingProcess(process2)

cond2.setDependingProcess(process2)
cond2.setWakingProcess(process1)

diagramm.addProcess(process1)
diagramm.addProcess(process2)
diagramm.addCondition(cond)
diagramm.addCondition(cond2)

diagramm.tickUpdate()
process1.activate()
diagramm.generate(10)