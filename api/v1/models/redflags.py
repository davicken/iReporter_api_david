
class Incident:
    def __init__(self, inc_id, location, createdOn, createdBy, status, comment, images, videos):
        self.inc_id = inc_id
        self.location = location
        self.createdOn = createdOn
        self.createdBy = createdBy
        self.images = images
        self.videos = videos
        self.comment = comment
        self.status = status

class RedFlag(Incident):
    def __init__(self, inc_type, inc_id, location, createdOn, createdBy, status, comment, images, videos):
        self.inc_type = inc_type
        super().__init__(inc_id, location, createdOn, createdBy, status, comment, images, videos)

    def to_json(self):
        return {'inc_id' : self.inc_id, 'inc_type' : self.inc_type, 'createdOn' : self.createdOn, 'createdBy' : self.createdBy, 'location': self.location,'status': self.status, 'comment': self.comment, 'images': self.images, 'videos': self.videos}   


