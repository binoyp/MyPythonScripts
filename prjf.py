import rhinoscriptsyntax as rs
import math

x1 = rs.GetPoint("Pick start point")
x2 = rs.GetPoint("Pick end point")
h = rs.GetPoint("Pick a point above deck")
n = rs.GetInteger("Number of stations", 30, 0)
dx = rs.Distance(x1,x2)/ n


#  file for saving shf file
surface = rs.GetObject("Select surface to project onto", rs.filter.surface)
filter = "Text File (*.shf)|*.shf|All Files (*.*)|*.*||"
filename = rs.SaveFileName("Save point coordinates as", filter)
###

file = open( filename, "w" )
file.write("hull \n")

for i in range(1,n):
    flg_stn = 1
    c1= (x1[0] - i*dx, x1[1], x1[2])
    c2= (x1[0] - i*dx, x1[1], h[2])
    curp1= rs.AddPoint(c1)
    curp2= rs.AddPoint(c2)
    curl = rs.AddLine(curp1, curp2)
    rs.DeleteObject(curp1)
    rs.DeleteObject(curp2)
    lstCur = rs.ProjectCurveToSurface(curl, surface, (0,1,0))