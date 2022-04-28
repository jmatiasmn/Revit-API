#Walls by points
from Autodesk.Revit.DB import *

doc = __revit__.ActiveUIDocument.Document

inicial = XYZ(0, 0, 0)
final = XYZ(0, 50, 0)
geomLine = Line.CreateBound(inicial,final)

level = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsNotElementType().FirstElement().Id

wallTransatcion = Transaction(doc,"test")

if wallTransatcion.Start() == TransactionStatus.Started:
    wall = Wall.Create(doc, geomLine, level,True)

wallTransatcion.Commit()

