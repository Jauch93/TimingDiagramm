# -*- coding: utf-8 -*-

import Tkinter as tk
import TimingDiagramm as TD
import Process as PR

class TimingDiagrammGui:
    def __init__(self):
        # Prepare BusinessLogic
        self.diagramm = TD.TimingDiagramm()
        
        self.processWidget = []
        
        # Build GUI
        self.top = tk.Tk()
        
        self.top.title('TimingDiagramm')
        #You can set the geometry attribute to change the root windows size
        self.top.geometry("1000x200") #You want the size of the app to be 500x500
        self.top.resizable(0, 0) #Don't allow resizing in the x or y direction
        
        self.addProcessButton = tk.Button(self.top, text ="AddProcess", command = self.addProcessCb)
        self.addProcessButton.pack()
        
        self.top.mainloop()
        
        
    def update(self):
        print("updating")
        for process in self.processWidget:
            process.update()
        
    def addProcessCb(self):
        AddProcessDialog(self)#self.top, self.diagramm)

class AddProcessDialog:
    def __init__(self, parentWindow):
        self.parent = parentWindow
        self.diagramm = parentWindow.diagramm
        self.addProcessDialog = tk.Toplevel(self.parent.top)
        self.addProcessDialog.title('Add Process')
        #You can set the geometry attribute to change the root windows size
        self.addProcessDialog.geometry("200x200") #You want the size of the app to be 500x500
        self.addProcessDialog.resizable(0, 0) #Don't allow resizing in the x or y direction
        
        nameLabel = tk.Label(self.addProcessDialog, text="ProcessName: ")
        nameLabel.pack() 
        
        self.nameTextBox = tk.Text(self.addProcessDialog, height=1, width=20)
        self.nameTextBox.insert(tk.END, "Unnamed")
        self.nameTextBox.pack()
        
        durationLabel = tk.Label(self.addProcessDialog, text="ProcessDuration: ")
        durationLabel.pack() 
        
        self.durationTextBox = tk.Text(self.addProcessDialog, height=1, width=5)
        self.durationTextBox.insert(tk.END, "0")
        self.durationTextBox.pack()
        
        self.submitButton = tk.Button(self.addProcessDialog, text ="AddProcess", command = self.addProcessCb)
        self.submitButton.pack()
        
        self.addProcessDialog.mainloop()
        
    def addProcessCb(self):
        process = PR.Process(self.nameTextBox.get("1.0", "end-1c"), int(self.durationTextBox.get("1.0", "end-1c")))
        self.diagramm.addProcess(process)
        self.parent.processWidget.append(ProcessEntry(process,self.parent))
        print(self.diagramm.processes[0].name)

        self.parent.update()
        
        self.addProcessDialog.destroy()
        
class ProcessEntry:
    def __init__(self, process, topWindow):
        self.top = topWindow.top
        self.process = process
        
    def update(self):
        self.nameLabel = tk.Label(self.top, text=self.process.name)
        self.nameLabel.pack() 
        
        self.durationLabel = tk.Label(self.top, text=self.process.duration)
        self.durationLabel.pack()
        
    
gui = TimingDiagrammGui()
#gui = AddProcessDialog()