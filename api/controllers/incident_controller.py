from flask import request, jsonify
from api.models.incident_model import RedFlag, IncidentData 
from api.helpers.validation import validate_create_redflag_data

my_redflags = IncidentData()

class IncidentController:

    def index(self):
        # welcome message
        return jsonify(
            {
                "message": [
                    "Welcome to Mwesigwa\'s iReporter APIs home",
                    "Endpoints",
                    "#1 : GET /api/v1/red-flags",
                    "#2 : GET /api/v1/red-flags/<red_flag_id>",
                    "#3 : POST /api/v1/red-flags",
                    "#4 : PATCH /api/v1/red-flags/<red_flag_id>/location",
                    "#5 : PATCH /api/v1/red-flags/<red_flag_id>/comment",
                    "#6 : DELETE /api/v1/red-flags/<red_flag_id>"
                    ]
            })
            

    def create_redflag(self):
        # create a red-flag
        data = request.get_json()
        title = data.get('title')
        location = data.get('location')
        comment = data.get('comment')
        images = data.get('images')
        videos = data.get('videos')
        createdBy = request.headers["userId"]
        incidentId = len(my_redflags.redflags)+1
    
        # check for empty request
        if not request.data:
            return jsonify({
                'error': 'Request Cannot Be Empty',
                'status': 400
            }), 400
        #ensuring data format being posted is json
        if request.content_type != 'application/json':
            return jsonify({
                "status": "400",
                "message": "Data input must be in json format"
            })

        # validate the input data
        if validate_create_redflag_data(data):
            return jsonify({"error": 400,
                            "message": validate_create_redflag_data(data)
                            }), 400

        flag_record = RedFlag(
            incident_id = incidentId,
            location = location,
            created_by = createdBy,
            title = title,
            comment = comment,
            images = images,
            videos = videos
        )

        my_redflags.create_redflag(flag_record)
        
        return jsonify({'status': 201, 'data': [{
            "id": incidentId,
            "message": "created red-flag record successfully" 
            }]
            }),201

    def get_all_redflags(self):
        # get all existing red-flags
        json_redflags = []
        for redflag in my_redflags.redflags:
            json_redflags.append(redflag.to_json())
        return jsonify({'status': 200, 'data': json_redflags})

    def get_redflag(self, red_flag_id):
        # get a specific red-flag based on its id
        for redflag in my_redflags.redflags:
            if redflag.__dict__['incidentId'] == red_flag_id:
                return jsonify({
                    'status': 302,
                    'data': [redflag.to_json()]
                }), 302

        return jsonify({
            'status': 204,
            'error': 'That red-flag record does not exist'
        }), 200

    def delete_record(self, red_flag_id):
        # delete a single red-flag record by its id
        for redflag in my_redflags.redflags:
            if redflag.__dict__['incidentId'] == red_flag_id:
                my_redflags.redflags.remove(redflag)
                return jsonify({
                    'status': 200,
                    'data': [{
                        'id': redflag.__dict__['incidentId'],
                        'message': 'red-flag record with id {} has been deleted successfully'.format(redflag.__dict__['incidentId'])
                    }]
                }), 200

        return jsonify({
            'status': 204,
            'error': 'That red-flag record does not exist'
        }), 404

    def edit_location(self, red_flag_id):
        # edit specific red-flag record location
        if not request.json:
            return jsonify({
                'status': 400,
                'error': 'There is no request data given, Provide new location'
            }), 400
        new_location = request.get_json()
        if 'location' not in new_location:
            return jsonify({
                "status": 400,
                "error": "wrong location format. follow this example ->> 'location':{'lat': '0.55767630', 'long': '0.355475685'}"
            }), 417

        for redflag in my_redflags.redflags:
            if redflag.__dict__["incidentId"] == red_flag_id:
                redflag.__dict__["location"] = new_location["location"]
                return jsonify({
                    "status": 202,
                    "data": [{
                        "message": "Location of red-flag record id {} updated to {}".format(red_flag_id, new_location["location"])
                    }]
                }), 202

        return jsonify({
            "status": 404,
            "error": "Sorry, that red-flag record does\'t exist"
        }), 404

    def edit_comment(self, red_flag_id):
        # edit red-flag record  comment
        if not request.json:
            return jsonify({
                'status': 400,
                'error': 'There is no request data given, Provide new comment'
            }), 400
        new_comment = request.get_json()
        if 'comment' not in new_comment:
            return jsonify({
                "status": 400,
                "error": "wrong comment format. follow this example ->> 'comment':'My red-flag comment'"
            }), 417

        for redflag in my_redflags.redflags:
            if redflag.__dict__["incidentId"] == red_flag_id:
                redflag.__dict__["comment"] = new_comment["comment"]
                return jsonify({
                    "status": 202,
                    "data": [{
                        "message": "comment of red-flag record id {} updated to {}".format(red_flag_id, new_comment["comment"])
                    }]
                }), 202

        return jsonify({
            "status": 404,
            "error": "Sorry, that red-flag record does\'t exist"
        }), 404
