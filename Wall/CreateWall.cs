public void CreateWall()
{
	Document doc = this.ActiveUIDocument.Document;
	XYZ start = new XYZ(0, 0, 0);
	XYZ end = new XYZ(10, 10, 0);
	Line geomLine = Line.CreateBound(start, end);
	ElementId level = new FilteredElementCollector(doc)
	.OfCategory(BuiltInCategory.OST_Levels)
	.WhereElementIsNotElementType()
	.FirstElement().Id;

	using (Transaction t = new Transaction(doc,"Create Wall")) 
	{
		t.Start();

		Wall wall = Wall.Create(doc,geomLine,level,false);
		t.Commit();

	}
}
