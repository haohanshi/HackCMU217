import checkpoints.py
import globalVal.py

global CPList

'''
Location Naming Standardization: Type_Building_Level_Number
'''
class location:
    def __init__(self,name,type,building,level,number):
        self.name=name
        self.type=type
        self.building=building
        self.level=level
        self.number=number

    def Name(self):
        return self.name

    def Type(self):
        return self.type

    def Building(self):
        return self.building

    def Level(self):
        return self.Level

    def Number(self):
        return self.Number



        

'''
path: heuristic, legal status, stations(printer,cafe,restroom,vending)
'''
class stations:
    def __init__(self,have==True,printer,cafe,restroom,vending):
        self.have=have
        self.printer=printer
        self.cafe=cafe
        self.restroom=restroom
        self.vending=vending

    def Have(self):
        return self.have

    def Printer(self):
        return self.printer

    def Cafe(self):
        return self.cafe

    def Restroom(self):
        return self.restroom

    def Vending(self):
        return self.vending


class path:
    def __init__(self, cp1, cp2, type, eta = 0):
        self.cp1 = cp1
        self.cp2 = cp2
        self.heuristic=0
        self.legal=1
        self.stations=None
        self.eta = eta
        self.type = type

    def Heuristic(self):
        return self.heuristic

    def Legal(self):
        return self.legal

    def Stations(self):
        return self.stations

    def Cp1(self):
        return self.cp1

    def Cp2(self):
        return self.cp2

    def Type(self):
        return self.type

    def ETA(self):
        return self.eta


'''
Generating Path Objects
e.g. WEH5312_to_DH2210
Input: location names
Output: path objects
'''

def listOfPoints(num_cp,locList):
    cpList = []
    for i in range(num_cp):
        cpList.append(location(locList[i][0], locList[i][1], locList[i][2], locList[i][3], locList[i][4]))
    return cpList

def listOfpaths(CPList):
    Paths = {}
    num_cp = len(CPList)
    cpList = listOfPoints(num_cp)
    for i in range(num_cp):
        for j in range(num_cp):
            if i != j:
                loc1 = cpList[i]
                loc2 = cpList[j]
                setupPath(loc1,loc2,Paths)
    return Paths

def setupPath(loc1,loc2,Paths):
    path_name=loc1.Name+"_to_"+loc2.Name
    if (loc1.Type == "Stair" and loc2.Type == "Stair"):
        pathType = "Stair"
    else if (loc1.Type == "Elevator" and loc2.Type == "Elevator"):
        pathType = "Elevator"
    else if (loc1.Type == "Entrance" and loc2.Type == "Entrance"):
        pathType = "Road"
    else:
        pathType = "Corridor"
    # else if (loc1.Type == "Entrance" and loc2.Type == "Room"):
    #     pathType = "Corridor"
    # else if (loc2.Type == "Entrance" and loc1.Type == "Room"):
    #     pathType = "Corridor"
    # else if (loc1.Type == "Entrance" and loc2.Type == "Stair"):
    #     pathType = "Corridor"
    # else if (loc1.Type == "Entrance" and loc2.Type == "Elevator"):
    #     pathType = "Corridor"
    # else if (loc2.Type == "Entrance" and loc1.Type == "Stair"):
    #     pathType = "Corridor"
    # else if (loc2.Type == "Entrance" and loc1.Type == "Elevator"):
    #     pathType = "Corridor"
    # else if (loc1.Type == "Room" and loc2.Type == "Stair"):
    #     pathType = "Corridor"
    # else if (loc1.Type == "Room" and loc2.Type == "Elevator"):
    #     pathType = "Corridor"
    # else if (loc2.Type == "Room" and loc1.Type == "Stair"):
    #     pathType = "Corridor"
    # else if (loc2.Type == "Room" and loc1.Type == "Elevator"):
    #     pathType = "Corridor"
    # else if (loc1.Type == "Room" and loc2.Type == "Room"):
    #     pathType = "Corridor"
    Paths[path_name]=path(loc1, loc2, pathType)

def isLegal(Paths):
    for key in Paths:
        path = Paths[key]
        if path.cp1.Building == "WEH" and path.cp2.Building == "DH" and path.cp1.Level == 5 and path.cp2.Level == 0:
            res = True
        else if path.cp1.Building != path.cp2.Building:
            res = False
        else if path.cp1.Level == path.cp2.Level:
            res = True
        else if path.cp1.Type == "Elevator" and path.cp2.Type == "Elevator" and abs(path.cp1.Level - path.cp2.Level) == 1:
            res = True
        else if path.cp1.Type == "Stair" and path.cp2.Type == "Stair" and abs(path.cp1.Level - path.cp2.Level) == 1:
            res = True
        else:
            res = False
        path.legal = res

def getHeuristics(Paths):
    for key in Paths:
        path = Paths[key]
        if path.legal:
            if path.Type == "Corridor":
                path.heuristic = 2 - Preferences.Indoor * 0.5
            else if path.Type == "Out":
                path.heuristic = Preferences.Indoor * 0.5
            else if path.Type == "Stair":
                path.heuristic = 1 - Preferences.stair * 0.5
            else if path.Type == "Elevator":
                path.heuristic = Preferences.stair * 0.5 + 0.5
        else:
            path.heuristic = 1000
    

def main():
    pass









