import rhinoscriptsyntax as rs

surface = rs.GetObject("Select surface to project onto", rs.filter.surface)

curve = rs.GetObject("Select curve to project", rs.filter.curve)

# Project down...

results = rs.ProjectCurveToSurface(curve, surface, (0,1,0))

print len(results)