class RedFlag:
    def __init__(self, f_id, createdBy, location, status, comment):
        self.f_id = f_id
        self.createdBy = createdBy
        self.location = location
        self.status = status
        self.comment = comment
    def to_json(self):
        return {'f_id' : self.f_id, 'createdBy' : self.createdBy, 'location': self.location, 'status': self.status, 'comment': self.comment}   



    

    