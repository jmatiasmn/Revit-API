#Code based on TwentyTwo Example

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.Attributes import *

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

PARAMETERS = [BuiltInParameter.ELEM_FAMILY_AND_TYPE_PARAM,BuiltInParameter.WALL_BASE_CONSTRAINT, BuiltInParameter.HOST_AREA_COMPUTED, BuiltInParameter.CURVE_ELEM_LENGTH]

t = Transaction(doc,"Create Schedule")

t.Start()

WallCategoryId = ElementId(BuiltInCategory.OST_Walls)
Schedule = ViewSchedule.CreateSchedule(doc,WallCategoryId)
Schedule.Name = "Wall Schedule Examples"

FamilyTypeSorting = None
BaseConstraintFilter = None

def CheckField(vs):
	global PARAMETERS
	for bip in PARAMETERS:
		if ElementId(bip) == vs.ParameterId:
			return True
		return False
		
def GetLevelByName(doc, name):
	levels = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsNotElementType().ToElements()
	for level in levels:
		if level.Name == name:
			return level

for sf in Schedule.Definition.GetSchedulableFields():
	print(sf)
	for bip in PARAMETERS:
		if ElementId(bip) == sf.ParameterId:
			scheduleField = Schedule.Definition.AddField(sf)
			
			if sf.ParameterId == ElementId(BuiltInParameter.WALL_BASE_CONSTRAINT):
				BaseConstraintFilter = ScheduleFilter(scheduleField.FieldId,ScheduleFilterType.Equal,GetLevelByName(doc,"Level 1").Id)
				Schedule.Definition.AddFilter(BaseConstraintFilter)
		
			if sf.ParameterId == ElementId(BuiltInParameter.ELEM_FAMILY_AND_TYPE_PARAM):
				FamilyTypeSorting = ScheduleSortGroupField(scheduleField.FieldId)
				Schedule.Definition.AddSortGroupField(FamilyTypeSorting)	
		
		
		
t.Commit()
