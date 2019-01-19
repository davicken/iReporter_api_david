from datetime import datetime
current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
class Incident:
    def __init__(self, **kwargs):
        self.inc_id = kwargs["id"]
        self.location = kwargs["loc"]
        self.createdOn = current_time
        self.createdBy = 7
        self.images = kwargs["image"]
        self.videos = kwargs["vid"]
        self.comment = kwargs["comment"]
        self.status = "draft"

class RedFlag(Incident):
    def __init__(self, **kwargs):
        self.inc_type = "red-flag"
        super().__init__(**kwargs)

    def to_json(self):
        return {'inc_id': self.inc_id, 'inc_type': self.inc_type, 'createdOn': self.createdOn, 'createdBy': self.createdBy, 'location': self.location, 'status': self.status, 'comment': self.comment, 'images': self.images, 'videos': self.videos}
