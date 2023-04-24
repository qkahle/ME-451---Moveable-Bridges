import pychrono.core as chrono
import pychrono.irrlicht as chronoirr
import pychrono.vehicle as veh
import matplotlib.pyplot as plt
import numpy as np

#import pychrono as chrono
system = chrono.ChSystemNSC()
system.Set_G_acc(chrono.ChVectorD(0, -9.81, 0))

# create contact material for handling contact
mat = chrono.ChMaterialSurfaceNSC()
mat.SetFriction(.4)

table_thickness = 0.2
table_pos_y = -1.2
table = chrono.ChBodyEasyBox(5, table_thickness, 5, 1000, True, True, mat)
system.AddBody(table)
table.SetIdentifier(2)
table.SetBodyFixed(True)
table.SetName("table")
table.SetPos(chrono.ChVectorD(0, table_pos_y, 0))
table.GetVisualShape(0).SetColor(chrono.ChColor(1, 0.2, 0.2))

vis = chronoirr.ChVisualSystemIrrlicht()
vis.AttachSystem(system)
# vis.SetWindowSize(1024,768)
vis.SetWindowSize(1920, 1080)
vis.SetWindowTitle('slider crank demo')
vis.Initialize()
vis.AddSkyBox()
vis.AddCamera(chrono.ChVectorD(-0.5, 0.5, 3))
vis.AddTypicalLights()

time_end = 4

while (vis.Run() and system.GetChTime() < time_end):
    
    print(system.GetChTime())

    vis.BeginScene() 
    vis.Render()
    vis.EndScene()
    system.DoStepDynamics(5e-3)   
    