#Wall based on DetailLines
from Autodesk.Revit.DB import *

doc = __revit__.ActiveUIDocument.Document

level = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsNotElementType().FirstElement().Id
DetailLines = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Lines).WhereElementIsNotElementType().ToElements()

lines = []
for line in DetailLines:
	StartPoint = line.GeometryCurve.GetEndPoint(0)
	EndPoint = line.GeometryCurve.GetEndPoint(1)	
	lines.append(Line.CreateBound(StartPoint,EndPoint))
wallTransaction = Transaction(doc,"Paredes")

wallTransaction.Start()
sub = SubTransaction(doc)

for line in lines:
		if sub.Start() == TransactionStatus.Started:	
		    wall = Wall.Create(doc, line, level,True)
		    sub.Commit()
	    
