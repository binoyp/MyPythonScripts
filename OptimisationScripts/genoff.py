import rhinoscriptsyntax as rs
import math
import Rhino.Geometry.Point3d

_BOW ="""35.93127          0.00000          0.52150          1
35.94223          0.00000          0.55251          0
35.95212          0.00000          0.58358          0
35.96105          0.00000          0.61471          0
35.96908          0.00000          0.64589          0
35.97631          0.00000          0.67713          0
35.98278          0.00000          0.70842          0
35.98857          0.00000          0.73975          0
35.99372          0.00000          0.77112          0
35.99829          0.00000          0.80253          0
36.00232          0.00000          0.83397          0
36.00586          0.00000          0.86544          0
36.00895          0.00000          0.89694          0
36.01162          0.00000          0.92847          0
36.01392          0.00000          0.96002          0
36.01587          0.00000          0.99159          0
36.01752          0.00000          1.02319          0
36.01888          0.00000          1.05480          0
36.01999          0.00000          1.08642          0
36.02089          0.00000          1.11806          0
36.02160          0.00000          1.14971          0
36.02214          0.00000          1.18138          0
36.02255          0.00000          1.21305          0
36.02285          0.00000          1.24472          0
36.02308          0.00000          1.27641          0
36.02325          0.00000          1.30809          0
36.02340          0.00000          1.33978          0
36.02355          0.00000          1.37147          0
36.02372          0.00000          1.40315          0
36.02390          0.00000          1.43484          0
36.02410          0.00000          1.46652          0
36.02432          0.00000          1.49820          0
36.02456          0.00000          1.52989          0
36.02481          0.00000          1.56157          0
36.02508          0.00000          1.59325          0
36.02536          0.00000          1.62493          0
36.02566          0.00000          1.65660          0
36.02597          0.00000          1.68828          0
36.02630          0.00000          1.71996          0
36.02664          0.00000          1.75163          0
36.02700          0.00000          1.78330          0
36.02737          0.00000          1.81498          0
36.02775          0.00000          1.84665          0
36.02815          0.00000          1.87832          0
36.02856          0.00000          1.90999          0
36.02898          0.00000          1.94166          0
36.02942          0.00000          1.97333          0
36.02987          0.00000          2.00500          0
36.03032          0.00000          2.03667          0
36.03079          0.00000          2.06833          0
36.03127          0.00000          2.10000          0
"""
_STERN="""0.00000          0.00000          0.00000          1
-0.00000          0.00000          0.03812          0
-0.00001          0.00000          0.07623          0
-0.00002          0.00000          0.11435          0
-0.00006          0.00000          0.15246          0
-0.00011          0.00000          0.19056          0
-0.00020          0.00000          0.22865          0
-0.00032          0.00000          0.26674          0
-0.00049          0.00000          0.30481          0
-0.00071          0.00000          0.34286          0
-0.00099          0.00000          0.38090          0
-0.00135          0.00000          0.41892          0
-0.00179          0.00000          0.45691          0
-0.00233          0.00000          0.49488          0
-0.00297          0.00000          0.53282          0
-0.00374          0.00000          0.57072          0
-0.00465          0.00000          0.60858          0
-0.00571          0.00000          0.64640          0
-0.00695          0.00000          0.68417          0
-0.00839          0.00000          0.72189          0
-0.01004          0.00000          0.75954          0
-0.01193          0.00000          0.79713          0
-0.01409          0.00000          0.83464          0
-0.01656          0.00000          0.87206          0
-0.01935          0.00000          0.90940          0
-0.02252          0.00000          0.94663          0
-0.02611          0.00000          0.98374          0
-0.03015          0.00000          1.02072          0
-0.03471          0.00000          1.05756          0
-0.03985          0.00000          1.09424          0
-0.04563          0.00000          1.13073          0
-0.05213          0.00000          1.16702          0
-0.05945          0.00000          1.20309          0
-0.06768          0.00000          1.23890          0
-0.07696          0.00000          1.27441          0
-0.08742          0.00000          1.30959          0
-0.09923          0.00000          1.34440          0
-0.11259          0.00000          1.37876          0
-0.12768          0.00000          1.41265          0
-0.14465          0.00000          1.44600          0
-0.16366          0.00000          1.47879          0
-0.18487          0.00000          1.51095          0
-0.20844          0.00000          1.54246          0
-0.23456          0.00000          1.57324          0
-0.26338          0.00000          1.60327          0
-0.29504          0.00000          1.63251          0
-0.32961          0.00000          1.66092          0
-0.36713          0.00000          1.68851          0
-0.40750          0.00000          1.71530          0
-0.45051          0.00000          1.74135          9
"""
def getSurfaces():
    surface = rs.ObjectsByType(8)
    hidobj = rs.HiddenObjects()
    if hidobj:
        for obj in hidobj:
            rs.ShowObject(obj)
    outDic = {'mod' : None, 'ref' : None}
    for srf in surface:
        print rs.ObjectName(srf)
        if rs.ObjectName(srf) == "ref":
            #rs.HideObject(srf)
            outDic['ref'] = srf
        elif rs.ObjectName(srf) == "mod":
            outDic['mod'] = srf   
        else:
            rs.DeleteObject(srf)
    for obj in hidobj:
            rs.HideObject(obj)
    return outDic
def trimSurface(sur):
    #sur = getSurfaces()['ref']
    pl =rs.AddPlaneSurface( rs.WorldXYPlane(), 40000.0, 6000.0 )
    rs.MoveObject(pl, (-3000,-500, 2100))
    lsrf = rs.SplitBrep ( sur, pl )   
    rs.DeleteObject(pl)
    rs.DeleteObject(lsrf[0])
    rs.DeleteObject(sur)
    rs.ObjectName(lsrf[1],'mod')
    return lsrf[1]
    
def transformSrf(obj, dicTr):
    if obj:
        point_count = rs.SurfacePointCount(obj)
        points = rs.SurfacePoints(obj)
        knots = rs.SurfaceKnots(obj)
        degree = rs.SurfaceDegree(obj)
    else:
        return None
    for k in dicTr:
        points[k] = dicTr[k]
    if rs.IsSurfaceRational(obj):
        weights = rs.SurfaceWeights(obj)
        objout = rs.AddNurbsSurface(point_count, points, knots[0], knots[1], degree, weights)
    else:
        objout = rs.AddNurbsSurface(point_count, points, knots[0], knots[1], degree)
    if objout: 
        rs.SelectObject(objout)
        rs.ObjectName(objout,"mod")
        return objout
    else:
        return objout
def genOffFile():
    x1 = 35859.39
    x2 = 0.0
    h = 3000.0
    n = 50
    dx = x1 / n
    print dx
    
    #  file for saving shf file

    filename = "test.txt"
    ###
    file = open( filename, "w" )
    file.write("hull \n")
    file.write(_BOW)
    srfdic = getSurfaces()
    surface = srfdic['mod']
    
    for i in range(0,n+1):
        flg_stn = 1
        c1= (x1 - i*dx, 5000, -1000)
        c2= (x1 - i*dx, 5000, h)
        curp1= rs.AddPoint(c1)
        curp2= rs.AddPoint(c2)
        curl = rs.AddLine(curp1, curp2)
        rs.DeleteObject(curp1)
        rs.DeleteObject(curp2)
        lstCur = rs.ProjectCurveToSurface(curl, surface, (0,1,0))
        rs.DeleteObject(curl)
        if len(lstCur) <> 1 :
            print "Error in Projection"
        else:
    
            if rs.CurveStartPoint(lstCur[0])[2] < rs.CurveEndPoint(lstCur[0])[2]:
                sp = rs.CurveStartPoint(lstCur[0])
                lp = rs.CurveEndPoint(lstCur[0])
            else:
                lp = rs.CurveStartPoint(lstCur[0])
                sp = rs.CurveEndPoint(lstCur[0])
                
            points = rs.CurveContourPoints(lstCur[0],sp,lp)
            npts = len(points)
            cpt  =  1
            for pt in points:
                #print(str(pt.X)+","+str(pt.Y)+","+str(pt.Z))
                file.write( "{:.5f}".format(pt.X/1000.0))
                file.write( " " * 10)
                file.write( "{:.5f}".format(abs(pt.Y)/1000.0) )
                file.write( " " * 10)
                file.write( "{:.5f}".format(pt.Z/1000.0) )
                file.write( " " * 10)
                file.write( str(flg_stn) )
                file.write( "\n" )
                flg_stn = 0
                cpt += 1
        
            rs.DeleteObject(lstCur[0])
    file.write(_STERN)
    file.write("end")
    file.close()        
    
def moveDic(_dic, vect):
    for k in _dic:
        _dic[k] = rs.PointAdd(_dic[k], vect[k])
    return _dic
def readTrfFyl():
    f = open('trf.csv','r')
    retDic={}
    for line in f:
        tlist = [float(k) for k in line.split(',')]
        retDic[int(tlist[0])] = Rhino.Geometry.Point3d(tlist[1], tlist[2], tlist[3])
    f.close()
    return retDic
def init():
    dicSur = getSurfaces()
    print dicSur
    if dicSur['mod']:
        rs.DeleteObject(dicSur['mod'])
    if dicSur['ref']:
        surface = dicSur['ref']
    else:
        raise RuntimeError, "No surface"
    vec = readTrfFyl()
    points = rs.SurfacePoints(surface)
    seldic = {k:points[k] for k in vec.keys()}
    trTic = moveDic(seldic, vec)
    srf = transformSrf(surface, trTic)
    msrf = trimSurface(srf)
    rs.HideObject(surface)
    genOffFile()
    rs.DeleteObject(msrf)
    rs.ShowObject(surface)
if __name__ == '__main__':
    init()
