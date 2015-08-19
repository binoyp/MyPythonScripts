import rhinoscriptsyntax as rs
def export_curdatapoints():
    object_id = rs.GetObject("Select curve", rs.filter.curve)
    if( object_id==None ): return

    #Get the filename to create
    filter = "Text File (*.shf)|*.shf|All Files (*.*)|*.*||"
    filename = rs.SaveFileName("Save point coordinates as", filter)
    if( filename==None ): return
    if rs.IsCurveClosed(object_id):
        start_point = rs.GetPoint("Base point of center line")
    
        end_point = rs.GetPoint("Endpoint of center line", start_point)
        
        points = rs.CurveContourPoints(object_id, start_point, end_point)
    else:
        points = rs.CurveContourPoints(object_id,rs.CurveStartPoint(object_id),rs.CurveEndPoint(object_id))
    if not points: return
    

    file = open( filename, "w" )
    for pt in points:
        print(str(pt.X)+","+str(pt.Y)+","+str(pt.Z))
        file.write( str(pt.X) )
        file.write( ", " )
        file.write( str(pt.Y) )
        file.write( ", " )
        file.write( str(pt.Z) )
        file.write( "\n" )
    file.close()

    
if __name__ == "__main__":
    export_curdatapoints()

