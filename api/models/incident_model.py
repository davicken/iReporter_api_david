from datetime import datetime
current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

class Incident:
    def __init__(self, **kwargs):
        self.incidentId = kwargs["incident_id"]
        self.title = kwargs["title"]
        self.location = kwargs["location"]
        self.createdOn = current_time
        self.createdBy = kwargs["created_by"]
        self.images = kwargs["images"]
        self.videos = kwargs["videos"]
        self.comment = kwargs["comment"]
        self.status = "draft"


class RedFlag(Incident):
    def __init__(self, **kwargs):
        self.incType = "red-flag"
        super().__init__(**kwargs)

    def to_json(self):
        return {
            'id': self.incidentId,
            'title': self.title,
            'type': self.incType,
            'createdOn': self.createdOn,
            'createdBy': self.createdBy,
            'location': self.location,
            'status': self.status,
            'comment': self.comment,
            'images': self.images,
            'videos': self.videos
        }

class Intervention(Incident):
    def __init__(self, **kwargs):
        self.incType = "intervention"
        super().__init__(**kwargs)

    def to_json(self):
        return {
            'id': self.incidentId,
            'title': self.title,
            'type': self.incType,
            'createdOn': self.createdOn,
            'createdBy': self.createdBy,
            'location': self.location,
            'status': self.status,
            'comment': self.comment,
            'images': self.images,
            'videos': self.videos
        }


class IncidentData: 
    # class for managing data of incidents

    def __init__(self):
        self.redflags = []
        self.interventions = []

   
   