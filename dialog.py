class DialogDTO:
    def __init__(self, Name, CreatedBy, CreatedDate, ModifiedBy, ModifiedDate):
        self.Name = Name
        self.CreatedBy = CreatedBy
        self.CreatedDate = CreatedDate
        self.ModifiedBy = ModifiedBy
        self.ModifiedDate = ModifiedDate

    def fromDBObject(self, dbObject):
        self.Name = dbObject.Name
        self.CreatedBy = dbObject.CreatedBy
        self.CreatedDate = dbObject.CreatedDate
        self.ModifiedBy = dbObject.ModifiedBy
        self.ModifiedDate = dbObject.ModifiedDate
        return self